# Python 获取百度热搜并保存 CSV：免费热搜API示例

做公众号选题、热点看板、AI 写作提示时，可以先把热搜榜保存成 CSV。
这个示例调用百度热搜 API，取前 30 条并写入本地文件。
适合做每日选题池或数据分析练习。

## Python 示例

```python
import csv
import os
import requests

params = {"tab": "realtime"}
api_key = os.getenv("APIZERO_API_KEY")
if api_key:
    params["key"] = api_key

resp = requests.get("https://v1.apizero.cn/api/hot-baidu", params=params, timeout=15)
resp.raise_for_status()
payload = resp.json()

rows = payload.get("data", [])[:30]
with open("baidu_hot.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.DictWriter(f, fieldnames=["rank", "title", "hot_index", "link"])
    writer.writeheader()
    for item in rows:
        writer.writerow({
            "rank": item.get("rank"),
            "title": item.get("title"),
            "hot_index": item.get("hot_index"),
            "link": item.get("link"),
        })

print("saved baidu_hot.csv")
```

## 可以怎么用

- 每天定时生成热点选题表。
- 给 AI 写作工具提供实时标题。
- 做简单的数据大屏。

GitHub 示例：https://github.com/MageGojo/apizero-examples/tree/main/examples/content  
接口文档：https://apizero.cn/aidocs/hot-baidu

