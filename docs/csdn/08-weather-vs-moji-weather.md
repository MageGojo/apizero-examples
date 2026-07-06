# 墨迹天气和彩云天气API对比：哪个适合小程序/网站天气模块

如果只是快速做天气模块，优先用彩云天气接口。
如果你需要更完整的实况、AQI、生活指数、历史天气，可以测试墨迹天气接口。
下面用同一个城市做对比。

## 彩云天气

```python
import requests

resp = requests.get(
    "https://v1.apizero.cn/api/weather",
    params={"city": "北京", "type": "weather", "days": 3},
    timeout=15,
)
print(resp.json())
```

## 墨迹天气

```python
import requests

resp = requests.get(
    "https://v1.apizero.cn/api/moji-weather",
    params={"city": "北京"},
    timeout=15,
)
print(resp.json())
```

## 怎么选

- 快速上线：选彩云天气。
- 字段更丰富：测试墨迹天气。
- 前端只展示一句天气摘要：优先彩云天气。
- 做生活指数/空气质量页：测试墨迹天气。

GitHub 示例：https://github.com/MageGojo/apizero-examples/tree/main/examples/weather  
接口文档：https://apizero.cn/aidocs/moji-weather

