"""Query ApiZero QQ info API with Python.

Docs: https://apizero.cn/aidocs/qq
"""

import os
import requests


API_URL = "https://v1.apizero.cn/api/qq"


def main() -> None:
    params = {"qq": "88888888"}
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
    info = payload.get("data") or {}
    print("qq:", info.get("qq"))
    print("name:", info.get("name"))
    print("mail:", info.get("mail"))
    print("avatar:", (info.get("avatars") or {}).get("s100"))


if __name__ == "__main__":
    main()
