// Query ApiZero barcode lookup API with Node.js 18+.
// Docs: https://apizero.cn/aidocs/barcode-lookup

const params = new URLSearchParams({
  barcode: "6921168509256",
});

if (process.env.APIZERO_API_KEY) {
  params.set("key", process.env.APIZERO_API_KEY);
}

const url = `https://v1.apizero.cn/api/barcode-lookup?${params}`;
const res = await fetch(url);
if (res.status === 429) {
  throw new Error("HTTP 429: 请求过快或匿名额度已用完，稍后重试或设置 APIZERO_API_KEY。");
}
if (!res.ok) throw new Error(`HTTP ${res.status}`);

const payload = await res.json();
const product = payload.data ?? {};
console.log("status:", payload.code, payload.msg);
console.log("name:", product.name);
console.log("brand:", product.brand);
console.log("spec:", product.spec);
console.log("image:", product.image);
