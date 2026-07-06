# Node.js 商品条码查询API封装：扫码后返回商品名称和图片

做扫码录入时，前端通常只拿到一串条形码。
后端可以调用商品条码查询 API，把条码转换成商品名称、品牌、规格和图片。
这个示例用 Node.js 18 直接调用，不需要额外依赖。

## Node.js 示例

```javascript
const barcode = "6921168509256";

const params = new URLSearchParams({ barcode });
if (process.env.APIZERO_API_KEY) {
  params.set("key", process.env.APIZERO_API_KEY);
}

const res = await fetch(`https://v1.apizero.cn/api/barcode-lookup?${params}`);
if (!res.ok) throw new Error(`HTTP ${res.status}`);

const payload = await res.json();
const product = payload.data ?? {};

console.log({
  barcode: product.barcode,
  found: product.found,
  name: product.name,
  brand: product.brand,
  spec: product.spec,
  image: product.image,
});
```

## 业务里怎么处理

- `found=true`：自动填充商品名称、品牌、规格、图片。
- `found=false`：让用户手动录入，并把条码保存到待补全列表。
- 接口返回的图片 URL 可以直接给前端 `<img>` 展示。

GitHub 示例：https://github.com/MageGojo/apizero-examples/tree/main/examples/barcode  
接口文档：https://apizero.cn/aidocs/barcode-lookup

