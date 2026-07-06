"""Video metadata parsing debug example.

This endpoint is intentionally not the primary growth entry because invalid,
expired, private, or unsupported share links can fail. Use it for legal content
metadata parsing and debugging only.

Docs: https://apizero.cn/aidocs/video-parse
"""

import os
import requests


API_URL = "https://v1.apizero.cn/api/video-parse"


def main() -> None:
    share_url = os.getenv("VIDEO_SHARE_URL")
    if not share_url:
        raise SystemExit("Set VIDEO_SHARE_URL to a legal, publicly accessible share URL first.")

    params = {
        "url": share_url,
        "flat": 1,
    }
    api_key = os.getenv("APIZERO_API_KEY")
    if api_key:
        params["key"] = api_key

    response = requests.get(API_URL, params=params, timeout=20)
    if response.status_code == 429:
        raise SystemExit("HTTP 429: 请求过快或匿名额度已用完，稍后重试或设置 APIZERO_API_KEY。")
    if not response.ok:
        raise SystemExit(f"HTTP {response.status_code}: {response.text[:300]}")
    payload = response.json()

    print("status:", payload.get("code"), payload.get("msg"))
    print("data:", payload.get("data"))


if __name__ == "__main__":
    main()
