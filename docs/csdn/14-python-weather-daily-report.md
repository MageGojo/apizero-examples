# Python 每天自动查询天气：免费天气API生成出行提醒

想每天早上自动生成天气提醒，可以用 Python 调用天气 API。
这个示例查询北京天气，并根据温度、AQI、预警数量生成简单提示。
后续可以接企业微信、飞书、邮件或定时任务。

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
payload = resp.json()

summary = payload.get("data", {}).get("summary", {})
city = summary.get("city")
skycon = summary.get("skycon")
temperature = summary.get("temperature")
aqi = summary.get("air_quality", {}).get("aqi")
alert_count = summary.get("alert_count", 0)

print(f"{city}今天{skycon}，当前{temperature}℃，AQI {aqi}。")
if alert_count:
    print(f"今天有 {alert_count} 条天气预警，出门前注意查看。")
```

## 适合扩展

- macOS/Linux 用 crontab 每天 8 点运行。
- 企业微信机器人推送天气摘要。
- 家庭看板展示当天温度和空气质量。

GitHub 示例：https://github.com/MageGojo/apizero-examples/tree/main/examples/weather  
接口文档：https://apizero.cn/aidocs/weather

