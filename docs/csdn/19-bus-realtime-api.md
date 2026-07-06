# 实时公交到站API怎么用？查询站点公交预计到站时间

如果你在做生活服务小程序、通勤助手或校园公交工具，可以接实时公交到站 API。
输入城市和站点名后，接口会返回线路、方向、预计到站信息。
下面是 Python 调用示例。

## Python 示例

```python
import os
import requests

payload = {
    "city": "北京",
    "station": "中关村",
}

headers = {"Content-Type": "application/json"}
api_key = os.getenv("APIZERO_API_KEY")
if api_key:
    headers["X-Api-Key"] = api_key

resp = requests.post(
    "https://v1.apizero.cn/api/bus-realtime",
    json=payload,
    headers=headers,
    timeout=15,
)
resp.raise_for_status()
print(resp.json())
```

## 适合什么场景

- 通勤到站提醒。
- 小程序站点查询。
- 校园/园区出行工具。
- 地图侧边栏公交信息补充。

GitHub 示例：https://github.com/MageGojo/apizero-examples/tree/main/examples/content  
接口文档：https://apizero.cn/aidocs/bus-realtime

