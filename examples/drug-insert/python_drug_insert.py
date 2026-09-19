"""Query ApiZero drug insert API with Python.

Docs: https://apizero.cn/aidocs/drug-insert
"""

import os
import sys

import requests


API_URL = "https://v1.apizero.cn/api/drug-insert"


def headers() -> dict[str, str]:
    api_key = os.getenv("APIZERO_API_KEY")
    if not api_key:
        return {}
    return {"Authorization": f"Bearer {api_key}"}


def search(name: str) -> dict:
    response = requests.get(API_URL, params={"name": name}, headers=headers(), timeout=15)
    if response.status_code == 429:
        raise SystemExit("HTTP 429: 请求过快或额度已用完，稍后重试或设置 APIZERO_API_KEY。")
    if not response.ok:
        raise SystemExit(f"HTTP {response.status_code}: {response.text[:300]}")
    payload = response.json()
    if payload.get("code") != 0:
        raise SystemExit(f"业务错误 {payload.get('code')}: {payload.get('msg')}")
    return payload.get("data") or {}


def detail(insert_id: str) -> dict:
    response = requests.get(API_URL, params={"id": insert_id}, headers=headers(), timeout=15)
    if not response.ok:
        raise SystemExit(f"HTTP {response.status_code}: {response.text[:300]}")
    payload = response.json()
    if payload.get("code") != 0:
        raise SystemExit(f"业务错误 {payload.get('code')}: {payload.get('msg')}")
    return payload.get("data") or {}


def main() -> None:
    keyword = sys.argv[1] if len(sys.argv) > 1 else "阿莫西林"
    data = search(keyword)
    print("search:", data.get("query"), "found=", data.get("found"), "total=", data.get("total"))
    items = data.get("list") or []
    if not items:
        print("未命中说明书")
        return
    first = items[0]
    print("first:", first.get("id"), first.get("name"), first.get("approval_no"))
    full = detail(first["id"])
    print("detail:", full.get("name"), "sections=", len(full.get("sections") or []))
    for section in (full.get("sections") or [])[:3]:
        content = (section.get("content") or "").replace("\n", " ")
        print(f"- {section.get('name')}: {content[:80]}")


if __name__ == "__main__":
    main()
