# 小程序天气接口怎么做？Node.js 后端调用免费天气API示例

小程序前端不适合直接暴露第三方 Key，常见做法是用自己的 Node.js 后端转发天气接口。
这个示例用 Node.js 18 自带 `fetch` 调用天气 API。
适合做小程序首页天气、城市天气卡片、出行提醒模块。

## Node.js 示例

```javascript
const city = "北京";

const params = new URLSearchParams({
  type: "weather",
  city,
  days: "3",
  hours: "24",
});

if (process.env.APIZERO_API_KEY) {
  params.set("key", process.env.APIZERO_API_KEY);
}

const res = await fetch(`https://v1.apizero.cn/api/weather?${params}`);
if (!res.ok) throw new Error(`HTTP ${res.status}`);

const data = await res.json();
console.log(data.data?.summary);
```

## 小程序后端建议返回什么

前端一般不需要完整响应，可以只返回：

- 城市名。
- 天气现象。
- 当前温度。
- 体感温度。
- AQI。
- 未来 3 天预报。

这样前端展示更简单，也能减少传输数据。

## 常见问题

- 不设置 `APIZERO_API_KEY` 可以先用匿名额度测试。
- 生产环境建议在服务器环境变量里设置 Key。
- 城市名查不到时，可以改用经纬度参数。

GitHub 示例：https://github.com/MageGojo/apizero-examples/tree/main/examples/weather  
接口文档：https://apizero.cn/aidocs/weather

