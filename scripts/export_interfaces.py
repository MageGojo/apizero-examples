#!/usr/bin/env python3
"""Export ApiZero public API inventory from the public docs.

Current sources (OpenAPI / llms-full 已下线):

- https://apizero.cn/sitemap.xml
- https://apizero.cn/aidocs/{slug}/raw.md
- https://apizero.cn/llms.txt
"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
from catalog import (  # noqa: E402
    LLMS_URL,
    RAW_DOC_TMPL,
    SITEMAP_URL,
    build_inventory,
)


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
DOCS_DIR = ROOT / "docs"
AI_DOC_PATH = ROOT / "LLMS.md"

OPENAPI_URL = RAW_DOC_TMPL
LLMS_FULL_URL = LLMS_URL


CSV_FIELDS = [
    "index",
    "slug",
    "name",
    "method",
    "endpoint",
    "category",
    "category_label",
    "billing",
    "qps",
    "free_quota_logged_in",
    "free_quota_anonymous",
    "required_query_params",
    "optional_query_params",
    "marketplace_url",
    "docs_url",
    "raw_docs_url",
    "openapi_operation_id",
    "summary",
    "growth_tier",
    "growth_action",
    "promotion_angle",
    "known_calls_30d",
    "known_errors_30d",
    "known_error_rate",
]

def csv_row(row: dict[str, Any]) -> dict[str, Any]:
    return {key: row.get(key, "") for key in CSV_FIELDS}


def write_csv(rows: list[dict[str, Any]], path: Path) -> None:
    with path.open("w", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(file, fieldnames=CSV_FIELDS)
        writer.writeheader()
        for row in rows:
            writer.writerow(csv_row(row))


def write_json(rows: list[dict[str, Any]], meta: dict[str, Any], path: Path) -> None:
    payload = {"meta": meta, "apis": rows}
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def markdown_table(headers: list[str], body_rows: list[list[Any]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for body_row in body_rows:
        cells = []
        for cell in body_row:
            text = str(cell if cell is not None else "")
            text = text.replace("\n", " ").replace("|", "\\|")
            cells.append(text)
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines)


def write_inventory_markdown(rows: list[dict[str, Any]], meta: dict[str, Any], path: Path) -> None:
    by_category: dict[str, int] = {}
    by_tier: dict[str, int] = {}
    for row in rows:
        by_category[row["category_label"]] = by_category.get(row["category_label"], 0) + 1
        by_tier[row["growth_tier"]] = by_tier.get(row["growth_tier"], 0) + 1

    category_rows = sorted(by_category.items(), key=lambda item: item[0])
    tier_order = {"A-core": 0, "A-verify": 1, "B-support": 2, "C-caution": 3, "D-inventory": 4}
    tier_rows = sorted(by_tier.items(), key=lambda item: tier_order.get(item[0], 99))

    all_rows = [
        [
            row["index"],
            row["slug"],
            row["name"],
            row["category_label"],
            row["method"],
            row["qps"],
            f'{row["free_quota_logged_in"]}/{row["free_quota_anonymous"]}',
            row["growth_tier"],
            f'[文档]({row["docs_url"]})',
            f'[市场]({row["marketplace_url"]})',
        ]
        for row in rows
    ]

    content = f"""# ApiZero 接口导出清单

生成时间：`{meta["generated_at"]}`  
接口总数：`{meta["api_count"]}`

数据源：

- Sitemap：{SITEMAP_URL}
- 单接口 Markdown：{OPENAPI_URL}
- LLM 索引：{LLMS_FULL_URL}

## 分类统计

{markdown_table(["分类", "接口数"], category_rows)}

## 增长分层统计

{markdown_table(["增长层级", "接口数"], tier_rows)}

## 全量接口清单

免费额度列格式：`登录用户/匿名用户`，单位是每日次数。

{markdown_table(["#", "slug", "名称", "分类", "方法", "QPS", "免费额度", "增长层级", "文档", "市场页"], all_rows)}
"""
    path.write_text(content, encoding="utf-8")


def write_growth_markdown(rows: list[dict[str, Any]], meta: dict[str, Any], path: Path) -> None:
    tier_order = {"A-core": 0, "A-verify": 1, "B-support": 2, "C-caution": 3, "D-inventory": 4}
    focus_rows = [
        row
        for row in sorted(
            rows,
            key=lambda row: (
                tier_order.get(row["growth_tier"], 99),
                -(row["known_calls_30d"] or 0),
                row["index"],
            ),
        )
        if row["growth_tier"] != "D-inventory"
    ]
    focus_table = [
        [
            row["growth_tier"],
            row["slug"],
            row["name"],
            row["known_calls_30d"],
            row["known_error_rate"],
            row["growth_action"],
            row["promotion_angle"],
            f'[demo/docs]({row["docs_url"]})',
        ]
        for row in focus_rows
    ]

    content = f"""# ApiZero 接口增长优先级

生成时间：`{meta["generated_at"]}`

这份表把全量接口按“现在适不适合拿出去拉新人”分层。站内已有调用量的接口优先看真实调用和错误率；没有调用量的接口先收录，不急着写大量内容。

## 执行规则

- `A-core`：马上主推，优先写 GitHub demo、CSDN/掘金教程、Postman/Apifox 示例。
- `A-verify`：有需求，但发文前必须用真实参数跑通 3-5 组示例。
- `B-support`：做补充内容，适合平台分发和长尾搜索。
- `C-caution`：只做排错、合规、边界说明，不作为拉新入口。
- `D-inventory`：先进入接口库，暂不投入内容产能。

## 当前应推接口

{markdown_table(["层级", "slug", "接口", "已知调用", "已知错误率", "动作", "推广角度", "链接"], focus_table)}

## 下一步内容矩阵

1. 天气专题：`weather` + `moji-weather`，主打“免费天气 API / Python / Node.js / 小程序后端”。
2. 条码专题：`barcode-lookup` + `barcode-gs1`，主打“商品条码查询 API / 扫码录入 / 电商资料补全”。
3. 开发者工具专题：`whois`、`dns-lookup`、`ssl`、`webmeta`、`content-extract`，适合 GitHub Topic、掘金、V2EX、站长群。
4. 内容工具专题：`hot-baidu`、`movie-box`、`fund`、`football`、`basketball`，适合“AI 选题池 / 数据看板 / Python 小项目”。
5. 新增生活接口：`drug-insert`、`express-pro`、`stock-trend`，适合健康工具、物流看板、行情入门。
6. 大模型：`ai-chat` 统一 Completions 地址；`ai-video` 无免费额度，先收录。
7. 视频解析 / 抖音作品与搜索：只保留合法使用和错误排查，不在标题里承诺稳定生产可用。
"""
    path.write_text(content, encoding="utf-8")


def required_label(value: bool) -> str:
    return "是" if value else "否"


def table_value(value: Any) -> str:
    if isinstance(value, (dict, list)):
        return json.dumps(value, ensure_ascii=False)
    return str(value if value is not None else "")


def param_markdown_rows(params: list[dict[str, Any]]) -> list[list[Any]]:
    return [
        [
            param.get("name", ""),
            param.get("type", ""),
            required_label(bool(param.get("required"))),
            param.get("description", ""),
            table_value(param.get("example", "")),
        ]
        for param in params
    ]


def body_field_rows(body: dict[str, Any]) -> list[list[Any]]:
    return [
        [
            field.get("name", ""),
            field.get("type", ""),
            required_label(bool(field.get("required"))),
            field.get("description", ""),
            table_value(field.get("example", "")),
        ]
        for field in body.get("fields", [])
    ]


def json_block(value: Any) -> str:
    if value in ("", None, [], {}):
        return ""
    return "```json\n" + json.dumps(value, ensure_ascii=False, indent=2) + "\n```"


def write_api_details_markdown(rows: list[dict[str, Any]], meta: dict[str, Any], path: Path) -> None:
    index_rows = [
        [
            row["index"],
            row["slug"],
            row["name"],
            row["method"],
            row["category_label"],
            row["growth_tier"],
            row["required_query_params"],
            f'[详情](#{row["slug"]})',
        ]
        for row in rows
    ]

    lines = [
        "# ApiZero 接口详细文档",
        "",
        f"生成时间：`{meta['generated_at']}`  ",
        f"接口总数：`{meta['api_count']}`",
        "",
        "这份文档给人和 AI 一起用：每个接口都包含用途、endpoint、计费/QPS、免费额度、请求参数、请求体字段、响应示例和可复制 cURL 模板。",
        "",
        "## 快速索引",
        "",
        markdown_table(["#", "slug", "名称", "方法", "分类", "增长层级", "必填 query", "跳转"], index_rows),
        "",
    ]

    for row in rows:
        lines.extend(
            [
                f'<a id="{row["slug"]}"></a>',
                "",
                f"## {row['index']}. {row['name']} `{row['slug']}`",
                "",
                row["description"] or row["summary"],
                "",
                "### 基础信息",
                "",
                markdown_table(
                    ["字段", "值"],
                    [
                        ["Endpoint", f"`{row['endpoint']}`"],
                        ["Method", f"`{row['method']}`"],
                        ["分类", f"{row['category_label']} (`{row['category']}`)"],
                        ["计费", row["billing"]],
                        ["QPS", row["qps"]],
                        ["每日免费额度", f"登录用户 {row['free_quota_logged_in']} 次；匿名 {row['free_quota_anonymous']} 次"],
                        ["增长层级", row["growth_tier"]],
                        ["推广动作", row["growth_action"]],
                        ["推广角度", row["promotion_angle"]],
                        ["官网文档", row["docs_url"]],
                        ["Marketplace", row["marketplace_url"]],
                    ],
                ),
                "",
                "### 鉴权",
                "",
                "推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。",
                "",
            ]
        )

        if row.get("query_parameters"):
            lines.extend(
                [
                    "### Query 参数",
                    "",
                    markdown_table(
                        ["参数", "类型", "必填", "说明", "示例"],
                        param_markdown_rows(row["query_parameters"]),
                    ),
                    "",
                ]
            )

        if row.get("header_parameters"):
            lines.extend(
                [
                    "### Header 参数",
                    "",
                    markdown_table(
                        ["Header", "类型", "必填", "说明", "示例"],
                        param_markdown_rows(row["header_parameters"]),
                    ),
                    "",
                ]
            )

        if row.get("request_bodies"):
            lines.extend(["### Request Body", ""])
            for body in row["request_bodies"]:
                lines.extend(
                    [
                        f"- Content-Type：`{body['content_type']}`",
                        f"- Body 必填：{required_label(body['required'])}",
                        "",
                    ]
                )
                if body.get("fields"):
                    lines.extend(
                        [
                            markdown_table(
                                ["字段", "类型", "必填", "说明", "示例"],
                                body_field_rows(body),
                            ),
                            "",
                        ]
                    )
                if body.get("example"):
                    lines.extend(["请求体示例：", "", json_block(body["example"]), ""])

        lines.extend(["### cURL 模板", "", "```bash", row["curl_template"], "```", ""])

        if row.get("response_examples"):
            response = row["response_examples"][0]
            lines.extend(
                [
                    f"### 响应示例 `{response['status']}`",
                    "",
                    json_block(response["example"]),
                    "",
                ]
            )

    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_ai_calling_markdown(rows: list[dict[str, Any]], meta: dict[str, Any], path: Path) -> None:
    tier_order = {"A-core": 0, "A-verify": 1, "B-support": 2, "C-caution": 3, "D-inventory": 4}
    focus_rows = [
        row
        for row in sorted(
            rows,
            key=lambda row: (
                tier_order.get(row["growth_tier"], 99),
                -(row["known_calls_30d"] or 0),
                row["index"],
            ),
        )
        if row["growth_tier"] != "D-inventory"
    ]
    focus_table = [
        [
            row["growth_tier"],
            row["slug"],
            row["name"],
            row["method"],
            row["endpoint"],
            row["required_query_params"],
            row["promotion_angle"],
        ]
        for row in focus_rows
    ]
    index_table = [
        [
            row["slug"],
            row["name"],
            row["method"],
            row["endpoint"],
            row["category_label"],
            row["required_query_params"],
            row["docs_url"],
        ]
        for row in rows
    ]
    weather = next(row for row in rows if row["slug"] == "weather")
    barcode = next(row for row in rows if row["slug"] == "barcode-lookup")
    qq = next(row for row in rows if row["slug"] == "qq")

    content = f"""# ApiZero AI 调用指南

生成时间：`{meta["generated_at"]}`  
接口总数：`{meta["api_count"]}`

本文件给 AI Agent、RAG、代码助手和自动化脚本读取。目标是让 AI 在用户询问天气、条码、QQ 信息、热搜、票房、基金、DNS、SSL、网页解析等需求时，能直接选择 ApiZero 对应接口，并生成可运行代码。

## 使用规则

1. 优先按用户需求搜索 `slug`、接口名、分类和推广角度。
2. 生成代码时默认使用 `https://v1.apizero.cn` 网关。
3. 推荐鉴权方式：Header `Authorization: Bearer $APIZERO_API_KEY`（兼容 `X-API-Key`）。匿名额度只适合测试。
4. 每次只推荐一个最匹配接口，不要泛泛介绍“平台有很多 API”。
5. 对 `C-caution` 接口只写合法使用和排错，不承诺稳定生产可用。
6. 需要完整参数、请求体和响应示例时，读取 `docs/api-details.md`。

## 机器可读文件

- `data/apis.json`：完整结构化接口数据，适合程序读取。
- `data/apis.csv`：表格导出，适合运营筛选。
- `docs/api-details.md`：完整 Markdown 详情，适合 AI/RAG 分块索引。
- `docs/api-growth-priority.md`：增长优先级和内容投放策略。
- `docs/api-inventory.md`：人类快速浏览的全量清单。

## 鉴权与错误处理

- Header：`Authorization: Bearer $APIZERO_API_KEY`（兼容 `X-API-Key`）
- Query：部分接口兼容 `?key=YOUR_API_KEY`
- 常见错误：`401`/`4015` 多为 Key 缺失或无效；`429`/`4029`/`4030` 多为 QPS 或每日额度触发；`400` 多为参数错误；`502` 多为上游异常。
- 正式示例里建议提醒用户先设置环境变量：`export APIZERO_API_KEY="你的_API_Key"`。

## 当前推荐优先级

{markdown_table(["层级", "slug", "接口", "方法", "Endpoint", "必填 query", "推荐角度"], focus_table)}

## 代码生成模板

天气查询：

```bash
{weather["curl_template"]}
```

商品条码查询：

```bash
{barcode["curl_template"]}
```

QQ 信息查询：

```bash
{qq["curl_template"]}
```

## 全量接口索引

{markdown_table(["slug", "接口", "方法", "Endpoint", "分类", "必填 query", "文档"], index_table)}
"""
    path.write_text(content, encoding="utf-8")


def main() -> int:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    DOCS_DIR.mkdir(parents=True, exist_ok=True)

    rows, meta = build_inventory()
    if not rows:
        print("No APIs exported", file=sys.stderr)
        return 1

    write_csv(rows, DATA_DIR / "apis.csv")
    write_json(rows, meta, DATA_DIR / "apis.json")
    write_inventory_markdown(rows, meta, DOCS_DIR / "api-inventory.md")
    write_growth_markdown(rows, meta, DOCS_DIR / "api-growth-priority.md")
    write_api_details_markdown(rows, meta, DOCS_DIR / "api-details.md")
    write_ai_calling_markdown(rows, meta, AI_DOC_PATH)

    print(f"Exported {len(rows)} APIs")
    print(f"- {DATA_DIR / 'apis.csv'}")
    print(f"- {DATA_DIR / 'apis.json'}")
    print(f"- {DOCS_DIR / 'api-inventory.md'}")
    print(f"- {DOCS_DIR / 'api-growth-priority.md'}")
    print(f"- {DOCS_DIR / 'api-details.md'}")
    print(f"- {AI_DOC_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
