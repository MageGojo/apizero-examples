"""Fetch and parse the live ApiZero catalog.

Official machine docs moved off OpenAPI / llms-full (404 / 410).
Current sources:

- https://apizero.cn/sitemap.xml
- https://apizero.cn/aidocs/{slug}/raw.md
- https://apizero.cn/llms.txt
"""

from __future__ import annotations

import datetime as dt
import json
import re
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
CACHE_DIR = ROOT / "data" / "cache" / "raw"

SITEMAP_URL = "https://apizero.cn/sitemap.xml"
LLMS_URL = "https://apizero.cn/llms.txt"
AIDOCS_BASE = "https://apizero.cn/aidocs"
MARKETPLACE_BASE = "https://apizero.cn/marketplace"
RAW_DOC_TMPL = AIDOCS_BASE + "/{slug}/raw.md"

CATEGORY_FROM_LABEL = {
    "生活服务": "life",
    "文档识别": "ocrdata",
    "金融数据": "finance",
    "AI 能力": "ai",
    "地理位置": "geo",
    "身份核验": "kyc",
    "内容娱乐": "content",
    "开发工具": "dev",
    "招中标": "tender",
}

CATEGORY_LABELS = {code: label for label, code in CATEGORY_FROM_LABEL.items()}

KNOWN_USAGE = {
    "weather": {"calls_30d": 17379, "errors_30d": 62},
    "barcode-gs1": {"calls_30d": 1805, "errors_30d": 255},
    "video-parse": {"calls_30d": 835, "errors_30d": 359},
    "qq": {"calls_30d": 577, "errors_30d": 19},
    "moji-weather": {"calls_30d": 441, "errors_30d": 14},
    "barcode-lookup": {"calls_30d": 164, "errors_30d": None},
}

GROWTH_OVERRIDES = {
    "weather": {
        "tier": "A-core",
        "action": "主推",
        "angle": "免费天气 API；城市名直接查；适合小程序、网站天气模块、日报脚本。",
    },
    "barcode-lookup": {
        "tier": "A-core",
        "action": "主推",
        "angle": "免费商品条码查询；适合库存录入、电商资料补全、扫码工具。",
    },
    "barcode-gs1": {
        "tier": "A-verify",
        "action": "验证后主推",
        "angle": "PRO 商品条码查询；发文前先用真实条码验证，降低新用户复制失败率。",
    },
    "qq": {
        "tier": "A-core",
        "action": "主推",
        "angle": "QQ 头像昵称 API；适合头像展示、轻量用户资料补全、网页小工具。",
    },
    "moji-weather": {
        "tier": "A-core",
        "action": "主推",
        "angle": "墨迹天气；和 weather 合并做天气专题，对比字段丰富度和使用场景。",
    },
    "video-parse": {
        "tier": "C-caution",
        "action": "只做排错/合规指南",
        "angle": "错误率高，暂不作为拉新入口；只讲合法使用、常见错误和可测试输入。",
    },
    "hot-baidu": {
        "tier": "B-support",
        "action": "补充推广",
        "angle": "百度热搜 API；适合公众号、AI 写作工具、热点选题池。",
    },
    "movie-box": {
        "tier": "B-support",
        "action": "补充推广",
        "angle": "实时电影票房 API；适合影视数据看板和小项目教程。",
    },
    "fund": {
        "tier": "B-support",
        "action": "补充推广",
        "angle": "基金估值 API；适合 Python 自用脚本、看板、投资工具教程。",
    },
    "bus-realtime": {
        "tier": "B-support",
        "action": "补充推广",
        "angle": "实时公交 API；适合城市出行小程序、通勤提醒工具。",
    },
    "whois": {
        "tier": "B-support",
        "action": "补充推广",
        "angle": "Whois 域名查询；适合站长工具、域名监控、开发者脚本。",
    },
    "ssl": {
        "tier": "B-support",
        "action": "补充推广",
        "angle": "SSL 证书查询；适合站长工具、证书到期提醒。",
    },
    "dns-lookup": {
        "tier": "B-support",
        "action": "补充推广",
        "angle": "DNS 查询 API；适合开发者工具、域名诊断、运维脚本。",
    },
    "webmeta": {
        "tier": "B-support",
        "action": "补充推广",
        "angle": "网页 Meta 信息提取；适合链接预览、采集前预处理、站点分析。",
    },
    "content-extract": {
        "tier": "B-support",
        "action": "补充推广",
        "angle": "网页正文提取；适合 RAG、AI 摘要、内容采集前清洗。",
    },
    "stock-trend": {
        "tier": "B-support",
        "action": "补充推广",
        "angle": "A股实时行情；免费额度可跑通，适合行情看板和量化入门。",
    },
    "drug-insert": {
        "tier": "B-support",
        "action": "补充推广",
        "angle": "药品说明书查询；先搜名称再拉详情，适合健康工具教程。",
    },
    "express-pro": {
        "tier": "B-support",
        "action": "补充推广",
        "angle": "快递查询 PRO；可不传公司自动识别，适合物流看板。",
    },
    "football": {
        "tier": "B-support",
        "action": "补充推广",
        "angle": "足球赛事赛程；适合比分看板和赛程提醒。",
    },
    "basketball": {
        "tier": "B-support",
        "action": "补充推广",
        "angle": "篮球赛事赛程；适合 NBA/CBA 看板。",
    },
    "ai-chat": {
        "tier": "B-support",
        "action": "补充推广",
        "angle": "大模型统一网关；对话/生图/视频同一 Completions 地址，默认经济档。",
    },
    "douyin-search": {
        "tier": "C-caution",
        "action": "只做排错/合规指南",
        "angle": "抖音搜索对输入和平台策略敏感，只讲合法查询和常见错误。",
    },
    "douyin-works": {
        "tier": "C-caution",
        "action": "只做排错/合规指南",
        "angle": "抖音作品列表对登录态和链接格式敏感，不作为拉新入口。",
    },
}

DEFAULT_GROWTH = {
    "tier": "D-inventory",
    "action": "先收录",
    "angle": "先放入接口库，等站内调用量或搜索需求上来后再写专项内容。",
}

DEMO_QUERY_PARAMS = {
    "weather": {"city": "北京", "type": "weather"},
    "moji-weather": {"city": "北京"},
    "barcode-lookup": {"barcode": "6921168509256"},
    "barcode-gs1": {"code": "6921168509256"},
    "qq": {"qq": "10001"},
    "hot-baidu": {},
    "movie-box": {},
    "fund": {"action": "estimate", "code": "005827"},
    "whois": {"domain": "apizero.cn"},
    "ssl": {"domain": "apizero.cn"},
    "webmeta": {"url": "https://apizero.cn"},
    "content-extract": {"url": "https://apizero.cn"},
    "drug-insert": {"name": "阿莫西林"},
    "stock-trend": {"code": "600519", "type": "simple"},
    "football": {},
    "basketball": {},
}


USER_AGENT = "ApiZeroExamplesExport/1.2 (+https://github.com/MageGojo/apizero-examples)"


def fetch_text(url: str, retries: int = 3) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    last_error: Exception | None = None
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(request, timeout=40) as response:
                return response.read().decode("utf-8")
        except (urllib.error.URLError, TimeoutError) as error:
            last_error = error
            time.sleep(0.4 * (attempt + 1))
    raise RuntimeError(f"failed to fetch {url}: {last_error}")


def clean_text(value: str | None) -> str:
    if not value:
        return ""
    return re.sub(r"\s+", " ", value.replace("\u3000", " ")).strip()


def strip_cell(value: str) -> str:
    value = value.strip().strip("|").strip()
    value = value.replace("\u3000", " ")
    if value.startswith("`") and value.endswith("`") and value.count("`") == 2:
        value = value[1:-1]
    return value.strip()


def parse_sitemap_slugs(xml_text: str) -> list[str]:
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    root = ET.fromstring(xml_text)
    slugs: list[str] = []
    seen: set[str] = set()
    for loc in root.findall(".//sm:loc", ns):
        if not loc.text:
            continue
        path = urlparse(loc.text.strip()).path
        if not path.startswith("/marketplace/"):
            continue
        parts = [part for part in path.split("/") if part]
        if len(parts) != 2:
            continue
        slug = parts[1]
        if slug in seen or slug in {"", "sub"}:
            continue
        seen.add(slug)
        slugs.append(slug)
    return slugs


def quota_number(raw: str) -> str:
    raw = clean_text(raw)
    if not raw or raw in {"无", "—", "-", "N/A"}:
        return ""
    match = re.search(r"([\d,]+)", raw)
    return match.group(1).replace(",", "") if match else ""


def parse_kv_table(markdown: str) -> dict[str, str]:
    rows: dict[str, str] = {}
    for line in markdown.splitlines():
        if not line.startswith("|"):
            continue
        cells = [strip_cell(cell) for cell in line.strip().strip("|").split("|")]
        if len(cells) < 2:
            continue
        key, value = cells[0], cells[1]
        if key in {"字段", "---", ""} or set(key) <= {"-", ":"}:
            continue
        rows[key] = value
    return rows


def parse_param_tables(markdown: str) -> list[dict[str, Any]]:
    params: list[dict[str, Any]] = []
    seen: set[str] = set()
    lines = markdown.splitlines()
    i = 0
    while i < len(lines):
        header = [strip_cell(cell) for cell in lines[i].strip().strip("|").split("|")] if lines[i].startswith("|") else []
        if header[:3] == ["参数", "类型", "必填"]:
            i += 1
            if i < len(lines) and set(lines[i].replace("|", "").replace("-", "").replace(":", "").strip()) == set():
                i += 1
            while i < len(lines) and lines[i].startswith("|"):
                cells = [strip_cell(cell) for cell in lines[i].strip().strip("|").split("|")]
                i += 1
                if len(cells) < 3 or cells[0] in {"参数", "---"}:
                    continue
                name = cells[0].strip("`")
                if not name or name in seen:
                    continue
                if name.startswith("(") or "无查询" in name or name in {"字段", "值"}:
                    continue
                seen.add(name)
                required = cells[2] in {"是", "true", "True", "required"}
                params.append(
                    {
                        "name": name,
                        "required": required,
                        "type": cells[1] if len(cells) > 1 else "",
                        "description": cells[3] if len(cells) > 3 else "",
                        "example": cells[4] if len(cells) > 4 else "",
                    }
                )
            continue
        i += 1
    return params


def extract_json_examples(markdown: str) -> list[dict[str, Any]]:
    examples: list[dict[str, Any]] = []
    for match in re.finditer(r"```json\s*\n(.*?)```", markdown, re.S):
        raw = match.group(1).strip()
        try:
            parsed = json.loads(raw)
        except json.JSONDecodeError:
            continue
        examples.append(
            {
                "status": "200",
                "content_type": "application/json",
                "description": "文档示例",
                "example": parsed,
            }
        )
        if len(examples) >= 2:
            break
    return examples


def extract_curl(markdown: str) -> str:
    for match in re.finditer(r"```(?:bash|sh)?\s*\n(.*?)```", markdown, re.S):
        block = match.group(1).strip()
        if "curl" not in block:
            continue
        block = block.replace("YOUR_API_KEY", "$APIZERO_API_KEY")
        return block
    return ""


def extract_subs(markdown: str) -> list[dict[str, str]]:
    body = markdown
    start = re.search(r"^## 3\. 子能力\s*$", markdown, re.M)
    if start:
        rest = markdown[start.end() :]
        nxt = re.search(r"^## \d+\.", rest, re.M)
        body = rest[: nxt.start()] if nxt else rest
    subs: list[dict[str, str]] = []
    for match in re.finditer(r"^### (?P<title>.+?)\s+\(`(?P<id>[^`]+)`\)\s*$", body, re.M):
        subs.append({"id": match.group("id"), "title": clean_text(match.group("title"))})
    return subs


def description_from_raw(markdown: str) -> str:
    text = re.sub(r"^<!--.*?-->", "", markdown, flags=re.S).strip()
    text = re.sub(r"^# .+\n+", "", text, count=1)
    cut = re.search(r"^## 平台约定\s*$", text, re.M)
    if cut:
        text = text[: cut.start()]
    return text.strip()


def param_info_list(params: list[dict[str, Any]]) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    for param in params:
        result.append(
            {
                "name": param["name"],
                "in": "query",
                "required": bool(param.get("required")),
                "type": param.get("type", ""),
                "description": clean_text(param.get("description", "")),
                "example": param.get("example", ""),
            }
        )
    return result


def sample_value(value: Any, fallback: str) -> str:
    if value is None or value == "":
        return fallback
    return str(value)


def example_body_from_params(params: list[dict[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for param in params:
        result[param["name"]] = sample_value(param.get("example"), f"<{param['name']}>")
    return result


def curl_template(row: dict[str, Any]) -> str:
    if row.get("doc_curl"):
        return row["doc_curl"]

    method = row["method"].upper()
    endpoint = row["endpoint"]
    has_required_query = any(param.get("required") for param in row.get("query_parameters", []))
    should_attach_query = method == "GET" or (method != "POST" and has_required_query)
    demo_params = DEMO_QUERY_PARAMS.get(row["slug"]) if should_attach_query else None
    if demo_params is None and should_attach_query:
        query_params = [
            param
            for param in row.get("query_parameters", [])
            if param.get("name") not in {"key"} and param.get("required")
        ]
        if not query_params:
            query_params = [
                param
                for param in row.get("query_parameters", [])
                if param.get("name") not in {"key"}
            ][:2]
        demo_params = {
            param["name"]: sample_value(param.get("example"), "<" + param["name"] + ">")
            for param in query_params[:4]
        }
    if demo_params:
        query = "&".join(f"{key}={value}" for key, value in demo_params.items())
        endpoint = f"{endpoint}?{query}"

    lines = [
        "curl -sS \\",
        f"  -X {method} \\",
        '  -H "Authorization: Bearer $APIZERO_API_KEY" \\',
    ]
    bodies = row.get("request_bodies") or []
    if bodies:
        body = bodies[0]
        lines.append(f'  -H "Content-Type: {body["content_type"]}" \\')
        example = body.get("example")
        if not example:
            example = example_body_from_params(body.get("fields") or [])
        lines.append(f"  -d '{json.dumps(example, ensure_ascii=False)}' \\")
    lines.append(f'  "{endpoint}"')
    return "\n".join(lines)


def error_rate(calls: int | None, errors: int | None) -> str:
    if not calls or errors is None:
        return ""
    return f"{errors / calls:.2%}"


def growth_for(slug: str) -> dict[str, str]:
    return GROWTH_OVERRIDES.get(slug, DEFAULT_GROWTH)


def parse_raw_md(slug: str, markdown: str) -> dict[str, Any]:
    title_match = re.search(r"^# (.+)$", markdown, re.M)
    info_match = re.search(r"^## 1\. 基本信息\s*$", markdown, re.M)
    info_block = ""
    if info_match:
        rest = markdown[info_match.end() :]
        nxt = re.search(r"^## ", rest, re.M)
        info_block = rest[: nxt.start()] if nxt else rest
    info = parse_kv_table(info_block)

    params = parse_param_tables(markdown)
    query_parameters = param_info_list(params)
    required = [item["name"] for item in query_parameters if item["required"]]
    optional = [item["name"] for item in query_parameters if not item["required"]]

    method = (info.get("请求方法") or "GET").upper()
    request_bodies: list[dict[str, Any]] = []
    if method == "POST" and params:
        request_bodies.append(
            {
                "content_type": "application/json",
                "required": True,
                "schema_type": "object",
                "fields": [
                    {
                        "name": item["name"],
                        "required": item["required"],
                        "type": item["type"],
                        "description": item["description"],
                        "example": item.get("example", ""),
                    }
                    for item in params
                ],
                "example": example_body_from_params(params),
            }
        )

    category_label = info.get("分类") or ""
    category = CATEGORY_FROM_LABEL.get(category_label, category_label)
    usage = KNOWN_USAGE.get(slug, {})
    growth = growth_for(slug)
    description = description_from_raw(markdown)

    row: dict[str, Any] = {
        "slug": info.get("接口标识") or slug,
        "name": info.get("接口名称") or (title_match.group(1).strip() if title_match else slug),
        "method": method,
        "endpoint": info.get("接口地址") or f"https://v1.apizero.cn/api/{slug}",
        "category": category,
        "category_label": category_label or CATEGORY_LABELS.get(category, category),
        "billing": info.get("计费模式", ""),
        "qps": info.get("QPS 限制", ""),
        "free_quota_logged_in": quota_number(info.get("登录免费额度", "")),
        "free_quota_anonymous": quota_number(info.get("匿名每日额度", "")),
        "required_query_params": ", ".join(required),
        "optional_query_params": ", ".join(optional),
        "marketplace_url": f"{MARKETPLACE_BASE}/{slug}",
        "docs_url": f"{AIDOCS_BASE}/{slug}",
        "raw_docs_url": RAW_DOC_TMPL.format(slug=slug),
        "openapi_operation_id": slug.replace("-", "_"),
        "summary": clean_text(description),
        "description": description,
        "growth_tier": growth["tier"],
        "growth_action": growth["action"],
        "promotion_angle": growth["angle"],
        "known_calls_30d": usage.get("calls_30d", ""),
        "known_errors_30d": "" if usage.get("errors_30d") is None else usage.get("errors_30d", ""),
        "known_error_rate": error_rate(usage.get("calls_30d"), usage.get("errors_30d")),
        "parameters": params,
        "query_parameters": query_parameters,
        "header_parameters": [],
        "path_parameters": [],
        "request_bodies": request_bodies,
        "response_examples": extract_json_examples(markdown),
        "sub_interfaces": extract_subs(markdown),
        "doc_curl": extract_curl(markdown),
    }
    row["curl_template"] = curl_template(row)
    return row


def fetch_raw(slug: str) -> str:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache_path = CACHE_DIR / f"{slug}.md"
    text = fetch_text(RAW_DOC_TMPL.format(slug=slug))
    cache_path.write_text(text, encoding="utf-8")
    return text


def build_inventory() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    slugs = parse_sitemap_slugs(fetch_text(SITEMAP_URL))
    if not slugs:
        raise RuntimeError("sitemap 里没有 marketplace slug")

    rows: list[dict[str, Any]] = []
    errors: list[str] = []

    def load(slug: str) -> dict[str, Any]:
        return parse_raw_md(slug, fetch_raw(slug))

    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = {pool.submit(load, slug): slug for slug in slugs}
        parsed: dict[str, dict[str, Any]] = {}
        for future in as_completed(futures):
            slug = futures[future]
            try:
                parsed[slug] = future.result()
            except Exception as error:  # noqa: BLE001 — 导出时记录失败 slug，不中断其余
                errors.append(f"{slug}: {error}")

    if errors and len(parsed) < len(slugs) * 0.9:
        raise RuntimeError("太多接口文档拉失败：\n" + "\n".join(errors[:12]))

    for index, slug in enumerate(slugs, start=1):
        if slug not in parsed:
            continue
        row = parsed[slug]
        row["index"] = index
        rows.append(row)

    meta = {
        "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        "sources": {
            "sitemap": SITEMAP_URL,
            "raw_docs": RAW_DOC_TMPL,
            "llms": LLMS_URL,
        },
        "api_count": len(rows),
        "added_since_2026_07": [
            slug
            for slug in (
                "douyin-works",
                "express-pro",
                "ai-chat",
                "ocr-qrcode",
                "douyin-search",
                "user-info",
                "football",
                "contact-parse",
                "idcard-face-3c",
                "basketball",
                "drug-insert",
                "ocr-text-box",
                "ai-video",
                "tender-files",
                "company-contacts",
                "tender-search",
                "tender-number",
                "tender-rewrite",
                "tender-extract",
                "planned-search",
                "tender-contract",
                "tender-source",
                "tender-site",
                "tender-search-ai",
                "planned-files",
                "tender-company",
                "tender-detail-ai",
                "tender-classify",
                "tender-category",
                "company-customers",
                "company-stats",
                "history-today",
                "tender-detail",
                "tender-structure",
                "planned-detail",
                "company-suppliers",
            )
            if slug in parsed
        ],
        "fetch_errors": errors,
    }
    return rows, meta
