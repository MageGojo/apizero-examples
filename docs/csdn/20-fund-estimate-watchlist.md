# Python 基金估值自选列表：批量查询多个基金实时估值

如果你关注多个基金，可以用 Python 循环调用基金估值 API。
这个示例维护一个自选列表，逐个输出基金估值结果。
适合做命令行看板、定时提醒或个人投资记录。

## Python 示例

```python
import os
import time
import requests

fund_codes = ["110022", "161725", "005827"]
api_key = os.getenv("APIZERO_API_KEY")

for code in fund_codes:
    params = {
        "action": "estimate",
        "code": code,
    }
    if api_key:
        params["key"] = api_key

    resp = requests.get("https://v1.apizero.cn/api/fund", params=params, timeout=15)
    resp.raise_for_status()
    payload = resp.json()

    print(code, payload.get("data"))
    time.sleep(0.5)
```

## 注意

- 批量查询时建议加 `sleep`，避免请求过快。
- 基金代码请替换成自己的自选列表。
- 返回字段可以再格式化成表格或推送消息。

GitHub 示例：https://github.com/MageGojo/apizero-examples/tree/main/examples/content  
接口文档：https://apizero.cn/aidocs/fund

