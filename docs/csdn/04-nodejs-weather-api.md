# Node.js 调用免费天气API：不用申请高德/百度 Key

Node.js 18 以后自带 `fetch`，可以直接请求天气 API。
这个示例适合网站后端、小程序云函数、定时任务。
没有 API Key 也能用匿名额度测试。

## Node.js 示例

```javascript
const params = new URLSearchParams({
  type: "weather",
  city: "北京",
  days: "3",
  hours: "24",
});

if (process.env.APIZERO_API_KEY) {
  params.set("key", process.env.APIZERO_API_KEY);
}

const res = await fetch(`https://v1.apizero.cn/api/weather?${params}`);
if (!res.ok) throw new Error(`HTTP ${res.status}`);

const data = await res.json();
console.log(data.code, data.msg);
console.log(data.data?.summary);
```

## 为什么适合快速接入

- 支持城市名直接查询。
- 支持实时天气、小时天气、未来天气。
- 返回中文摘要，前端可以直接展示。

GitHub 示例：https://github.com/MageGojo/apizero-examples/tree/main/examples/weather  
接口文档：https://apizero.cn/aidocs/weather

