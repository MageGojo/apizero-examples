// Query ApiZero Baidu hot search API with Node.js 18+.
// Docs: https://apizero.cn/aidocs/hot-baidu

const params = new URLSearchParams({
  tab: "realtime",
});

if (process.env.APIZERO_API_KEY) {
  params.set("key", process.env.APIZERO_API_KEY);
}

const url = `https://v1.apizero.cn/api/hot-baidu?${params}`;
const res = await fetch(url);
if (res.status === 429) {
  throw new Error("HTTP 429: 请求过快或匿名额度已用完，稍后重试或设置 APIZERO_API_KEY。");
}
if (!res.ok) throw new Error(`HTTP ${res.status}`);

const payload = await res.json();
console.log("status:", payload.code, payload.msg);
for (const item of (payload.data ?? []).slice(0, 5)) {
  console.log(item.rank, item.title, item.hot_index);
}
