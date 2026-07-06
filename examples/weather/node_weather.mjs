// Query ApiZero weather API with Node.js 18+.
// Docs: https://apizero.cn/aidocs/weather

const params = new URLSearchParams({
  type: "weather",
  city: "北京",
  days: "3",
  hours: "24",
});

if (process.env.APIZERO_API_KEY) {
  params.set("key", process.env.APIZERO_API_KEY);
}

const url = `https://v1.apizero.cn/api/weather?${params}`;
const res = await fetch(url);
if (res.status === 429) {
  throw new Error("HTTP 429: 请求过快或匿名额度已用完，稍后重试或设置 APIZERO_API_KEY。");
}
if (!res.ok) throw new Error(`HTTP ${res.status}`);

const payload = await res.json();
console.log("status:", payload.code, payload.msg);
console.log("summary:", payload.data?.summary);
console.log("location:", payload.data?.location);
