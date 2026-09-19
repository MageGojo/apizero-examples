"""Query ApiZero A-share realtime quote API with Python.

Docs: https://apizero.cn/aidocs/stock-trend
"""

import json
import os
import sys

import requests


API_URL = "https://v1.apizero.cn/api/stock-trend"


def main() -> None:
    code = sys.argv[1] if len(sys.argv) > 1 else "600519"
    headers = {}
    api_key = os.getenv("APIZERO_API_KEY")
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"

    response = requests.post(
        API_URL,
        headers=headers,
        json={"code": code, "type": "simple", "limit": 5},
        timeout=15,
    )
    if response.status_code == 429:
        raise SystemExit("HTTP 429: 请求过快或额度已用完，稍后重试或设置 APIZERO_API_KEY。")
    if not response.ok:
        raise SystemExit(f"HTTP {response.status_code}: {response.text[:300]}")
    payload = response.json()
    if payload.get("code") != 0:
        raise SystemExit(f"业务错误 {payload.get('code')}: {payload.get('msg')}")

    data = payload.get("data") or {}
    stock = data.get("stock") or {}
    quote = data.get("quote") or {}
    print("stock:", stock.get("code"), stock.get("name"), stock.get("trade_status"))
    print("quote:", json.dumps(quote, ensure_ascii=False))


if __name__ == "__main__":
    main()
