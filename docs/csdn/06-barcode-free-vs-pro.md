# 商品条码查询免费版和PRO版有什么区别？适合库存、电商、扫码录入

条码查询一般有两类需求：快速补全商品信息，或者做官方注册信息核验。
免费版更适合展示商品名、品牌、规格、图片。
PRO 版更适合看厂商注册主体、产品登记信息、官方数据来源。

## 免费版适合

- 库存录入。
- 商品展示。
- 个人记账。
- 扫码识物。

接口：`https://v1.apizero.cn/api/barcode-lookup`

## PRO 版适合

- 合规核验。
- 溯源审核。
- 电商上架审核。
- 供应链资料校验。

接口：`https://v1.apizero.cn/api/barcode-gs1`

## Python PRO 示例

```python
import os
import requests

params = {"code": "6907992700199"}

api_key = os.getenv("APIZERO_API_KEY")
if api_key:
    params["key"] = api_key

resp = requests.get("https://v1.apizero.cn/api/barcode-gs1", params=params, timeout=15)
resp.raise_for_status()
data = resp.json()

product = data.get("data", {})
print(product.get("registered"))
print(product.get("name"))
print(product.get("manufacturer"))
print(product.get("category"))
```

## 怎么选

只是扫码展示商品，用免费版。
需要官方注册主体和合规字段，用 PRO 版。

GitHub 示例：https://github.com/MageGojo/apizero-examples/tree/main/examples/barcode  
接口文档：https://apizero.cn/aidocs/barcode-gs1

