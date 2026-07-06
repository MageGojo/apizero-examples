# 实时电影票房API做看板：Python 获取今日票房榜

想做一个影视数据看板，可以先从实时电影票房 API 开始。
接口返回当日票房榜数据，适合练习数据展示、公众号素材和小程序榜单。
下面是最小 Python 示例。

## Python 示例

```python
import os
import requests

params = {}
api_key = os.getenv("APIZERO_API_KEY")
if api_key:
    params["key"] = api_key

resp = requests.get("https://v1.apizero.cn/api/movie-box", params=params, timeout=15)
resp.raise_for_status()
payload = resp.json()

print(payload.get("code"), payload.get("msg"))
print(payload.get("data"))
```

## 看板可以展示什么

- 电影名称。
- 实时票房。
- 累计票房。
- 票房占比。
- 排片占比。

## 扩展方向

- 保存为 CSV。
- 用 ECharts 做榜单图。
- 每小时定时刷新。

GitHub 示例：https://github.com/MageGojo/apizero-examples/tree/main/examples/content  
接口文档：https://apizero.cn/aidocs/movie-box

