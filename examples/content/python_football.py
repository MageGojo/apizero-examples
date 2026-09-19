"""Query ApiZero football fixtures API with Python.

Docs: https://apizero.cn/aidocs/football
"""

import os

import requests


API_URL = "https://v1.apizero.cn/api/football"


def main() -> None:
    headers = {}
    api_key = os.getenv("APIZERO_API_KEY")
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"

    response = requests.post(API_URL, headers=headers, json={}, timeout=15)
    if response.status_code == 429:
        raise SystemExit("HTTP 429: 请求过快或额度已用完，稍后重试或设置 APIZERO_API_KEY。")
    if not response.ok:
        raise SystemExit(f"HTTP {response.status_code}: {response.text[:300]}")
    payload = response.json()
    if payload.get("code") != 0:
        raise SystemExit(f"业务错误 {payload.get('code')}: {payload.get('msg')}")

    data = payload.get("data") or {}
    summary = data.get("summary") or {}
    matches = data.get("matches") or []
    print("status:", payload.get("code"), payload.get("msg"), "date=", summary.get("date"), "count=", summary.get("count"))
    for item in matches[:8]:
        home = ((item.get("home") or {}).get("name") if isinstance(item.get("home"), dict) else item.get("home")) or item.get("home_name")
        away = ((item.get("away") or {}).get("name") if isinstance(item.get("away"), dict) else item.get("away")) or item.get("away_name")
        print("-", item.get("league") or item.get("league_name"), home, "vs", away, item.get("status") or item.get("state"))


if __name__ == "__main__":
    main()
