"""Query ApiZero official GS1 barcode API with Python.

Use this PRO endpoint when you need registered manufacturer and official data.
Docs: https://apizero.cn/aidocs/barcode-gs1
"""

import os
import requests


API_URL = "https://v1.apizero.cn/api/barcode-gs1"


def main() -> None:
    params = {"code": "6907992700199"}
    api_key = os.getenv("APIZERO_API_KEY")
    if api_key:
        params["key"] = api_key

    response = requests.get(API_URL, params=params, timeout=15)
    if response.status_code == 429:
        raise SystemExit("HTTP 429: 请求过快或匿名额度已用完，稍后重试或设置 APIZERO_API_KEY。")
    if not response.ok:
        raise SystemExit(f"HTTP {response.status_code}: {response.text[:300]}")
    payload = response.json()

    print("status:", payload.get("code"), payload.get("msg"))
    product = payload.get("data") or {}
    print("registered:", product.get("registered"))
    print("name:", product.get("name"))
    print("manufacturer:", product.get("manufacturer"))
    print("category:", product.get("category"))


if __name__ == "__main__":
    main()
