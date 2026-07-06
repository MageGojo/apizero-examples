# 基金估值API：Python 查询基金实时估值示例

如果你想做一个基金估值提醒脚本，可以用基金估值 API。
输入基金代码，返回实时估值、涨跌幅等信息。
下面示例使用 Python 查询基金代码 `110022`。

```python
import os
import requests

params = {
    "action": "estimate",
    "code": "110022",
}

api_key = os.getenv("APIZERO_API_KEY")
if api_key:
    params["key"] = api_key

resp = requests.get("https://v1.apizero.cn/api/fund", params=params, timeout=15)
resp.raise_for_status()
print(resp.json())
```

## 可扩展玩法

- 每天定时推送关注基金估值。
- 做基金估值看板。
- 接入企业微信/飞书机器人提醒。

GitHub 示例：https://github.com/MageGojo/apizero-examples/tree/main/examples/content  
接口文档：https://apizero.cn/aidocs/fund

