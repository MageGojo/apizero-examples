# 百度热搜API：给公众号/AI写作工具做热点选题池

做公众号选题、AI 写作工具、资讯看板时，经常需要实时热点列表。
这个示例调用百度热搜 API，返回排行榜、标题、热度和链接。
适合做热点选题池或后台看板。

## Python 示例

```python
import os
import requests

params = {"tab": "realtime"}

api_key = os.getenv("APIZERO_API_KEY")
if api_key:
    params["key"] = api_key

resp = requests.get("https://v1.apizero.cn/api/hot-baidu", params=params, timeout=15)
resp.raise_for_status()
data = resp.json()

for item in data.get("data", [])[:10]:
    print(item.get("rank"), item.get("title"), item.get("hot_index"))
```

## 可用场景

- 公众号每日选题。
- AI 写作工具热点提示。
- 数据大屏热榜模块。
- 舆情监控的轻量入口。

GitHub 示例：https://github.com/MageGojo/apizero-examples/tree/main/examples/content  
接口文档：https://apizero.cn/aidocs/hot-baidu

