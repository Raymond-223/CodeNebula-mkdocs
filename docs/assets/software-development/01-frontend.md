# 前端开发

前端开发是软件工程中最贴近用户的领域之一，涵盖了从页面结构、视觉呈现到交互逻辑的完整链路。本章从 HTML5 语义化、CSS3 布局与动画、JavaScript 核心进阶、TypeScript 静态类型系统，到 React、Vue、Angular 三大主流框架及构建工具链、性能优化策略，进行系统性、高密度的讲解。读者可将其作为日常开发的手册式参考。

---

## 一、HTML5 核心

### 1.1 语义化 HTML

语义化标签不仅提升代码可读性，对 SEO 和无障碍访问有直接影响。HTML5 引入了一套描述页面区域的标准标签：

```html
<body>
  <header>
    <nav>
      <ul>
        <li><a href="/">首页</a></li>
        <li><a href="/blog">博客</a></li>
      </ul>
    </nav>
  </header>
  <main>
    <article>
      <h1>文章标题</h1>
      <section>
        <h2>章节一</h2>
        <p>内容…</p>
      </section>
    </article>
    <aside>
      <h3>相关阅读</h3>
      <ul>…</ul>
    </aside>
  </main>
  <footer>
    <p>&copy; 2026 CodeNebula</p>
  </footer>
</body>
```

| 标签 | 作用 | SEO 影响 |
|------|------|----------|
| `<header>` | 页眉或区块头部 | 提升标题权重 |
| `<nav>` | 导航区域 | 搜索引擎优先抓取 |
| `<main>` | 页面主体（唯一） | 核心内容权重提升 |
| `<article>` | 独立内容单元 | 利于摘要展示 |
| `<section>` | 主题分组 | 结构化评分加分 |
| `<aside>` | 侧边或补充内容 | 辅助内容标记 |
| `<footer>` | 页脚或区块尾部 | 版权/元信息 |

### 1.2 表单与验证

现代 HTML 表单内置了丰富的输入类型和验证属性，减少对 JavaScript 的依赖：

```html
<form novalidate>
  <label for="email">邮箱</label>
  <input
    type="email"
    id="email"
    name="email"
    required
    pattern="[a-z0-9._%+\-]+@[a-z0-9.\-]+\.[a-z]{2,}$"
    autocomplete="email"
  />

  <label for="tel">电话</label>
  <input type="tel" id="tel" name="tel" pattern="[0-9]{11}" />

  <label for="age">年龄</label>
  <input type="number" id="age" name="age" min="1" max="150" step="1" />

  <label for="color">偏好颜色</label>
  <input type="color" id="color" name="color" />

  <input type="submit" value="提交" />
</form>
```

**Constraint Validation API** 可自定义校验消息：

```javascript
const input = document.getElementById('email');
input.addEventListener('invalid', (e) => {
  e.preventDefault();
  input.setCustomValidity('请输入有效的邮箱地址');
});
```

### 1.3 无障碍访问（ARIA）

ARIA（Accessible Rich Internet Applications）为辅助技术提供语义补充。优先使用原生语义标签，仅在无法满足时使用 ARIA：

```html
<!-- 错误：重复语义 -->
<nav role="navigation">…</nav>

<!-- 正确：自定义组件使用 ARIA -->
<div
  role="tablist"
  aria-label="文档选项卡"
>
  <button role="tab" aria-selected="true" tabindex="0">HTML</button>
  <button role="tab" aria-selected="false" tabindex="-1">CSS</button>
</div>
<div role="tabpanel" aria-labelledby="tab-1">
  HTML 内容…
</div>
```

**关键 ARIA 属性速查：**

| 属性 | 用途 | 示例值 |
|------|------|--------|
| `aria-label` | 元素标签 | `"关闭对话框"` |
| `aria-labelledby` | 引用标签元素 ID | `"heading-id"` |
| `aria-describedby` | 详细描述 | `"desc-id"` |
| `aria-expanded` | 展开状态 | `true` / `false` |
| `aria-hidden` | 从无障碍树隐藏 | `true` |
| `aria-live` | 动态区域通知 | `polite` / `assertive` |

### 1.4 SEO 基础

**Meta 标签：**

```html
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<meta name="description" content="CodeNebula 软件开发知识库" />
<meta name="keywords" content="前端, React, Vue, TypeScript" />
```

**Open Graph（社交媒体分享）：**

```html
<meta property="og:title" content="前端开发完全指南" />
<meta property="og:description" content="覆盖 HTML/CSS/JS/TS/框架的全链路知识体系" />
<meta property="og:image" content="https://example.com/og-image.png" />
<meta property="og:url" content="https://example.com/frontend" />
<meta property="og:type" content="article" />
```

**结构化数据（Schema.org / JSON-LD）：**

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "TechArticle",
  "headline": "前端开发完全指南",
  "author": { "@type": "Person", "name": "CodeNebula" },
  "datePublished": "2026-07-23",
  "description": "覆盖 HTML/CSS/JS/TS/框架的全链路知识体系"
}
</script>
```

---

## 二、CSS3 深入

### 2.1 选择器详解

**伪类（Pseudo-classes）** 描述元素的特殊状态：

```css
/* 结构性伪类 */
li:first-child { }
li:last-child { }
li:nth-child(2n+1) { }   /* 奇数行 */
li:nth-last-child(3) { } /* 倒数第三个 */

/* 状态伪类 */
input:focus { }
input:disabled { }
input:checked + label { }
button:hover { }

/* 否定伪类 */
div:not(.excluded) { }

/* 空值/范围 */
input:required { }
input:in-range { }
input:out-of-range { }
```

**伪元素（Pseudo-elements）** 创建 DOM 树之外的虚拟元素：

```css
/* 双冒号是标准写法，兼容旧浏览器可用单冒号 */
h2::before {
  content: "📌 ";
}
blockquote::after {
  content: " — 引自 CodeNebula";
}
input::placeholder {
  color: #999;
}
/* 选中文本样式 */
::selection {
  background: #3390ff;
  color: white;
}
```

**属性选择器** 按 HTML 属性精准匹配：

| 选择器 | 匹配规则 | 示例 |
|--------|----------|------|
| `[attr]` | 存在该属性 | `[disabled]` |
| `[attr="val"]` | 精确等于 | `[type="email"]` |
| `[attr^="val"]` | 以 val 开头 | `[href^="https"]` |
| `[attr$="val"]` | 以 val 结尾 | `[src$=".webp"]` |
| `[attr*="val"]` | 包含 val | `[class*="icon"]` |
| `[attr|="val"]` | 以 val- 开头 | `[lang|="zh"]` |
| `[attr~="val"]` | 空格分隔包含 | `[rel~="noopener"]` |

### 2.2 盒模型

CSS 盒模型由 `content → padding → border → margin` 构成。`box-sizing` 决定 width/height 的计算范围：

```css
/* 默认：标准盒模型 */
.box-content {
  box-sizing: content-box;
  width: 200px;      /* 仅内容区宽度 */
  padding: 20px;
  border: 2px solid;
  /* 实际渲染宽度：200 + 20*2 + 2*2 = 244px */
}

/* 常用：IE/怪异盒模型 */
.box-border {
  box-sizing: border-box;
  width: 200px;      /* 包含 padding 和 border */
  padding: 20px;
  border: 2px solid;
  /* 实际渲染宽度：200px，内容宽度自动缩为 156px */
}
```

**外边距折叠（Margin Collapsing）** 发生在垂直方向上相邻的块级元素之间，取两者中较大的外边距：

```css
/* 两个相邻 div，一个 margin-bottom: 30px，一个 margin-top: 20px */
/* 最终间距为 30px（取大值）而非 50px */
```

解决方法：使用 BFC（Block Formatting Context）、flex 容器、或单边 margin。

### 2.3 Flexbox

一维布局模型，适用于导航、居中、等分等场景。

**容器属性：**

```css
.container {
  display: flex;
  flex-direction: row;         /* row | column | row-reverse | column-reverse */
  flex-wrap: wrap;             /* nowrap | wrap | wrap-reverse */
  justify-content: center;     /* flex-start | flex-end | center | space-between | space-around | space-evenly */
  align-items: center;         /* stretch | flex-start | flex-end | center | baseline */
  align-content: space-around; /* 多行时的交叉轴对齐 */
  gap: 16px;                   /* row-gap + column-gap 简写 */
}
```

**项目属性：**

```css
.item {
  flex: 1 1 200px;            /* grow shrink basis */
  align-self: flex-end;       /* 单独覆盖 align-items */
  order: -1;                  /* 排序，默认 0 */
}
```

**常见布局模式：**

```css
/* 圣杯布局 — 中间自适应，两侧固定 */
.holy-grail {
  display: flex;
}
.holy-grail > .sidebar {
  flex: 0 0 250px;
}
.holy-grail > .main {
  flex: 1 1 auto;
}

/* 水平垂直居中 */
.center {
  display: flex;
  justify-content: center;
  align-items: center;
}

/* 粘性页脚 */
.page {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}
.page > .content {
  flex: 1;
}
```

### 2.4 Grid

二维布局系统，适合页面整体结构或复杂网格场景。

```css
.grid {
  display: grid;
  grid-template-columns: 250px 1fr 1fr;     /* 三列：固定 + 等比 */
  grid-template-rows: auto 1fr auto;         /* 三行 */
  grid-template-areas:
    "header header header"
    "sidebar main main"
    "footer footer footer";
  gap: 16px;
}

.header { grid-area: header; }
.sidebar { grid-area: sidebar; }
.main { grid-area: main; }
.footer { grid-area: footer; }
```

**高级技术：**

```css
/* 自动响应列，无需媒体查询 */
.auto-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1rem;
}

/* fr 单位与固定值混用 */
.dashboard {
  display: grid;
  grid-template-columns: 2fr 1fr 300px;
}

/* 显式放置项目 */
.card:first-child {
  grid-column: span 2;   /* 跨两列 */
  grid-row: 1 / 3;       /* 从行线1到行线3 */
}
```

| 方法 | 适用场景 | 优势 |
|------|----------|------|
| Flexbox | 导航、居中、一维排列 | 灵活、内容驱动 |
| Grid | 页面骨架、二维布局 | 精准控制行列、区域命名 |

### 2.5 响应式设计

**移动优先（Mobile First）原则：** 先写移动端样式，再通过 `min-width` 媒体查询渐进增强：

```css
/* 基础样式 — 移动端 */
.container {
  padding: 1rem;
  font-size: 16px;
}

/* 平板 ≥768px */
@media (min-width: 768px) {
  .container {
    padding: 2rem;
    display: grid;
    grid-template-columns: 1fr 1fr;
  }
}

/* 桌面 ≥1200px */
@media (min-width: 1200px) {
  .container {
    grid-template-columns: 1fr 1fr 1fr 1fr;
  }
}
```

**常见断点参考：**

| 断点 | 范围 | 设备 |
|------|------|------|
| `320px` | 小屏手机 | iPhone SE |
| `375px` | 主流手机 | iPhone 12/13/14 |
| `768px` | 平板 | iPad |
| `1024px` | 小屏笔记本 | iPad Pro 横屏 |
| `1200px` | 桌面 | 标准显示器 |
| `1440px+` | 大屏 | 2K/4K 显示器 |

### 2.6 动画与过渡

**Transitions（过渡）：**

```css
.button {
  background: #3390ff;
  color: white;
  transition: background 0.3s ease, transform 0.2s cubic-bezier(0.4, 0, 0.2, 1);
}
.button:hover {
  background: #1a6fd0;
  transform: translateY(-2px);
}
```

**Keyframes（关键帧动画）：**

```css
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animated {
  animation: fadeInUp 0.6s ease-out forwards;
  /* animation: name duration timing-function delay iteration-count direction fill-mode */
}
```

**Transforms（变换）性能优化：** 优先使用 `transform` 和 `opacity` 做动画，它们仅触发合成（Composite），不触发重排（Reflow）或重绘（Repaint）：

```css
/* 高效 — 仅合成层 */
.box {
  transform: translateX(100px);
  opacity: 0.5;
}

/* 低效 — 触发重排 */
.box {
  left: 100px;
}
```

### 2.7 SCSS 预处理器

SCSS 通过编译生成 CSS，提供变量、嵌套、混合、函数等能力：

```scss
// 变量
$primary: #3390ff;
$spacing-unit: 8px;
$breakpoint-md: 768px;

// 混合
@mixin card($radius: 8px, $shadow: true) {
  border-radius: $radius;
  padding: $spacing-unit * 2;
  @if $shadow {
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  }
}

// 嵌套 + 父选择器引用
.card {
  @include card(12px);

  &__title {
    font-size: 1.25rem;
    color: darken($primary, 20%);
  }

  &--featured {
    border: 2px solid $primary;
  }

  @media (max-width: $breakpoint-md) {
    padding: $spacing-unit;
  }
}

// 函数
@function px-to-rem($px, $base: 16px) {
  @return calc($px / $base) * 1rem;
}

.title {
  font-size: px-to-rem(24px); // 1.5rem
}
```

### 2.8 CSS 自定义属性（CSS Variables）

与 SCSS 变量不同，CSS 自定义属性是运行时的、可级联的、可在 JavaScript 中读写：

```css
:root {
  --color-primary: #3390ff;
  --color-text: #1a1a2e;
  --spacing-md: 16px;
  --border-radius: 8px;
}

.card {
  background: var(--color-primary);
  color: var(--color-text);
  padding: var(--spacing-md);
  border-radius: var(--border-radius);
}

/* 通过作用域覆盖 */
.dark-mode {
  --color-text: #eee;
  --color-primary: #66b0ff;
}
```

**JavaScript 读写自定义属性：**

```javascript
const root = document.documentElement;
// 读取
const primary = getComputedStyle(root).getPropertyValue('--color-primary').trim();
// 写入
root.style.setProperty('--color-primary', '#ff6633');
```

| 特性 | SCSS 变量 | CSS 自定义属性 |
|------|-----------|----------------|
| 作用域 | 编译时 | 运行时、DOM 级联 |
| 动态性 | 不可变 | 可 JS 动态修改 |
| 媒体查询 | 不支持 | 支持 |
| 计算 | 编译时计算 | 运行时计算 |

---

## 三、JavaScript 深入

### 3.1 ES6+ 核心特性

**let / const 与块级作用域：**

```javascript
// var 函数作用域，存在变量提升
console.log(x); // undefined（提升但未初始化）
var x = 1;

// let/const 块级作用域，TDZ（暂时性死区）
console.log(y); // ReferenceError
let y = 1;

const PI = 3.14; // 必须初始化，不可重新赋值
// PI = 3;      // TypeError
const obj = { a: 1 };
obj.a = 2;       // ✅ 对象属性可修改
```

**解构赋值：**

```javascript
// 数组解构
const [first, second, ...rest] = [1, 2, 3, 4, 5];
// first=1, second=2, rest=[3,4,5]

// 对象解构 + 重命名 + 默认值
const { name: userName = '匿名', age = 18 } = { name: 'Alice' };
// userName='Alice', age=18

// 嵌套解构
const { address: { city, zip } } = { address: { city: '北京', zip: '100000' } };

// 函数参数解构
function createUser({ name, role = 'user' }) { … }
```

**展开运算符与 Rest 参数：**

```javascript
// 数组展开
const arr1 = [1, 2], arr2 = [3, 4];
const merged = [...arr1, ...arr2]; // [1,2,3,4]

// 对象展开（浅拷贝）
const base = { a: 1, b: 2 };
const extended = { ...base, c: 3 }; // {a:1, b:2, c:3}

// Rest 参数
function sum(...nums) {
  return nums.reduce((a, b) => a + b, 0);
}
```

**可选链（Optional Chaining）与空值合并（Nullish Coalescing）：**

```javascript
const user = { profile: { name: 'Bob' } };

// 传统深访问 — 易报错
// const city = user.address.city; // TypeError

// 可选链 — 短路返回 undefined
const city = user?.address?.city; // undefined

// 空值合并 — 仅对 null/undefined 生效
const count = user?.count ?? 0;   // 0（而非空字符串或 0 被替换）
const name = user?.name || '默认'; // 传统写法：空字符串''也会被替换
```

**模板字面量：**

```javascript
const name = 'CodeNebula';
const year = 2026;
const html = `
  <div class="card">
    <h2>${name}</h2>
    <p>成立于 ${year} 年</p>
    ${isActive ? '<span class="badge">活跃中</span>' : ''}
  </div>
`;
```

### 3.2 函数进阶

**箭头函数：**

```javascript
// 简洁语法
const double = (x) => x * 2;

// 无参数时需写空括号
const now = () => Date.now();

// 返回对象字面量需加括号
const create = (id) => ({ id, timestamp: Date.now() });

// 关键区别：箭头函数无自己的 this
const obj = {
  name: 'Alice',
  greet: function() {
    setTimeout(() => {
      console.log(`Hello, ${this.name}`); // this 指向 obj
    }, 100);
  },
  badGreet: function() {
    setTimeout(function() {
      console.log(`Hello, ${this.name}`); // this 指向 window/undefined
    }, 100);
  }
};
```

**闭包（Closure）：**

```javascript
function createCounter() {
  let count = 0;          // 私有变量
  return {
    increment: () => ++count,
    decrement: () => --count,
    getCount: () => count,
  };
}

const counter = createCounter();
counter.increment();      // 1
counter.increment();      // 2
console.log(counter.count); // undefined — 无法直接访问
```

**IIFE（Immediately Invoked Function Expression）：**

```javascript
// 传统模块模式
const Module = (() => {
  const privateVar = 'secret';
  const privateMethod = () => console.log(privateVar);
  return {
    publicMethod: () => {
      privateMethod();
    }
  };
})();
```

**高阶函数与柯里化：**

```javascript
// 高阶函数：接收或返回函数
const withLogging = (fn) => (...args) => {
  console.log(`调用 ${fn.name}，参数:`, args);
  return fn(...args);
};

const add = (a, b) => a + b;
const loggedAdd = withLogging(add);
loggedAdd(2, 3); // 日志输出后返回 5

// 柯里化：多参转单参链式
const curry = (fn) => {
  return function curried(...args) {
    if (args.length >= fn.length) {
      return fn(...args);
    }
    return (...next) => curried(...args, ...next);
  };
};

const curriedAdd = curry((a, b, c) => a + b + c);
curriedAdd(1)(2)(3); // 6
```

### 3.3 异步编程

**事件循环机制：**

JavaScript 是单线程语言，依赖事件循环（Event Loop）实现异步。

```
执行栈 (Call Stack)
  ↓
Web APIs (setTimeout, fetch, DOM events)
  ↓
任务队列:
  ┌──────────────────────┐
  │ 微任务 (Microtask)   │ ← Promise.then, queueMicrotask, MutationObserver
  ├──────────────────────┤
  │ 宏任务 (Macrotask)   │ ← setTimeout, setInterval, I/O, UI render
  └──────────────────────┘
```

```javascript
console.log('1');                      // 同步
setTimeout(() => console.log('2'), 0); // 宏任务
Promise.resolve().then(() => {         // 微任务
  console.log('3');
  queueMicrotask(() => console.log('4')); // 微任务内嵌套微任务
});
console.log('5');                      // 同步
// 输出顺序：1, 5, 3, 4, 2
```

**Promise 链式调用：**

```javascript
fetch('/api/user')
  .then(res => {
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    return res.json();
  })
  .then(user => fetch(`/api/posts?userId=${user.id}`))
  .then(res => res.json())
  .then(posts => console.log(posts))
  .catch(err => console.error('请求失败:', err))
  .finally(() => console.log('完成'));

// 并行请求
const [user, posts] = await Promise.all([
  fetch('/api/user').then(r => r.json()),
  fetch('/api/posts').then(r => r.json()),
]);

// 竞赛 — 取最先完成的
const result = await Promise.race([
  fetch('/api/data').then(r => r.json()),
  new Promise((_, reject) => setTimeout(() => reject(new Error('超时')), 5000)),
]);
```

**async/await：**

```javascript
async function loadUserDashboard(userId) {
  try {
    const user = await fetch(`/api/user/${userId}`).then(r => r.json());
    const [posts, notifications] = await Promise.all([
      fetch(`/api/posts?userId=${userId}`).then(r => r.json()),
      fetch(`/api/notifications?userId=${userId}`).then(r => r.json()),
    ]);
    return { user, posts, notifications };
  } catch (error) {
    console.error('加载仪表盘失败:', error);
    throw error; // 或返回兜底数据
  }
}

// 顶层 await（ES2022、模块环境）
const config = await fetch('/config.json').then(r => r.json());
```

### 3.4 原型与类

JavaScript 通过原型链（Prototype Chain）实现继承：

```javascript
// 原型继承本质
const parent = { type: 'parent' };
const child = Object.create(parent);
child.name = 'child';
console.log(child.name); // 'child'（自有属性）
console.log(child.type); // 'parent'（原型链向上查找）
console.log(child.toString); // 继续沿原型链找到 Object.prototype
```

**ES6 Class 语法糖：**

```javascript
class Animal {
  // 私有字段（ES2022）
  #id = crypto.randomUUID();

  constructor(name) {
    this.name = name;
  }

  // 实例方法
  speak() {
    console.log(`${this.name} 发出了声音`);
  }

  // 静态方法
  static isAnimal(obj) {
    return obj instanceof Animal;
  }

  // Getter/Setter
  get id() {
    return this.#id;
  }
}

class Dog extends Animal {
  #breed;

  constructor(name, breed) {
    super(name); // 必须先调用 super
    this.#breed = breed;
  }

  speak() {
    console.log(`${this.name} 汪汪！`);
  }

  get breed() {
    return this.#breed;
  }

  static isDog(obj) {
    return obj instanceof Dog;
  }
}
```

### 3.5 模块系统

**ES Modules（ESM）：**

```javascript
// 📁 math.js
export const PI = 3.14159;
export function add(a, b) { return a + b; }
export default class Calculator { … }

// 📁 app.js
import Calculator, { PI, add as sum } from './math.js';
import * as MathUtils from './math.js'; // 命名空间导入

// 动态导入
const module = await import('./math.js');
console.log(module.PI);
```

**CommonJS vs ESM：**

| 特性 | CommonJS (Node.js) | ESM (浏览器/现代 Node) |
|------|-------------------|----------------------|
| 语法 | `require()` / `module.exports` | `import` / `export` |
| 加载 | 同步（运行时） | 异步（编译时静态分析） |
| 值绑定 | 值拷贝 | 动态绑定（只读引用） |
| 循环依赖 | 可处理（返回未完成对象） | 需谨慎处理 |
| Tree Shaking | 不支持 | 原生支持 |
| 顶层 await | 不支持 | 支持 |

### 3.6 数据结构

```javascript
// Map — 键可为任意类型
const userMap = new Map();
userMap.set('alice', { role: 'admin' });
userMap.set(42, 'answer');
console.log(userMap.size); // 2

// Set — 值唯一
const uniqueIds = new Set([1, 2, 2, 3, 3, 3]);
console.log([...uniqueIds]); // [1, 2, 3]

// WeakMap — 键为对象且弱引用，适合内存敏感缓存
const cache = new WeakMap();
function process(obj) {
  if (!cache.has(obj)) {
    cache.set(obj, expensiveComputation(obj));
  }
  return cache.get(obj);
}

// WeakSet — 类似 WeakMap，值唯一且弱引用
const activeElements = new WeakSet();
```

### 3.7 错误处理

```javascript
class ValidationError extends Error {
  constructor(field, message) {
    super(message);
    this.name = 'ValidationError';
    this.field = field;
  }
}

function validateUser(data) {
  if (!data.email) {
    throw new ValidationError('email', '邮箱不能为空');
  }
  if (!data.email.includes('@')) {
    throw new ValidationError('email', '邮箱格式无效');
  }
}

try {
  validateUser({ email: 'invalid' });
} catch (err) {
  if (err instanceof ValidationError) {
    console.error(`字段 ${err.field}: ${err.message}`);
  } else {
    console.error('未知错误:', err);
  }
} finally {
  console.log('验证完成');
}
```

### 3.8 设计模式

```javascript
// 单例模式 (Singleton)
class Database {
  static #instance;
  constructor() {
    if (Database.#instance) return Database.#instance;
    Database.#instance = this;
  }
}

// 观察者模式 (Observer)
class EventBus {
  #listeners = new Map();
  on(event, fn) {
    if (!this.#listeners.has(event)) this.#listeners.set(event, []);
    this.#listeners.get(event).push(fn);
    return () => this.off(event, fn);
  }
  off(event, fn) {
    const listeners = this.#listeners.get(event);
    if (listeners) this.#listeners.set(event, listeners.filter(l => l !== fn));
  }
  emit(event, ...args) {
    this.#listeners.get(event)?.forEach(fn => fn(...args));
  }
}

// 工厂模式 (Factory)
class UserFactory {
  static create(type, data) {
    switch (type) {
      case 'admin': return new AdminUser(data);
      case 'editor': return new EditorUser(data);
      default: return new RegularUser(data);
    }
  }
}
```

---

## 四、TypeScript

### 4.1 类型系统基础

```typescript
// 基础类型
let isDone: boolean = false;
let count: number = 42;
let name: string = 'TypeScript';
let list: number[] = [1, 2, 3];
let tuple: [string, number] = ['hello', 42];
let nullable: string | null = null;
let anything: any = '可以是任何类型'; // 慎用

// 联合类型 + 类型字面量
type Status = 'idle' | 'loading' | 'success' | 'error';
let currentStatus: Status = 'idle'; // 只能取这四个值

// 交叉类型
type WithName = { name: string };
type WithAge = { age: number };
type Person = WithName & WithAge; // 同时包含 name 和 age

// 枚举
enum Direction {
  Up = 'UP',
  Down = 'DOWN',
  Left = 'LEFT',
  Right = 'RIGHT',
}
```

### 4.2 Interfaces 与 Types

```typescript
// Interface — 可声明合并，可扩展
interface User {
  readonly id: string;  // 只读
  name: string;
  email?: string;       // 可选
  role: 'admin' | 'user';
}

// 同名 interface 自动合并
interface User {
  createdAt: Date;
}

// Type — 不可合并，但更灵活
type Animal = {
  species: string;
  sound: string;
};

// 联合类型只能用 type
type Result<T> = { ok: true; data: T } | { ok: false; error: string };
```

| 特性 | `interface` | `type` |
|------|-------------|--------|
| 声明合并 | ✅ 支持 | ❌ 不支持 |
| 联合类型 | ❌ | ✅ |
| 交集/交叉 | `extends` | `&` |
| 映射类型 | ❌ | ✅ |
| 类实现 | ✅ `implements` | ✅ `implements` |
| 推荐场景 | 对象结构、API 定义 | 联合类型、工具类型 |

### 4.3 泛型

```typescript
// 泛型函数
function first<T>(arr: T[]): T | undefined {
  return arr[0];
}

const num = first([1, 2, 3]);  // number
const str = first(['a', 'b']); // string

// 泛型约束
interface HasLength {
  length: number;
}
function logLength<T extends HasLength>(arg: T): T {
  console.log(arg.length);
  return arg;
}
logLength('hello');  // ✅ 字符串有 length
logLength([1, 2]);   // ✅ 数组有 length
// logLength(42);    // ❌ 数字无 length

// 条件类型
type IsString<T> = T extends string ? 'yes' : 'no';
type A = IsString<string>; // 'yes'
type B = IsString<number>; // 'no'

// infer 关键字 — 提取类型
type ReturnTypeOf<T> = T extends (...args: any[]) => infer R ? R : never;
type Fn = (x: number) => string;
type R = ReturnTypeOf<Fn>; // string
```

### 4.4 实用工具类型（Utility Types）

```typescript
interface User {
  id: string;
  name: string;
  email: string;
  role: string;
  createdAt: Date;
}

// 全部可选
type PartialUser = Partial<User>;

// 全部必填
type RequiredUser = Required<PartialUser>;

// 选子集
type UserBasic = Pick<User, 'id' | 'name' | 'email'>;

// 排除属性
type UserWithoutTimestamps = Omit<User, 'createdAt'>;

// 记录类型
type UserRoles = Record<string, 'admin' | 'user' | 'guest'>;
const roles: UserRoles = { alice: 'admin', bob: 'user' };

// 提取函数返回类型
function createUser() { return { id: '1', name: 'Alice' }; }
type CreatedUser = ReturnType<typeof createUser>;

// 提取参数类型
type CreateUserParams = Parameters<typeof createUser>;
```

### 4.5 装饰器

TypeScript 装饰器是实验性特性（需在 `tsconfig.json` 中启用 `experimentalDecorators`）：

```typescript
// 类装饰器
function sealed(constructor: Function) {
  Object.seal(constructor);
  Object.seal(constructor.prototype);
}

@sealed
class Logger { }

// 方法装饰器
function log(target: any, propertyKey: string, descriptor: PropertyDescriptor) {
  const original = descriptor.value;
  descriptor.value = function (...args: any[]) {
    console.log(`调用 ${propertyKey}，参数:`, args);
    return original.apply(this, args);
  };
}

class Calculator {
  @log
  add(a: number, b: number) { return a + b; }
}
```

### 4.6 类型收窄与类型守卫

```typescript
// typeof 收窄
function printValue(val: string | number) {
  if (typeof val === 'string') {
    console.log(val.toUpperCase()); // 此处 val 为 string
  } else {
    console.log(val.toFixed(2));    // 此处 val 为 number
  }
}

// instanceof 收窄
class Dog { bark() {} }
class Cat { meow() {} }
function makeSound(animal: Dog | Cat) {
  if (animal instanceof Dog) {
    animal.bark();
  } else {
    animal.meow();
  }
}

// 自定义类型守卫
interface Fish { swim(): void; }
interface Bird { fly(): void; }

function isFish(pet: Fish | Bird): pet is Fish {
  return (pet as Fish).swim !== undefined;
}

function move(pet: Fish | Bird) {
  if (isFish(pet)) {
    pet.swim(); // TypeScript 知道此为 Fish
  } else {
    pet.fly();
  }
}
```

### 4.7 声明文件（\*.d.ts）

```typescript
// 📁 types.d.ts — 为无类型 JS 库编写声明
declare module 'legacy-lib' {
  export function doSomething(input: string): number;
  export const VERSION: string;
}

// 为全局变量声明
declare const API_BASE_URL: string;

// 增强已有模块
import 'react';
declare module 'react' {
  interface CSSProperties {
    '--custom-prop'?: string;
  }
}
```

---

## 五、React

### 5.1 组件

```jsx
// 函数组件（推荐）
function UserCard({ name, email, onDelete }) {
  return (
    <div className="user-card">
      <h3>{name}</h3>
      <p>{email}</p>
      <button onClick={() => onDelete(name)}>删除</button>
    </div>
  );
}

// 类组件（旧式）
class UserCard extends React.Component {
  render() {
    const { name, email, onDelete } = this.props;
    return (
      <div className="user-card">
        <h3>{name}</h3>
        <p>{email}</p>
        <button onClick={() => onDelete(name)}>删除</button>
      </div>
    );
  }
}
```

### 5.2 Hooks

```jsx
// useState — 状态管理
const [count, setCount] = useState(0);
const [user, setUser] = useState(null);

// useEffect — 副作用
useEffect(() => {
  fetch('/api/user').then(r => r.json()).then(setUser);
  return () => console.log('清理副作用'); // 组件卸载时执行
}, []); // 空依赖：仅挂载时执行

// useRef — 引用 DOM 或存储可变值（不触发重渲染）
const inputRef = useRef(null);
useEffect(() => { inputRef.current?.focus(); }, []);

// useContext — 上下文消费
const ThemeContext = createContext('light');
const theme = useContext(ThemeContext);

// useReducer — 复杂状态逻辑
const [state, dispatch] = useReducer(
  (state, action) => {
    switch (action.type) {
      case 'increment': return { count: state.count + 1 };
      case 'decrement': return { count: state.count - 1 };
      default: return state;
    }
  },
  { count: 0 }
);

// useMemo — 缓存计算结果
const sortedList = useMemo(
  () => items.sort((a, b) => a.name.localeCompare(b.name)),
  [items]
);

// useCallback — 缓存函数引用
const handleClick = useCallback(
  (id) => { console.log('点击:', id); },
  []
);
```

**自定义 Hooks：**

```javascript
function useDebounce(value, delay = 300) {
  const [debounced, setDebounced] = useState(value);

  useEffect(() => {
    const timer = setTimeout(() => setDebounced(value), delay);
    return () => clearTimeout(timer);
  }, [value, delay]);

  return debounced;
}

// 使用
const searchTerm = useDebounce(inputValue, 500);
```

### 5.3 状态管理

| 方案 | 适用场景 | 优势 | 劣势 |
|------|----------|------|------|
| **useState / useReducer** | 组件内状态 | 零依赖 | 跨组件需 prop drilling |
| **Context API** | 低频更新的全局状态（主题、语言） | 内置 | 更新时所有消费者重渲染 |
| **Redux Toolkit** | 大型应用、复杂交互 | DevTools、中间件 | 样板代码多 |
| **Zustand** | 中小型应用 | 简洁、TypeScript 友好 | 生态较小 |
| **Jotai** | 原子化状态 | 细粒度更新 | 学习曲线 |

**Zustand 示例：**

```javascript
import { create } from 'zustand';

const useStore = create((set) => ({
  count: 0,
  increment: () => set((state) => ({ count: state.count + 1 })),
  reset: () => set({ count: 0 }),
}));

// 组件中使用
function Counter() {
  const { count, increment } = useStore();
  return <button onClick={increment}>{count}</button>;
}
```

### 5.4 性能优化

```jsx
// React.memo — 阻止不必要的重渲染
const ExpensiveList = React.memo(({ items }) => {
  return items.map(item => <li key={item.id}>{item.name}</li>);
});

// 代码分割 + 懒加载
const LazyComponent = React.lazy(() => import('./HeavyComponent'));

function App() {
  return (
    <Suspense fallback={<div>加载中...</div>}>
      <LazyComponent />
    </Suspense>
  );
}

// 虚拟列表 — 只渲染可视区域
// 推荐库：react-window、react-virtuoso
```

### 5.5 测试

```jsx
import { render, screen, fireEvent } from '@testing-library/react';
import userEvent from '@testing-library/user-event';

test('用户点击计数器', async () => {
  render(<Counter />);
  const button = screen.getByRole('button', { name: /点击/i });

  await userEvent.click(button);
  expect(screen.getByText('1')).toBeInTheDocument();
});
```

### 5.6 Next.js

```typescript
// App Router (app/page.tsx)
// SSR — 默认
async function Page() {
  const data = await fetch('https://api.example.com/posts');
  const posts = await data.json();
  return <PostList posts={posts} />;
}

// ISR — 增量静态生成
export const revalidate = 3600; // 每小时重新生成

// 静态生成 (SSG)
export async function generateStaticParams() {
  const posts = await fetch('https://api.example.com/posts').then(r => r.json());
  return posts.map(post => ({ id: post.id }));
}
```

| 渲染模式 | 数据更新时机 | 适用场景 |
|----------|-------------|----------|
| SSR (Server-Side) | 每次请求 | 个性化内容、实时数据 |
| SSG (Static) | 构建时 | 博客、文档、营销页 |
| ISR (Incremental) | 构建时 + 按需 | 内容频繁更新的站点 |
| CSR (Client-Side) | 客户端渲染 | 仪表盘、管理后台 |

---

## 六、Vue

### 6.1 Options API vs Composition API

```vue
<!-- Options API -->
<script>
export default {
  data() { return { count: 0 }; },
  computed: { doubled() { return this.count * 2; } },
  methods: { increment() { this.count++; } },
  watch: { count(newVal) { console.log('变化:', newVal); } },
};
</script>
```

```vue
<!-- Composition API（推荐） -->
<script setup>
import { ref, computed, watch } from 'vue';

const count = ref(0);
const doubled = computed(() => count.value * 2);
const increment = () => count.value++;
watch(count, (newVal) => console.log('变化:', newVal));
</script>
```

| 特性 | Options API | Composition API |
|------|-------------|-----------------|
| 组织方式 | 按选项类型分组 | 按逻辑功能分组 |
| 逻辑复用 | Mixins（命名冲突） | Composables（组合函数） |
| TypeScript 支持 | 一般 | 优秀 |
| 学习曲线 | 低 | 中 |
| 推荐 | 简单组件 | 复杂组件、大型项目 |

### 6.2 响应式系统

```javascript
import { ref, reactive, computed, watch } from 'vue';

// ref — 基本类型响应式
const name = ref('Alice');
console.log(name.value); // 模板中自动解包，无需 .value

// reactive — 对象深度响应式
const user = reactive({ name: 'Bob', profile: { age: 30 } });
console.log(user.profile.age); // 直接访问

// computed — 自动追踪依赖
const fullName = computed(() => `${firstName.value} ${lastName.value}`);

// watch — 监听变化
watch(
  () => user.profile.age,
  (newVal, oldVal) => console.log(`年龄 ${oldVal} -> ${newVal}`),
  { deep: true, immediate: true }
);

// watchEffect — 自动追踪所有依赖
watchEffect(() => {
  console.log(`用户 ${user.name} 年龄 ${user.profile.age}`);
});
```

### 6.3 Vue Router

```javascript
// router/index.js
import { createRouter, createWebHistory } from 'vue-router';

const routes = [
  {
    path: '/',
    component: () => import('../views/Home.vue'), // 懒加载
  },
  {
    path: '/user/:id',
    component: () => import('../views/User.vue'),
    children: [
      { path: 'profile', component: Profile },
      { path: 'settings', component: Settings },
    ],
  },
  {
    path: '/admin',
    meta: { requiresAuth: true },
    beforeEnter: (to, from) => {
      if (!isAuthenticated()) return '/login';
    },
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// 全局导航守卫
router.beforeEach((to, from) => {
  console.log(`${from.path} → ${to.path}`);
});
```

### 6.4 Pinia

```javascript
// stores/user.js
import { defineStore } from 'pinia';

export const useUserStore = defineStore('user', () => {
  // state
  const user = ref(null);
  const token = ref(localStorage.getItem('token'));

  // getters
  const isLoggedIn = computed(() => !!token.value);

  // actions
  async function login(email, password) {
    const res = await fetch('/api/login', { method: 'POST', body: { email, password } });
    const data = await res.json();
    token.value = data.token;
    user.value = data.user;
    localStorage.setItem('token', data.token);
  }

  function logout() {
    token.value = null;
    user.value = null;
    localStorage.removeItem('token');
  }

  return { user, token, isLoggedIn, login, logout };
});
```

### 6.5 Nuxt.js

```vue
<!-- app.vue — Nuxt 3 App Router -->
<template>
  <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>
</template>

<!-- pages/index.vue — 自动路由 -->
<script setup>
// SSR 数据获取
const { data: posts } = await useFetch('/api/posts');
</script>
```

---

## 七、Angular

### 7.1 组件与模板

```typescript
// 📁 user-card.component.ts
import { Component, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-user-card',
  standalone: true,
  template: `
    <div class="card">
      <h3>{{ user.name }}</h3>
      <p>{{ user.email }}</p>
      <button (click)="delete.emit(user.id)">删除</button>
    </div>
  `,
  styles: [`.card { padding: 1rem; border: 1px solid #ccc; }`],
})
export class UserCardComponent {
  @Input({ required: true }) user!: User;
  @Output() delete = new EventEmitter<string>();
}
```

### 7.2 依赖注入与服务

```typescript
// 📁 user.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({ providedIn: 'root' }) // 单例
export class UserService {
  constructor(private http: HttpClient) {}

  getUsers(): Observable<User[]> {
    return this.http.get<User[]>('/api/users');
  }

  deleteUser(id: string): Observable<void> {
    return this.http.delete<void>(`/api/users/${id}`);
  }
}
```

### 7.3 RxJS

```typescript
import { Observable, from, Subject, BehaviorSubject } from 'rxjs';
import { map, filter, debounceTime, switchMap, catchError } from 'rxjs/operators';

// Subject — 多播
const subject = new Subject<number>();
subject.subscribe(v => console.log('A:', v));
subject.subscribe(v => console.log('B:', v));
subject.next(1); // A:1, B:1

// BehaviorSubject — 带初始值
const state = new BehaviorSubject<string>('idle');
state.subscribe(v => console.log('state:', v)); // 立即收到 'idle'

// switchMap — 防抖+取消前一个请求
this.searchInput.valueChanges.pipe(
  debounceTime(300),
  switchMap(term => this.api.search(term)),
  catchError(err => of([]))
).subscribe(results => this.results = results);
```

### 7.4 Standalone Components

Angular 15+ 推荐使用 Standalone 模式替代 NgModules：

```typescript
// app.config.ts — 应用配置
import { ApplicationConfig } from '@angular/core';
import { provideRouter } from '@angular/router';
import { provideHttpClient } from '@angular/common/http';

export const appConfig: ApplicationConfig = {
  providers: [
    provideRouter([
      { path: '', redirectTo: '/home', pathMatch: 'full' },
      { path: 'home', loadComponent: () => import('./home.component') },
    ]),
    provideHttpClient(),
  ],
};
```

| 特性 | NgModules | Standalone |
|------|-----------|------------|
| 模块声明 | 需要 NgModule | 不需要 |
| 惰性加载 | 通过模块 | 通过 `loadComponent` |
| 学习曲线 | 陡峭 | 平缓 |
| 推荐 | 遗留项目 | 新项目 |

---

## 八、构建工具

### 8.1 Vite

```bash
# 创建项目
npm create vite@latest my-project -- --template react-ts
cd my-project && npm install
npm run dev    # 开发服务器（HMR 极快）
npm run build  # 生产构建（Rollup）
npm run preview # 预览构建结果
```

**核心优势：**

- 开发阶段使用 ESBuild（Go 编写），比 Webpack 快 10-100x
- 原生 ESM + HMR，无需打包即可热更新
- 生产构建使用 Rollup，Tree Shaking 极佳
- TypeScript 天然支持（仅编译，不校验）

### 8.2 Webpack

```javascript
// webpack.config.js
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  mode: 'production',
  entry: './src/index.js',
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: '[name].[contenthash].js',
    clean: true,
  },
  module: {
    rules: [
      { test: /\.tsx?$/, use: 'ts-loader', exclude: /node_modules/ },
      { test: /\.css$/, use: ['style-loader', 'css-loader', 'postcss-loader'] },
      { test: /\.(png|svg|jpg|webp)$/, type: 'asset/resource' },
    ],
  },
  plugins: [new HtmlWebpackPlugin({ template: './public/index.html' })],
  optimization: {
    splitChunks: { chunks: 'all' },   // 代码分割
    usedExports: true,                // Tree Shaking
  },
};
```

### 8.3 Babel

```json
// babel.config.json
{
  "presets": [
    ["@babel/preset-env", {
      "targets": "> 0.5%, not dead",
      "useBuiltIns": "usage",
      "corejs": 3
    }],
    "@babel/preset-react",
    "@babel/preset-typescript"
  ],
  "plugins": [
    "@babel/plugin-transform-runtime"
  ]
}
```

### 8.4 包管理器对比

| 特性 | npm | yarn | pnpm |
|------|-----|------|------|
| 安装速度 | 慢 | 中 | 快（硬链接 + 全局存储） |
| 磁盘占用 | 高（每个项目重复） | 高 | 低（去重） |
| Workspaces | ✅ | ✅ | ✅ （原生支持最好） |
| 锁文件 | `package-lock.json` | `yarn.lock` | `pnpm-lock.yaml` |
| 严格模式 | ❌ | ✅ | ✅（不可访问未声明的依赖） |
| 推荐场景 | 通用 | 兼容性要求 | 新项目、Monorepo |

---

## 九、性能优化

### 9.1 Core Web Vitals

| 指标 | 全称 | 衡量 | 良好 | 需改善 | 差 |
|------|------|------|------|--------|-----|
| **LCP** | Largest Contentful Paint | 最大内容加载时间 | ≤2.5s | ≤4.0s | >4.0s |
| **FID** | First Input Delay | 首次输入延迟 | ≤100ms | ≤300ms | >300ms |
| **CLS** | Cumulative Layout Shift | 累计布局偏移 | ≤0.1 | ≤0.25 | >0.25 |

**优化策略：**

```html
<!-- LCP：预加载关键资源 -->
<link rel="preload" href="/fonts/Inter.woff2" as="font" crossorigin />
<link rel="preload" href="/images/hero.webp" as="image" />

<!-- CLS：为图片预留空间 -->
<img src="hero.webp" width="1200" height="600" alt="" />
```

### 9.2 懒加载与代码分割

```javascript
// 路由级代码分割（React）
const Dashboard = React.lazy(() => import('./Dashboard'));
const Settings = React.lazy(() => import('./Settings'));

// 图片懒加载
<img loading="lazy" src="large-image.webp" alt="" />

// 组件懒加载（Intersection Observer）
function LazyImage({ src, alt }) {
  const imgRef = useRef(null);
  const [loaded, setLoaded] = useState(false);

  useEffect(() => {
    const observer = new IntersectionObserver(([entry]) => {
      if (entry.isIntersecting) {
        setLoaded(true);
        observer.disconnect();
      }
    });
    if (imgRef.current) observer.observe(imgRef.current);
    return () => observer.disconnect();
  }, []);

  return <div ref={imgRef}>{loaded && <img src={src} alt={alt} />}</div>;
}
```

### 9.3 图片优化

```html
<!-- 响应式图片 + WebP -->
<picture>
  <source srcset="hero-1920.webp 1920w, hero-1280.webp 1280w, hero-640.webp 640w"
          sizes="(max-width: 768px) 100vw, 80vw"
          type="image/webp" />
  <img src="hero-1280.jpg"
       srcset="hero-1920.jpg 1920w, hero-1280.jpg 1280w, hero-640.jpg 640w"
       sizes="(max-width: 768px) 100vw, 80vw"
       alt="横幅" width="1200" height="600" />
</picture>

<!-- 渐进式加载（低质量占位图） -->
<style>
.blur-up {
  filter: blur(10px);
  transition: filter 0.4s;
}
.blur-up.loaded {
  filter: blur(0);
}
</style>
```

### 9.4 打包分析

```bash
# Vite 分析
npm run build && npx vite-bundle-analyzer

# Webpack 分析
npm run build -- --profile --json > stats.json
npx webpack-bundle-analyzer stats.json

# Rollup 分析
npm run build
npx rollup-plugin-visualizer ./dist/stats.html
```

**Tree Shaking 条件：**

- 使用 ESM 模块语法（`import` / `export`）
- 避免导入整个库（`import { debounce } from 'lodash-es'` 而非 `import _ from 'lodash'`）
- 副作用标记：`package.json` 中 `"sideEffects": false`

### 9.5 缓存策略

**Service Worker（Workbox）：**

```javascript
// service-worker.js
import { precacheAndRoute } from 'workbox-precaching';
import { registerRoute } from 'workbox-routing';
import { StaleWhileRevalidate, CacheFirst } from 'workbox-strategies';

// 预缓存静态资源
precacheAndRoute(self.__WB_MANIFEST);

// 运行时缓存 — 图片优先使用缓存
registerRoute(
  ({ request }) => request.destination === 'image',
  new CacheFirst({ cacheName: 'images', plugins: [] })
);

// API 请求 — 缓存后更新
registerRoute(
  ({ url }) => url.pathname.startsWith('/api/'),
  new StaleWhileRevalidate({ cacheName: 'api-cache' })
);
```

**HTTP 缓存：**

```nginx
# Nginx 配置
location /static/ {
  expires 1y;
  add_header Cache-Control "public, immutable";
}

location /api/ {
  add_header Cache-Control "no-cache";  # 需验证
}
```

---

## 总结

前端开发是一个多技术栈、高迭代的领域。扎实掌握 HTML 语义化、CSS 布局与动画、JavaScript 异步与原型机制，是进阶框架学习的基石。TypeScript 提供了类型安全保障，React/Vue/Angular 各有适用场景。现代构建工具 Vite 正在取代 Webpack 成为主流选择。性能优化应贯穿开发全过程，从 Core Web Vitals 到资源加载策略，每一层都对用户体验产生直接影响。

建议学习路径：**HTML+CSS → JavaScript 核心 → TypeScript → 框架（选一深入学习） → 构建工具 → 性能优化**。保持代码整洁、重视测试、持续跟进 ECMAScript 和框架生态的演进，是前端工程师长期成长的关键。


## 十、底层原理：浏览器与 JavaScript 引擎

前端性能问题的根因大多不在框架层，而在浏览器内核与语言运行时。本节从渲染管线、关键渲染路径、V8 执行模型、事件循环、内存管理与 HTTP 协议演进六个维度，揭示"页面为什么慢、卡顿从哪来"的底层机理。

### 10.1 浏览器渲染管线

浏览器将 HTML/CSS 转化为屏幕像素，经历五个阶段：

```
 HTML字节流         CSS字节流
     │                 │
     ▼                 ▼
 ┌─────────┐      ┌─────────┐
 │HTML解析器│      │CSS解析器 │
 └────┬────┘      └────┬────┘
      ▼                 ▼
   ┌─────┐          ┌─────┐
   │ DOM │          │CSSOM│
   └──┬──┘          └──┬──┘
      └───────┬────────┘
              ▼
   ┌───────────────────┐
   │ 渲染树 RenderTree  │ 合并 DOM+CSSOM，剔除 display:none
   └─────────┬─────────┘
             ▼
   ┌───────────────────┐
   │ 布局 Layout(Reflow)│ 计算几何：盒模型/位置/尺寸
   └─────────┬─────────┘
             ▼
   ┌───────────────────┐
   │ 绘制 Paint        │ 填充像素：颜色/边框/阴影
   └─────────┬─────────┘
             ▼
   ┌───────────────────┐
   │ 合成 Composite    │ 分层→GPU栅格化→合成帧
   └─────────┬─────────┘
             ▼
          屏幕像素
```

样式变更按"失效范围"分级处理，代价逐级递减：

| 变更类型 | 触发阶段 | 代价 |
|----------|----------|------|
| 几何属性（`width`/`font-size`）、DOM 增删、读取 `offsetWidth` | Layout→Paint→Composite | 最高（reflow） |
| 视觉属性（`color`/`background`） | Paint→Composite | 中（repaint） |
| `transform`/`opacity` | 仅 Composite | 最低 |

**reflow/repaint 的底层成因：**

- **reflow**：布局是全局性的——元素几何变化通过"脏标记"（dirty bit）沿包含块向上传播，波及祖先与整棵子树；更隐蔽的是**强制同步布局**：样式变更未生效时读取 `offsetHeight`、`getBoundingClientRect()` 等，浏览器被迫立即执行一次未排队的布局，写-读-写抖动可在一帧内多次 reflow。
- **repaint**：仅重绘像素、不重算几何，但仍占用主线程。
- **仅合成**：`transform`/`opacity` 不改文档流几何，配合 `will-change: transform` 提升为独立合成层后，动画完全交给 GPU 合成线程——这是"动画只用 transform"的底层依据。

> **核心思想**：性能优化的本质是让样式变更尽量落在代价更低的管线阶段——能用合成解决就不用绘制，能用绘制解决就不用布局。

**小结**：渲染管线是"解析→布局→绘制→合成"的流水线；reflow 源于几何失效的全局传播与强制同步布局，repaint 只重绘不重排，合成层把动画卸载到 GPU。

### 10.2 关键渲染路径与核心性能指标

关键渲染路径（Critical Rendering Path）指浏览器从收到 HTML 到首次绘制所需的最短资源序列：

```
HTML ──> 解析 ──┐
CSS  ──> 解析 ──┼──> 渲染树 ──> 布局 ──> 绘制 ──> FCP
JS   ──> 执行(阻塞解析) ──┘
   <script> = 解析器阻塞资源；<link rel="stylesheet"> = 渲染阻塞资源
```

资源就绪顺序直接决定用户可感知的指标：

| 阶段产物 | 对应指标 | 主要阻塞因素 | 关键优化 |
|----------|----------|--------------|----------|
| 首次绘制任何内容 | **FCP** | JS 阻塞 HTML/CSS 解析 | 内联关键 CSS、`defer`/`async` |
| 最大内容元素呈现 | **LCP** | 关键图片/字体加载时延 | `preload`、`preconnect`、SSR 首屏 |
| 首屏后的布局位移 | **CLS** | 无尺寸图片、动态插入、字体 FOIT | 预留宽高、`font-display: swap` |

三者对应 CRP 的不同环节：**FCP 取决于解析与首绘**，**LCP 取决于关键资源何时就绪**，**CLS 发生在首绘之后**——迟到内容挤占已布局区域，浏览器被迫二次 reflow。

> **核心思想**：Core Web Vitals 不是抽象分数，而是关键渲染路径上三个环节的量化投影——优化指标就是缩短对应环节的耗时。

**小结**：FCP 看解析、LCP 看关键资源、CLS 看绘制后的布局稳定性，优化手段应精确命中对应环节。

### 10.3 JavaScript 引擎执行模型（以 V8 为例）

V8 采用"解释器先行 + JIT 后补"的两级执行架构：

```
 源码 ──> Parser ──> AST ──> Ignition(解释器) ──> 字节码
                                   │ 类型反馈        │ 热点函数
                                   ▼                ▼
                            Profiler ──────> TurboFan(JIT 编译器)
                                                  │
                                                  ▼
                                          优化机器码 ──类型假设失效──> 去优化，回退字节码
```

**解释 vs JIT 的权衡：**

| 执行方式 | 启动速度 | 峰值性能 | 内存 | 适用 |
|----------|----------|----------|------|------|
| 纯解释（Ignition） | 快（无需编译） | 低（逐条解释） | 低 | 冷代码、启动阶段 |
| JIT（TurboFan） | 慢（编译开销） | 高（执行机器码） | 高 | 反复调用的热函数 |

JIT 的前提是**类型稳定**：TurboFan 依据 Profiler 的类型反馈做激进优化（如把属性访问编译为固定偏移的读内存指令），一旦类型与假设不符只能**去优化**回退字节码。由此引出两个核心机制：

- **隐藏类（Hidden Class / Map）**：V8 为对象记录"属性名→偏移量"映射（对象形状），同构对象共享同一 Map，属性访问即"按固定偏移读内存"。但 `obj.newProp = x` 会创建新 Map 并迁移对象，破坏共享——故应在构造函数中一次性定型属性。
- **内联缓存（Inline Cache，IC）**：属性访问指令首次执行时缓存"接收者 Map→偏移量"；持续命中同一 Map（单态）近乎零成本，多形状混用退化为多态/超态走慢路径。

> **核心思想**：V8 用解释器保启动速度、JIT 保峰值性能，其优化建立在类型稳定之上；隐藏类与内联缓存把动态语言的属性访问"静态化"，动态加属性、类型漂移会触发去优化。

**小结**：V8 的两级执行是"启动快"与"跑得快"的权衡产物；保持对象形状稳定是让 JIT 优化生效的前提，否则一切优化归零。

### 10.4 事件循环：宏任务与微任务

JavaScript 单线程，异步靠事件循环调度调用栈与两个队列：

```
        ┌──────────────── 事件循环（每轮迭代）────────────────┐
        │                                                     │
        │   ┌──────────┐   栈空时     ┌───────────────────┐    │
        │   │ 调用栈    │ ◄────────── │ 微任务队列(排空式)  │    │
        │   │Call Stack│             │ Promise.then 等    │    │
        │   └────┬─────┘             └───────────────────┘    │
        │        │                      ▲ 每轮清空全部          │
        │        ▼                      │                     │
        │   ┌──────────────────────┐    │                     │
        │   │ 宏任务队列(每轮取一个)  │────┘                     │
        │   │ setTimeout/I/O/事件   │                          │
        │   └──────────────────────┘                          │
        │   ── 渲染机会(rAF→样式/布局/绘制) 通常每帧一次          │
        └─────────────────────────────────────────────────────┘
```

**优先级**：调用栈为空 → **清空整个微任务队列** → 取一个宏任务 → 重复。微任务恒优先于宏任务，且每个回调结束都有微任务检查点（microtask checkpoint）。

**async/await 的底层实现**：`async` 函数体被编译为状态机（基于生成器），`await` 处挂起；`await expr` 等价于 `Promise.resolve(expr).then(续体)`，续体注册为**微任务**。因此 `await` 之后的代码必然在当前宏任务内的微任务阶段执行，不先于同阶段的 Promise 回调。

```javascript
console.log('1');                          // 同步
setTimeout(() => console.log('2'), 0);     // 宏任务 A
Promise.resolve().then(() => {             // 微任务 ①
  console.log('3');
  Promise.resolve().then(() => console.log('4')); // 微任务 ②
});
console.log('5');                          // 同步

// 预期输出（按序）：
// 1
// 5    ← 同步代码执行完，调用栈清空
// 3    ← 清空微任务队列：① 执行
// 4    ← ① 内注册的 ② 在本轮继续执行（排空式）
// 2    ← 最后才取出宏任务 A
```

> **核心思想**：`setTimeout(fn, 0)` 只能保证"至少延迟 0ms"，无法保证先于已排队的微任务——微任务队列排空式执行，宏任务队列取一进一。

**小结**：事件循环 = 调用栈 + 宏任务队列 + 微任务队列；async/await 是 Promise 微任务的语法糖，其续体在微任务阶段执行，这是判断异步执行顺序的基石。

### 10.5 内存管理：栈、堆与分代回收

**栈 vs 堆：**

| 维度 | 栈（Stack） | 堆（Heap） |
|------|-------------|------------|
| 存放 | 原始值、调用帧、局部变量、指针 | 对象、闭包捕获的引用类型 |
| 分配/释放 | 入栈/出栈，LIFO，零开销 | 由 GC 回收，有开销 |
| 生命周期 | 随函数调用自动结束 | 由可达性决定，不确定 |

**可达性分析**：GC 从根（Roots：全局对象、调用栈变量、闭包、DOM 引用）出发沿引用遍历，被触及者为"可达"（存活），其余即垃圾。**标记-清除**（Mark-Sweep）先标记可达对象再清除未标记者，碎片化严重时配合**标记-整理**（Mark-Compact）移动对象消除空洞；代价是需要"停止世界"（Stop-the-World）暂停应用。

**V8 分代回收**——基于"大部分对象朝生夕死"的弱分代假设：

```
 新生代 New Space(半空间复制)                  老生代 Old Space
┌───────────────────────────┐  存活2次/超限  ┌───────────────────────────┐
│ From ──Scavenger复制──► To │ ────────────► │ 标记-清除/标记-整理          │
│ 频繁 Minor GC，暂停极短     │    晋升       │ 低频 Major GC，暂停较长      │
└───────────────────────────┘               └───────────────────────────┘
```

- **新生代**：Cheney 半空间复制算法，在 From/To 间拷贝存活对象，存活者晋升老生代；Minor GC 频繁但极快。
- **老生代**：标记-清除/标记-整理；Major GC 低频但会 Stop-the-World，是长任务（Long Task）的潜在来源，增量标记正是为摊薄其暂停而设计。

**常见泄漏源**：全局变量/闭包意外持有、未解绑的事件监听器、游离 DOM 节点（JS 持有但已移除）、未清理的定时器。GC 无法回收"可达但无用"的对象——**泄漏的本质是可达性错误**，而非 GC 失效。

**小结**：栈管生命周期、堆管对象存储，GC 以根可达性判定生死；V8 用新生代高频小回收 + 老生代低频大回收摊平暂停，前端内存优化的核心是避免让无用对象保持可达。

### 10.6 HTTP 协议演进

HTTP 的每次版本跃迁都针对上一代的特定瓶颈：

```
HTTP/1.1              HTTP/2                  HTTP/3
─────────             ──────                  ──────
文本协议               二进制分帧(帧/消息/流)    基于 QUIC(承载于 UDP)
keep-alive 复用连接    单连接多路复用            Connection ID 连接迁移
队头阻塞: 请求排队      消除 HTTP 层队头阻塞      消除 TCP 层队头阻塞
头部冗余无压缩          HPACK 头部压缩           QPACK(适配乱序)
```

| 维度 | HTTP/1.1 | HTTP/2 | HTTP/3 |
|------|----------|--------|--------|
| 传输层 | TCP（一连接一请求） | TCP + 二进制分帧层 | QUIC（UDP + 内置 TLS 1.3） |
| 多路复用 | 无（约 6 条连接上限） | 单连接内流级复用 | 单连接内流级复用 |
| 队头阻塞 | 连接级：响应不完成后续全堵 | 无 HTTP 层阻塞，但 TCP 丢包重传仍阻塞后续流 | 无：丢包只影响所在流 |
| 头部压缩 | 无 | HPACK（静态/动态表 + Huffman） | QPACK（容忍乱序） |
| 连接建立 | TCP 握手（+TLS） | 同左 | 0-RTT 恢复 |
| 解决的问题 | keep-alive 复用连接、管线化（FIFO 限制未普及） | 队头阻塞 + 头部冗余 | TCP 队头阻塞 + 连接迁移 + 握手延迟 |

- **HTTP/1.1 痛点**：请求-响应严格串行，一个连接上一次只有一个在途请求（队头阻塞）；浏览器只能靠多开连接硬扛；每次请求重复发送完整头部。
- **HTTP/2 解法**：二进制分帧把数据切为帧，交错复用在同一 TCP 连接的多条流上；HPACK 用索引表压缩头部。但**未消除 TCP 层队头阻塞**——底层丢包重传时，后续所有流都要等待。
- **HTTP/3 解法**：QUIC 跑在 UDP 上，把"可靠传输 + 有序交付"下沉到每条流内部，丢包只阻塞该流；连接 ID 使网络切换（Wi-Fi→蜂窝）不中断；0-RTT 降低首屏延迟。

> **核心思想**：协议演进的本质是"解除串行依赖"——HTTP/2 解除请求间的串行，HTTP/3 解除流间共享 TCP 状态的耦合；HTTP/2 下应合并小文件（头部压缩使代价降低），HTTP/3 下更关注首字节延迟与连接迁移。

**小结**：HTTP/1.1 受制于串行与头部冗余，HTTP/2 以二进制分帧 + HPACK 解决但残留 TCP 队头阻塞，HTTP/3 借 QUIC/UDP 彻底解耦流间依赖并降低握手延迟——优化策略应随协议能力演进。

---

## 十节小结

底层原理决定上层优化的天花板：渲染管线解释动画为何用 `transform`，事件循环解释异步顺序为何如此，V8 解释为何"对象形状稳定"能快一个数量级，分代 GC 解释长任务从哪来，HTTP 演进解释资源加载策略为何随协议调整。掌握这些机制，前端优化才能从"背口诀"升级为"按机理推导"。
