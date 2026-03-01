---
name: ppt-generator
description: 专业级 HTML 演示文稿生成工具 v2.0。支持 12 种幻灯片类型、4 种主题、分步显示、演讲者笔记、代码高亮、Mermaid 图表。使用场景：技术分享、课程演示、项目汇报、会议演讲。
---

# PPT Generator v2.0 - 专业演示文稿生成

基于专业前端设计的 HTML 幻灯片生成工具，生成炫酷的科技感演示文稿。

## ✨ v2.0 新特性

| 功能 | 说明 |
|------|------|
| 🖼️ **图片展示** | `image` 类型，支持缩放、滤镜 |
| 💻 **代码高亮** | `code` 类型，Prism.js 语法高亮，支持 15+ 语言 |
| 📐 **双列布局** | `two-column` 类型，图文混排 |
| 📅 **时间线** | `timeline` 类型，里程碑展示 |
| 📊 **统计卡片** | `stats` 类型，数据可视化 |
| 🎬 **视频嵌入** | `video` 类型，本地/YouTube/Bilibili |
| ✨ **分步显示** | `fragments: true`，逐个显示列表项 |
| 📝 **演讲者笔记** | `notes` 字段 + `S` 键查看 |
| 👁️ **概览模式** | `O` 键缩略图视图 |
| ⏱️ **演讲计时** | `T` 键计时器 |
| 🎨 **主题系统** | dark/light/ocean/forest + 自定义 |
| 🖨️ **PDF 导出** | 打印样式优化 |

---

## 🚀 快速开始

### 1. 创建配置文件

```json
{
  "title": "我的演示文稿",
  "theme": {
    "preset": "dark"
  },
  "slides": [
    {
      "type": "title",
      "emoji": "🚀",
      "title": "演示标题",
      "subtitle": "副标题",
      "author": "你的名字",
      "year": "2026",
      "notes": "这是演讲者笔记，按 S 键查看"
    }
  ]
}
```

### 2. 生成 PPT

```bash
python3 scripts/generate-ppt.py \
  --config examples/v2-demo.json \
  --output output/presentation.html
```

### 3. 打开查看

```bash
# macOS
open output/presentation.html

# Windows
start output/presentation.html
```

---

## 📐 幻灯片类型（12 种）

### 1. 封面页 (title)

```json
{
  "type": "title",
  "emoji": "🚀",
  "title": "主标题",
  "subtitle": "副标题",
  "author": "作者名",
  "year": "2026",
  "notes": "演讲者笔记"
}
```

### 2. 列表页 (list)

```json
{
  "type": "list",
  "title": "页面标题",
  "fragments": true,
  "items": [
    "<span class=\"success\">✓</span> 项目 1",
    "<span class=\"error\">✗</span> 项目 2"
  ],
  "notes": "演讲者笔记"
}
```

**参数说明：**
- `fragments: true` - 逐个显示列表项

### 3. 对比页 (grid)

```json
{
  "type": "grid",
  "title": "对比标题",
  "description": "描述文字",
  "cards": [
    {
      "title": "正面标题",
      "type": "positive",
      "items": ["优点 1", "优点 2"]
    },
    {
      "title": "反面标题",
      "type": "negative",
      "items": ["缺点 1", "缺点 2"]
    }
  ]
}
```

**卡片类型：**
- `positive` - 绿色边框
- `negative` - 红色边框
- `warning` - 黄色边框
- `default` - 青色边框

### 4. 金句页 (quote)

```json
{
  "type": "quote",
  "text": "主要文字，",
  "highlight": "强调文字"
}
```

### 5. 任务页 (tasks)

```json
{
  "type": "tasks",
  "title": "行动清单",
  "fragments": true,
  "tasks": [
    {
      "title": "任务标题",
      "desc": "任务描述"
    }
  ]
}
```

### 6. 结束页 (end)

```json
{
  "type": "end",
  "title": "感谢语",
  "subtitle": "副标题",
  "author": "作者名",
  "email": "email@example.com",
  "contact": "微信/电话"
}
```

### 7. Mermaid 图表页 (mermaid)

```json
{
  "type": "mermaid",
  "title": "图表标题",
  "description": "图表描述",
  "chart": "flowchart",
  "code": "flowchart TD\n    A[开始] --> B{条件？}\n    B -->|是 | C[执行]\n    B -->|否 | D[结束]"
}
```

**支持的图表：** flowchart, sequenceDiagram, classDiagram, stateDiagram, gantt, pie, mindmap

### 8. 图片页 (image) 🆕

```json
{
  "type": "image",
  "title": "图片标题",
  "src": "https://example.com/image.jpg",
  "alt": "图片描述",
  "caption": "图片说明文字",
  "fit": "contain"
}
```

**参数说明：**
- `fit`: `contain`（默认）/ `cover` / `fill`

### 9. 代码页 (code) 🆕

```json
{
  "type": "code",
  "title": "代码标题",
  "description": "代码描述",
  "filename": "example.ts",
  "language": "typescript",
  "code": "const hello = 'world';\nconsole.log(hello);"
}
```

**支持的语言：** javascript, typescript, python, go, rust, jsx, tsx, css, sql, bash, json 等

### 10. 双列布局页 (two-column) 🆕

```json
{
  "type": "two-column",
  "title": "双列标题",
  "left": {
    "title": "左栏标题",
    "type": "list",
    "items": ["项目 1", "项目 2"]
  },
  "right": {
    "title": "右栏标题",
    "type": "code",
    "language": "python",
    "code": "print('Hello')"
  }
}
```

**栏目类型：**
- `text` - 文本内容，使用 `content` 字段
- `list` - 列表，使用 `items` 字段
- `code` - 代码，使用 `code` + `language` 字段
- `image` - 图片，使用 `src` + `alt` 字段

### 11. 时间线页 (timeline) 🆕

```json
{
  "type": "timeline",
  "title": "项目里程碑",
  "fragments": true,
  "events": [
    {
      "date": "2026-01",
      "title": "阶段一",
      "description": "完成需求分析"
    },
    {
      "date": "2026-02",
      "title": "阶段二",
      "description": "开发完成上线"
    }
  ]
}
```

### 12. 统计卡片页 (stats) 🆕

```json
{
  "type": "stats",
  "title": "核心指标",
  "description": "数据一览",
  "stats": [
    {
      "icon": "📊",
      "value": "99%",
      "label": "准确率"
    },
    {
      "icon": "⚡",
      "value": "10ms",
      "label": "响应时间"
    }
  ]
}
```

### 13. 视频页 (video) 🆕

```json
{
  "type": "video",
  "title": "视频演示",
  "src": "demo.mp4",
  "video_type": "local",
  "autoplay": false
}
```

**视频类型：**
- `local` - 本地视频文件
- `youtube` - YouTube 视频（填视频 ID 或完整链接）
- `bilibili` - B站视频（填 BV 号）

---

## 🎨 主题系统

### 内置主题

```json
{
  "theme": {
    "preset": "dark"
  }
}
```

| 主题 | 说明 |
|------|------|
| `dark` | 深色主题（默认） |
| `light` | 亮色主题 |
| `ocean` | 海洋蓝主题 |
| `forest` | 森林绿主题 |

### 自定义颜色

```json
{
  "theme": {
    "preset": "dark",
    "custom": {
      "accent-cyan": "#00ff88",
      "accent-purple": "#ff00ff"
    }
  }
}
```

**可自定义变量：**
- `bg-color-1`, `bg-color-2` - 背景色
- `accent-cyan`, `accent-green`, `accent-warning`, `accent-danger`, `accent-purple` - 强调色
- `text-main`, `text-muted` - 文字颜色

---

## 🎮 快捷键

| 操作 | 快捷键 |
|------|--------|
| 下一页 | `→` / `↓` / `空格` / `Enter` |
| 上一页 | `←` / `↑` |
| 幻灯片概览 | `O` |
| 演讲者笔记 | `S` |
| 黑屏暂停 | `B` |
| 演讲计时器 | `T` |
| 全屏模式 | `F11` |
| 快速跳转 | `1` - `9` |
| 首页 / 末页 | `Home` / `End` |

### 交互方式

| 操作 | 方式 |
|------|------|
| 鼠标点击 | 左侧 30% 上一页，右侧 30% 下一页 |
| 滚轮翻页 | 上滚上一页，下滚下一页 |
| 触摸滑动 | 左滑下一页，右滑上一页 |

---

## 📝 演讲者笔记

在任何幻灯片中添加 `notes` 字段：

```json
{
  "type": "list",
  "title": "标题",
  "items": ["..."],
  "notes": "这是演讲者笔记，只有按 S 键才能看到。可以写上要说的重点、提醒事项等。"
}
```

演示时按 `S` 键打开/关闭笔记面板。

---

## ✨ 分步显示 (Fragments)

添加 `fragments: true` 让列表项逐个显示：

```json
{
  "type": "list",
  "title": "逐个显示",
  "fragments": true,
  "items": ["第一项", "第二项", "第三项"]
}
```

支持 fragments 的类型：`list`, `tasks`, `timeline`

---

## 🖨️ PDF 导出

直接使用浏览器打印功能（Ctrl/Cmd + P）：

1. 打开生成的 HTML 文件
2. 按 `Ctrl + P` 或 `Cmd + P`
3. 选择"另存为 PDF"
4. 建议设置：横向、无边距、背景图形

---

## 📊 配置示例

| 示例 | 路径 | 说明 |
|------|------|------|
| v2.0 功能演示 | `examples/v2-demo.json` | 展示所有新功能 |
| Mermaid 演示 | `examples/mermaid-demo.json` | 图表类型示例 |
| AI 课程示例 | `examples/ai-survival-lesson1.json` | 完整课程演示 |

---

## 🎨 CSS 类名

### 文字样式

| 类名 | 效果 | HTML |
|------|------|------|
| `gradient-text` | 渐变文字 | `<h1 class="gradient-text">` |
| `highlight` | 高亮背景 | `<span class="highlight">` |
| `success` | 绿色 | `<span class="success">` |
| `error` | 红色 | `<span class="error">` |
| `warning` | 黄色 | `<span class="warning">` |

---

## 💡 最佳实践

### 内容建议
- ✅ 每页不超过 5 个要点
- ✅ 使用 fragments 控制信息节奏
- ✅ 多用图表少用字
- ✅ 添加演讲者笔记备忘

### 演示建议
- ✅ 使用 `O` 键快速预览全部幻灯片
- ✅ 使用 `T` 键开启计时器
- ✅ 提前测试全屏模式
- ✅ 准备 PDF 备用

### 技术建议
- ✅ 使用 Chrome 浏览器
- ✅ 开启硬件加速
- ✅ 图片使用网络链接或相对路径

---

## 🔗 相关链接

- [v2.0 功能演示](examples/v2-demo.json)
- [Mermaid 演示](examples/mermaid-demo.json)
- [HTML 模板](templates/ppt-template.html)
- [生成脚本](scripts/generate-ppt.py)
- [Mermaid 官方文档](https://mermaid.js.org/)
- [Prism.js 官方文档](https://prismjs.com/)

---

**🎉 开始制作你的专业演示文稿吧！** 🚀
