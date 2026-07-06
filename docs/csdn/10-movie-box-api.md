# 实时电影票房API：做影视数据看板的小项目

想做影视榜单、票房看板或电影公众号素材，可以用实时电影票房 API。
接口返回当日电影票房 Top 数据，适合做小项目和内容后台。
下面是最短 Python 示例。

```python
import os
import requests

params = {}
api_key = os.getenv("APIZERO_API_KEY")
if api_key:
    params["key"] = api_key

resp = requests.get("https://v1.apizero.cn/api/movie-box", params=params, timeout=15)
resp.raise_for_status()
print(resp.json())
```

## 适合什么场景

- 影视公众号数据素材。
- 小程序票房榜。
- 数据可视化练习项目。
- 今日电影市场看板。

GitHub 示例：https://github.com/MageGojo/apizero-examples/tree/main/examples/content  
接口文档：https://apizero.cn/aidocs/movie-box

