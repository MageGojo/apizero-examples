# Python 免费天气API接入教程：支持城市名查询和未来天气

想在 Python 脚本里查询北京、上海、广州这类城市天气，可以直接调用天气 API。
这个示例不用先申请高德/百度地图 Key，匿名额度就能测试。
复制下面代码，安装 `requests` 后即可运行。

## 适合什么场景

- 个人脚本每天自动推送天气。
- 小程序/网站后端展示城市天气。
- AI 助手根据天气生成出行提醒。

## Python 示例

```python
import os
import requests

params = {
    "type": "weather",
    "city": "北京",
    "days": 3,
    "hours": 24,
}

api_key = os.getenv("APIZERO_API_KEY")
if api_key:
    params["key"] = api_key

resp = requests.get("https://v1.apizero.cn/api/weather", params=params, timeout=15)
resp.raise_for_status()
data = resp.json()

print(data["code"], data["msg"])
print(data.get("data", {}).get("summary"))
```

## 参数说明

- `city`：城市名，比如 `北京`、`上海`、`杭州`。
- `type`：查询类型，常用 `weather` 一次返回综合天气。
- `days`：未来几天天气，示例里取 3 天。
- `hours`：小时级天气，示例里取 24 小时。

## 常见错误

- `4015`：匿名额度用完或接口需要 Key。
- `4030`：今日免费额度用完。
- `4000`：参数格式错误，检查城市名或经纬度。

GitHub 示例：https://github.com/MageGojo/apizero-examples/tree/main/examples/weather  
接口文档：https://apizero.cn/aidocs/weather

