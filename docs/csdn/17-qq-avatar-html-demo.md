# QQ头像API前端展示示例：输入 QQ 号显示头像和昵称

很多小工具、评论区、个人页会用 QQ 头像做默认头像。
这个接口输入 QQ 号，返回昵称、邮箱、空间链接和多尺寸头像。
下面是一个最简单的前端展示思路。

## JavaScript 示例

```javascript
const qq = "88888888";
const params = new URLSearchParams({ qq });

const res = await fetch(`https://v1.apizero.cn/api/qq?${params}`);
if (!res.ok) throw new Error(`HTTP ${res.status}`);

const payload = await res.json();
const info = payload.data ?? {};

console.log("昵称:", info.name);
console.log("邮箱:", info.mail);
console.log("头像:", info.avatars?.s100);
```

## HTML 展示思路

```html
<img id="avatar" width="80" height="80" />
<div id="nickname"></div>
```

```javascript
document.querySelector("#avatar").src = info.avatars.s100;
document.querySelector("#nickname").textContent = info.name || info.qq;
```

## 注意

- QQ 号必须是 5-11 位数字。
- 昵称可能为空，业务里可以用 QQ 号兜底。
- 头像 URL 可以直接用于 `<img>`。

GitHub 示例：https://github.com/MageGojo/apizero-examples/tree/main/examples/qq-info  
接口文档：https://apizero.cn/aidocs/qq

