// Query ApiZero QQ info API with Node.js 18+.
// Docs: https://apizero.cn/aidocs/qq

const params = new URLSearchParams({
  qq: "88888888",
});

if (process.env.APIZERO_API_KEY) {
  params.set("key", process.env.APIZERO_API_KEY);
}

const url = `https://v1.apizero.cn/api/qq?${params}`;
const res = await fetch(url);
if (res.status === 429) {
  throw new Error("HTTP 429: 请求过快或匿名额度已用完，稍后重试或设置 APIZERO_API_KEY。");
}
if (!res.ok) throw new Error(`HTTP ${res.status}`);

const payload = await res.json();
const info = payload.data ?? {};
console.log("status:", payload.code, payload.msg);
console.log("qq:", info.qq);
console.log("name:", info.name);
console.log("mail:", info.mail);
console.log("avatar:", info.avatars?.s100);
