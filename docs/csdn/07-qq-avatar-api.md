# QQ头像API：输入 QQ 号返回头像、昵称和邮箱

有些工具需要根据 QQ 号展示头像、昵称或 QQ 邮箱。
这个接口输入 QQ 号，返回昵称、邮箱、空间链接和多尺寸头像 URL。
适合用户资料展示、评论区头像、小工具页面。

## Python 示例

```python
import os
import requests

params = {"qq": "88888888"}

api_key = os.getenv("APIZERO_API_KEY")
if api_key:
    params["key"] = api_key

resp = requests.get("https://v1.apizero.cn/api/qq", params=params, timeout=15)
resp.raise_for_status()
data = resp.json()

info = data.get("data", {})
print(info.get("name"))
print(info.get("mail"))
print(info.get("avatars", {}).get("s100"))
```

## 返回字段

- `name`：QQ 昵称。
- `mail`：QQ 邮箱。
- `qzone`：QQ 空间链接。
- `avatars.s40/s100/s140/s640`：不同尺寸头像。

GitHub 示例：https://github.com/MageGojo/apizero-examples/tree/main/examples/qq-info  
接口文档：https://apizero.cn/aidocs/qq

