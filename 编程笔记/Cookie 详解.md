# Cookie 详解

## 一、什么是 Cookie

### 1.1 简单理解

想象一下，你去一家咖啡店：

```
第一次去：
你 → 咖啡店 → 店员不认识你 → 你点单 → 结账离开

第二次去：
你 → 咖啡店 → 店员认出你 → "先生，还是老样子吗？" → 快速服务
```

**Cookie 就是那个"认出你"的小本本**，它记录了你的信息，让服务器能记住你。

### 1.2 官方定义

Cookie 是服务器发送给浏览器的一小段文本信息，浏览器会将其保存在本地。当浏览器再次访问同一服务器时，会自动携带这些 Cookie，让服务器识别出用户。

```
服务器                              浏览器
  │                                    │
  │  Set-Cookie: user_id=123          │
  │ ─────────────────────────────────▶│
  │                                    │
  │  下次请求自动携带                  │
  │◀───────────────────────────────── │
  │  Cookie: user_id=123              │
```

### 1.3 Cookie 的作用

| 作用 | 说明 | 示例 |
|------|------|------|
| **会话管理** | 保存登录状态 | 用户登录后，下次访问自动识别 |
| **个性化** | 记住用户偏好 | 语言设置、主题选择 |
| **购物车** | 跨页面保存数据 | 电商网站的购物车功能 |
| **跟踪分析** | 用户行为分析 | 广告定向投放 |

---

## 二、Cookie 的工作原理

### 2.1 Cookie 的生命周期

```
┌─────────────────────────────────────────────────────────────┐
│                    Cookie 生命周期                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  服务器设置 Cookie                                          │
│       │                                                     │
│       ▼                                                     │
│  浏览器接收并存储                                            │
│       │                                                     │
│       ▼                                                     │
│  浏览器下次请求携带                                          │
│       │                                                     │
│       ▼                                                     │
│  服务器读取并识别用户                                        │
│       │                                                     │
│       ▼                                                     │
│  Cookie 过期或被清除                                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 2.2 HTTP 请求中的 Cookie

**服务器设置 Cookie（响应头）**：

```http
HTTP/1.1 200 OK
Content-Type: text/html
Set-Cookie: user_id=123; Path=/; Expires=Wed, 15 Jul 2026 10:00:00 GMT; HttpOnly; Secure
```

**浏览器携带 Cookie（请求头）**：

```http
GET /api/user HTTP/1.1
Host: example.com
Cookie: user_id=123; session=abc123
```

### 2.3 Cookie 的属性

| 属性 | 说明 | 示例 |
|------|------|------|
| **Name=Value** | Cookie 的名称和值 | `user_id=123` |
| **Expires** | 过期时间 | `Expires=Wed, 15 Jul 2026 10:00:00 GMT` |
| **Max-Age** | 存活秒数 | `Max-Age=3600`（1小时） |
| **Domain** | 作用域名 | `Domain=.example.com` |
| **Path** | 作用路径 | `Path=/api` |
| **HttpOnly** | 禁止 JavaScript 访问 | `HttpOnly` |
| **Secure** | 只在 HTTPS 下传输 | `Secure` |
| **SameSite** | 跨站请求限制 | `SameSite=Strict` |

---

## 三、Cookie 的类型

### 3.1 按过期时间分类

| 类型 | 说明 | 特点 |
|------|------|------|
| **会话 Cookie** | 浏览器关闭即失效 | 没有 Expires 或 Max-Age |
| **持久 Cookie** | 到期后才失效 | 设置了 Expires 或 Max-Age |

```javascript
// 会话 Cookie
document.cookie = "session_id=abc123";

// 持久 Cookie（1小时后过期）
document.cookie = "user_pref=dark; Max-Age=3600";

// 持久 Cookie（指定日期过期）
document.cookie = "remember_me=true; Expires=Wed, 15 Jul 2026 10:00:00 GMT";
```

### 3.2 按作用域分类

| 类型 | 说明 | 示例 |
|------|------|------|
| **会话 Cookie** | 当前会话有效 | 登录态 |
| **域名 Cookie** | 整个域名有效 | `.example.com` |
| **路径 Cookie** | 指定路径有效 | `/api` |

---

## 四、Cookie 的安全属性

### 4.1 HttpOnly

**作用**：禁止 JavaScript 访问 Cookie，防止 XSS 攻击

```
┌─────────────────────────────────────────────────────────────┐
│                    HttpOnly 保护机制                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  没有 HttpOnly:                                              │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐      │
│  │ 恶意脚本    │───▶│ JS 读取     │───▶│ 窃取 Cookie │      │
│  │ (XSS攻击)   │    │ document.cookie│ │             │      │
│  └─────────────┘    └─────────────┘    └─────────────┘      │
│                                                             │
│  有 HttpOnly:                                                │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐      │
│  │ 恶意脚本    │───▶│ JS 读取     │───▶│ 读取失败    │      │
│  │ (XSS攻击)   │    │ document.cookie│ │ (undefined) │      │
│  └─────────────┘    └─────────────┘    └─────────────┘      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**设置方式**：

```go
// Go 语言设置 HttpOnly Cookie
http.SetCookie(w, &http.Cookie{
    Name:     "session",
    Value:    "abc123",
    HttpOnly: true,
})
```

### 4.2 Secure

**作用**：只在 HTTPS 连接下传输 Cookie

```
HTTP:  Cookie 明文传输 → 可能被窃取
HTTPS: Cookie 加密传输 → 安全
```

**设置方式**：

```go
http.SetCookie(w, &http.Cookie{
    Name:     "session",
    Value:    "abc123",
    Secure:   true,
    HttpOnly: true,
})
```

### 4.3 SameSite

**作用**：防止 CSRF 攻击，控制跨站请求时是否携带 Cookie

| 值 | 说明 |
|----|------|
| **Strict** | 仅在同源请求时携带 |
| **Lax** | 允许部分跨站请求携带（如链接跳转） |
| **None** | 允许所有跨站请求携带（需配合 Secure） |

```
CSRF 攻击示意图：

┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  攻击者网站  │    │  用户浏览器  │    │  目标网站   │
│ (evil.com)  │    │             │    │(bank.com)   │
└──────┬──────┘    └──────┬──────┘    └──────┬──────┘
       │                  │                  │
       │  <img src=       │                  │
       │  "bank.com/      │                  │
       │  transfer?       │                  │
       │  to=attacker">  │                  │
       │────────────────▶│                  │
       │                  │  携带 bank.com   │
       │                  │  的 Cookie       │
       │                  │────────────────▶│
       │                  │                  │  执行转账！
       │                  │                  │
```

**设置方式**：

```go
http.SetCookie(w, &http.Cookie{
    Name:     "session",
    Value:    "abc123",
    HttpOnly: true,
    Secure:   true,
    SameSite: http.SameSiteStrictMode,
})
```

---

## 五、Cookie 与 Session 的关系

### 5.1 区别与联系

| 特性 | Cookie | Session |
|------|--------|---------|
| **存储位置** | 客户端 | 服务端 |
| **存储内容** | 少量文本（通常 < 4KB） | 任意数据 |
| **安全性** | 较低（可被篡改） | 较高 |
| **生命周期** | 可持久化 | 通常较短 |
| **传输方式** | 每次请求自动携带 | 通过 Cookie 传递 Session ID |

### 5.2 工作流程

```
┌─────────────────────────────────────────────────────────────┐
│                Cookie + Session 工作流程                    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  用户登录：                                                  │
│                                                             │
│  浏览器 ──POST /login──▶ 服务器                              │
│                              │                              │
│                              ▼                              │
│                       验证用户名密码                          │
│                              │                              │
│                              ▼                              │
│                    创建 Session 对象                         │
│                    SessionID = "abc123"                     │
│                              │                              │
│                              ▼                              │
│  浏览器 ◀──Set-Cookie: session=abc123── 服务器               │
│                              │                              │
│                              ▼                              │
│  用户访问其他页面：                                           │
│                              │                              │
│  浏览器 ──Cookie: session=abc123──▶ 服务器                   │
│                              │                              │
│                              ▼                              │
│                       根据 SessionID                         │
│                       查找 Session 对象                      │
│                              │                              │
│                              ▼                              │
│                    返回用户数据                              │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 5.3 无 Cookie 场景

**使用 Token（JWT）**：

```
浏览器 ──Authorization: Bearer <token>──▶ 服务器
```

---

## 六、Cookie 的限制

### 6.1 大小限制

- **单个 Cookie**：通常不超过 4KB
- **每个域名**：通常限制 50-100 个 Cookie

### 6.2 安全限制

- **HttpOnly**：防止 JS 读取
- **Secure**：强制 HTTPS
- **SameSite**：防止 CSRF

### 6.3 隐私限制

- **第三方 Cookie**：被浏览器逐渐限制
- **Do Not Track**：用户可选择不被追踪

---

## 七、Cookie 的常见问题

### 7.1 Cookie 被禁用怎么办？

**方案一**：URL 参数传递（不推荐，不安全）

```
https://example.com/api/user?session=abc123
```

**方案二**：Token 放在请求头

```http
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**方案三**：隐藏表单字段

```html
<form action="/submit" method="post">
    <input type="hidden" name="session" value="abc123">
</form>
```

### 7.2 Cookie 被篡改怎么办？

**解决方案**：签名验证

```go
package cookie

import (
	"crypto/hmac"
	"crypto/sha256"
	"encoding/base64"
)

func SignCookie(value, secret string) string {
	mac := hmac.New(sha256.New, []byte(secret))
	mac.Write([]byte(value))
	signature := base64.StdEncoding.EncodeToString(mac.Sum(nil))
	return value + "." + signature
}

func VerifyCookie(signedValue, secret string) (string, bool) {
	parts := strings.SplitN(signedValue, ".", 2)
	if len(parts) != 2 {
		return "", false
	}
	
	value, signature := parts[0], parts[1]
	expectedSignature := base64.StdEncoding.EncodeToString(
		hmac.New(sha256.New, []byte(secret)).Sum([]byte(value)))
	
	return value, signature == expectedSignature
}
```

### 7.3 Cookie 跨域问题

**问题**：不同域名的 Cookie 不能共享

```
example.com 的 Cookie 不能被 api.example.com 访问？
不，子域名可以访问父域名的 Cookie！
```

**设置方式**：

```go
http.SetCookie(w, &http.Cookie{
    Name:     "user_id",
    Value:    "123",
    Domain:   ".example.com",  // 所有子域名都能访问
    Path:     "/",
    HttpOnly: true,
})
```

---

## 八、Cookie 的替代品

### 8.1 Web Storage

| 特性 | LocalStorage | SessionStorage | Cookie |
|------|-------------|----------------|--------|
| **大小** | 5-10MB | 5-10MB | 4KB |
| **生命周期** | 持久 | 会话 | 可配置 |
| **传输** | 不自动发送 | 不自动发送 | 自动发送 |
| **存储位置** | 客户端 | 客户端 | 客户端 |

```javascript
// LocalStorage
localStorage.setItem('username', 'john');
localStorage.getItem('username');  // 'john'

// SessionStorage
sessionStorage.setItem('temp_data', 'value');
```

### 8.2 IndexedDB

**特点**：
- 更大的存储空间（无固定限制）
- 支持复杂查询
- 异步操作

### 8.3 Service Worker Cache

**特点**：
- 用于离线缓存
- 可编程缓存策略
- 不适合存储用户数据

---

## 九、实践示例

### 9.1 Go 语言操作 Cookie

**设置 Cookie**：

```go
func SetCookieHandler(w http.ResponseWriter, r *http.Request) {
    cookie := &http.Cookie{
        Name:     "user_id",
        Value:    "123",
        Path:     "/",
        MaxAge:   3600,
        HttpOnly: true,
        Secure:   true,
        SameSite: http.SameSiteStrictMode,
    }
    http.SetCookie(w, cookie)
    fmt.Fprintf(w, "Cookie set successfully")
}
```

**读取 Cookie**：

```go
func GetCookieHandler(w http.ResponseWriter, r *http.Request) {
    cookie, err := r.Cookie("user_id")
    if err != nil {
        http.Error(w, "Cookie not found", http.StatusNotFound)
        return
    }
    fmt.Fprintf(w, "User ID: %s", cookie.Value)
}
```

**删除 Cookie**：

```go
func DeleteCookieHandler(w http.ResponseWriter, r *http.Request) {
    cookie := &http.Cookie{
        Name:     "user_id",
        Value:    "",
        Path:     "/",
        MaxAge:   -1,
        HttpOnly: true,
        Secure:   true,
    }
    http.SetCookie(w, cookie)
    fmt.Fprintf(w, "Cookie deleted")
}
```

### 9.2 JavaScript 操作 Cookie

**设置 Cookie**：

```javascript
function setCookie(name, value, days) {
    let expires = "";
    if (days) {
        let date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + (value || "") + expires + "; path=/";
}
```

**读取 Cookie**：

```javascript
function getCookie(name) {
    let nameEQ = name + "=";
    let ca = document.cookie.split(';');
    for (let i = 0; i < ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) == ' ') c = c.substring(1, c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
    }
    return null;
}
```

**删除 Cookie**：

```javascript
function deleteCookie(name) {
    document.cookie = name + "=; Max-Age=-99999999; path=/";
}
```

---

## 十、安全最佳实践

### 10.1 Cookie 安全清单

- [ ] 使用 `HttpOnly` 属性防止 XSS
- [ ] 使用 `Secure` 属性强制 HTTPS
- [ ] 使用 `SameSite` 属性防止 CSRF
- [ ] 设置合理的过期时间
- [ ] 对敏感数据进行签名或加密
- [ ] 避免存储敏感信息在 Cookie 中

### 10.2 不要做的事情

```javascript
// ❌ 不要存储密码
document.cookie = "password=123456";

// ❌ 不要存储明文 Token
document.cookie = "token=abc123";

// ❌ 不要信任用户提交的 Cookie
// 始终在服务端验证
```

### 10.3 推荐做法

```go
// ✅ 使用 HttpOnly + Secure
http.SetCookie(w, &http.Cookie{
    Name:     "session",
    Value:    SignCookie(sessionID, secret),
    HttpOnly: true,
    Secure:   true,
    SameSite: http.SameSiteStrictMode,
})

// ✅ 服务端验证
sessionID, ok := VerifyCookie(cookie.Value, secret)
if !ok {
    http.Error(w, "Invalid cookie", http.StatusUnauthorized)
    return
}
```

---

## 十一、总结

### 11.1 Cookie 的本质

Cookie 是浏览器存储在客户端的一小段文本，用于在 HTTP 请求之间传递状态信息。

### 11.2 核心要点

1. **会话管理**：最主要的用途
2. **安全属性**：HttpOnly、Secure、SameSite
3. **与 Session 配合**：客户端存 Session ID，服务端存数据
4. **替代品**：LocalStorage、IndexedDB、Token

### 11.3 发展趋势

- 第三方 Cookie 逐渐被淘汰
- 隐私保护越来越严格
- Token-based 认证越来越流行

Cookie 虽然简单，但却是 Web 开发中不可或缺的技术。理解它的工作原理和安全属性，对于构建安全可靠的 Web 应用至关重要。