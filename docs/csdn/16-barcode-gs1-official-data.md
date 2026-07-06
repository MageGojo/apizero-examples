# 商品条码官方数据怎么查？GS1 商品条码查询PRO接口示例

普通条码查询适合展示商品信息，官方注册数据适合做合规核验。
商品条码查询 PRO 会返回厂商注册名称、产品登记信息、分类、规格等字段。
适合电商上架审核、供应链资料校验、商品溯源场景。

## Python 示例

```python
import os
import requests

params = {"code": "6907992700199"}

api_key = os.getenv("APIZERO_API_KEY")
if api_key:
    params["key"] = api_key

resp = requests.get("https://v1.apizero.cn/api/barcode-gs1", params=params, timeout=15)
resp.raise_for_status()
payload = resp.json()

product = payload.get("data", {})
print("是否注册:", product.get("registered"))
print("商品名:", product.get("name"))
print("厂商:", product.get("manufacturer"))
print("分类:", product.get("category"))
print("规格:", product.get("specification"))
```

## 和免费版区别

- 免费版：更适合扫码展示和资料补全。
- PRO 版：更适合官方注册数据、厂商主体、合规审核。

如果只是展示商品卡片，用免费版即可；如果要做审核和溯源，优先测试 PRO 版。

GitHub 示例：https://github.com/MageGojo/apizero-examples/tree/main/examples/barcode  
接口文档：https://apizero.cn/aidocs/barcode-gs1

