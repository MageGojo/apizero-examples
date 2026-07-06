# 商品条码查询API：扫码获取商品名称、品牌、规格、图片

做库存录入、电商资料补全、扫码识物时，最麻烦的是条码转商品信息。
这个示例输入商品条形码，返回商品名称、品牌、规格和图片 URL。
复制代码即可在 Python 中测试。

## Python 示例

```python
import os
import requests

params = {"barcode": "6921168509256"}

api_key = os.getenv("APIZERO_API_KEY")
if api_key:
    params["key"] = api_key

resp = requests.get("https://v1.apizero.cn/api/barcode-lookup", params=params, timeout=15)
resp.raise_for_status()
data = resp.json()

product = data.get("data", {})
print(product.get("name"))
print(product.get("brand"))
print(product.get("spec"))
print(product.get("image"))
```

## 适合什么场景

- 扫码录入商品资料。
- 小卖部/仓库库存系统。
- 记账 App 自动识别商品。
- 营销活动核销商品条码。

## 注意

冷门商品或新上市商品可能返回 `found=false`，这种情况要在业务里做兜底。

GitHub 示例：https://github.com/MageGojo/apizero-examples/tree/main/examples/barcode  
接口文档：https://apizero.cn/aidocs/barcode-lookup

