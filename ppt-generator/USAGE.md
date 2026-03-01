# PPT Generator 使用说明

> 适用于 Claude、OpenClaw、opencode、Cursor 等 AI 编程助手

---

## 📋 目录

- [快速开始](#-快速开始)
- [在 Cursor 中使用](#-在-cursor-中使用)
- [在 Claude 中使用](#-在-claude-中使用)
- [在 OpenClaw 中使用](#-在-openclaw-中使用)
- [在 opencode 中使用](#-在-opencode-中使用)
- [配置参考](#-配置参考)
- [常见问题](#-常见问题)

---

## 🚀 快速开始

### 基本流程

```
1. 选择模板 → 2. 编辑内容 → 3. 生成 HTML → 4. 浏览器打开
```

### 可用模板

| 模板 | 文件路径 | 适用场景 |
|------|----------|----------|
| 技术分享 | `examples/templates/tech-talk.json` | 技术大会、团队分享 |
| 产品发布 | `examples/templates/product-launch.json` | 新品发布、功能介绍 |
| 培训课程 | `examples/templates/training.json` | 企业培训、在线课程 |
| 项目汇报 | `examples/templates/project-report.json` | 周报月报、项目汇报 |

### 可用主题

| 主题 | 说明 | 推荐场景 |
|------|------|----------|
| `dark` | 深色（默认） | 技术演示 |
| `light` | 亮色 | 白天会议 |
| `ocean` | 海洋蓝 | 产品发布 |
| `forest` | 森林绿 | 环保主题 |
| `sunset` | 日落紫 | 创意展示 |
| `mono` | 黑白 | 打印友好 |

### 可用风格

| 风格 | 说明 | 视觉效果 |
|------|------|----------|
| `default` | 默认 | 平衡美观 |
| `minimal` | 简约 | 无阴影无动画 |
| `gradient` | 渐变 | 流动渐变色 |
| `neon` | 霓虹 | 发光效果 |
| `corporate` | 商务 | 专业简洁 |
| `playful` | 活泼 | 有趣动感 |

---

## 🖥️ 在 Cursor 中使用

### 方式 1：直接对话

```
@ppt-generator 帮我创建一个关于 "微服务架构" 的技术分享 PPT，
使用 ocean 主题和 neon 风格，包含以下内容：
1. 什么是微服务
2. 微服务 vs 单体架构
3. 核心组件介绍
4. 实践案例
5. 常见问题
```

### 方式 2：基于模板

```
@ppt-generator 使用 tech-talk 模板，创建一个 Python 性能优化的分享：
- 主题：Python 性能优化实战
- 演讲者：张三
- 痛点：响应慢、内存高
- 方案：缓存、异步、算法优化
- 效果：性能提升 10 倍
```

### 方式 3：手动操作

1. 打开终端
2. 执行命令：

```bash
cd /Users/g/.openclaw/skills/ppt-generator

# 复制模板
cp examples/templates/tech-talk.json my-ppt.json

# 编辑 my-ppt.json（替换 {{占位符}}）

# 生成 PPT
python3 scripts/generate-ppt.py -c my-ppt.json -o output/my-ppt.html
```

---

## 🤖 在 Claude 中使用

### 提示词模板

```
我需要你帮我创建一个演示文稿的 JSON 配置文件。

【主题】：{{你的主题}}
【场景】：{{技术分享/产品发布/培训课程/项目汇报}}
【主题风格】：{{dark/light/ocean/forest/sunset/mono}}
【视觉风格】：{{default/minimal/gradient/neon/corporate/playful}}

请按照以下 JSON 结构生成配置：

{
  "title": "演示标题",
  "theme": { "preset": "主题名" },
  "style": "风格名",
  "slides": [
    {
      "type": "title",
      "emoji": "🚀",
      "title": "主标题",
      "subtitle": "副标题",
      "author": "作者",
      "year": "2026"
    },
    // 更多幻灯片...
  ]
}

可用的幻灯片类型：
- title: 封面页
- list: 列表页（可加 "fragments": true 分步显示）
- grid: 对比卡片页
- quote: 金句页
- tasks: 任务清单页
- code: 代码展示页（需指定 language）
- mermaid: 图表页（需指定 chart 类型和 code）
- two-column: 双列布局页
- timeline: 时间线页
- stats: 统计数据页
- image: 图片展示页
- video: 视频嵌入页
- end: 结束页
```

### 示例对话

**用户：**
```
帮我创建一个 "AI 编程助手" 产品发布的 PPT 配置，使用 ocean 主题和 gradient 风格
```

**Claude 回复后，保存 JSON 文件，然后执行：**

```bash
python3 scripts/generate-ppt.py -c ai-assistant.json -o output/ai-assistant.html
open output/ai-assistant.html
```

---

## 🦎 在 OpenClaw 中使用

### 技能调用

```yaml
skill: ppt-generator
action: create
params:
  template: tech-talk
  title: "我的技术分享"
  theme: ocean
  style: neon
  content:
    topic: "微服务架构"
    author: "张三"
    sections:
      - name: "背景"
        points: ["痛点1", "痛点2"]
      - name: "方案"
        points: ["方案1", "方案2"]
```

### 命令行调用

```bash
openclaw run ppt-generator \
  --template tech-talk \
  --title "微服务架构分享" \
  --theme ocean \
  --style neon \
  --output my-presentation.html
```

### 对话模式

```
@ppt-generator 创建 PPT

主题：Kubernetes 入门指南
模板：培训课程
风格：corporate + light

章节：
1. 什么是 K8s
2. 核心概念
3. 基础操作
4. 实践练习
```

---

## 💻 在 opencode 中使用

### 内联命令

```bash
# 使用 opencode 执行
opencode "使用 ppt-generator 创建一个关于 Docker 的技术分享 PPT"
```

### 交互模式

```
> /skill ppt-generator

ppt> create --template tech-talk
ppt> set title "Docker 容器化实践"
ppt> set theme ocean
ppt> set style neon
ppt> add slide list "核心概念" --items "镜像,容器,仓库"
ppt> add slide code "Dockerfile 示例" --language dockerfile
ppt> generate output/docker-ppt.html
ppt> open
```

### 配置文件模式

创建 `.opencode/ppt-config.yaml`：

```yaml
ppt-generator:
  default-theme: dark
  default-style: neon
  output-dir: ./presentations
  auto-open: true
```

然后：

```bash
opencode ppt create "我的演示" --from-template tech-talk
```

---

## 📖 配置参考

### 完整 JSON 结构

```json
{
  "title": "演示文稿标题",
  "theme": {
    "preset": "dark",
    "custom": {
      "accent-cyan": "#00ff88"
    }
  },
  "style": "neon",
  "slides": []
}
```

### 幻灯片类型速查

#### 封面页 (title)

```json
{
  "type": "title",
  "emoji": "🚀",
  "title": "主标题",
  "subtitle": "副标题",
  "author": "作者",
  "year": "2026",
  "notes": "演讲者笔记"
}
```

#### 列表页 (list)

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

#### 代码页 (code)

```json
{
  "type": "code",
  "title": "代码标题",
  "description": "代码说明",
  "filename": "example.py",
  "language": "python",
  "code": "def hello():\n    print('Hello')"
}
```

支持语言：`javascript`, `typescript`, `python`, `go`, `rust`, `java`, `cpp`, `sql`, `bash`, `json`, `yaml`, `html`, `css`

#### Mermaid 图表 (mermaid)

```json
{
  "type": "mermaid",
  "title": "架构图",
  "description": "系统架构",
  "chart": "flowchart",
  "code": "flowchart TD\n    A[用户] --> B[服务]\n    B --> C[数据库]"
}
```

支持图表：`flowchart`, `sequenceDiagram`, `classDiagram`, `stateDiagram`, `gantt`, `pie`, `mindmap`

#### 双列布局 (two-column)

```json
{
  "type": "two-column",
  "title": "对比",
  "left": {
    "title": "左栏",
    "type": "list",
    "items": ["项目 1", "项目 2"]
  },
  "right": {
    "title": "右栏",
    "type": "code",
    "language": "python",
    "code": "print('hello')"
  }
}
```

#### 时间线 (timeline)

```json
{
  "type": "timeline",
  "title": "里程碑",
  "fragments": true,
  "events": [
    { "date": "2026-01", "title": "阶段一", "description": "完成设计" },
    { "date": "2026-03", "title": "阶段二", "description": "开发完成" }
  ]
}
```

#### 统计卡片 (stats)

```json
{
  "type": "stats",
  "title": "核心数据",
  "stats": [
    { "icon": "📊", "value": "99%", "label": "准确率" },
    { "icon": "⚡", "value": "10ms", "label": "响应时间" }
  ]
}
```

---

## 🎮 演示快捷键

| 按键 | 功能 |
|------|------|
| `→` / `空格` / `Enter` | 下一页/下一步 |
| `←` | 上一页 |
| `O` | 幻灯片概览 |
| `S` | 演讲者笔记 |
| `T` | 计时器 |
| `B` | 黑屏 |
| `1-9` | 快速跳转 |
| `Home` / `End` | 首页/末页 |
| `F11` | 全屏 |

---

## ❓ 常见问题

### Q: 如何添加图片？

```json
{
  "type": "image",
  "title": "产品截图",
  "src": "https://example.com/image.png",
  "caption": "图片说明"
}
```

### Q: 如何嵌入视频？

```json
{
  "type": "video",
  "title": "演示视频",
  "src": "demo.mp4",
  "video_type": "local"
}
```

YouTube：`"video_type": "youtube", "src": "视频ID"`

### Q: 如何自定义颜色？

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

### Q: 如何导出 PDF？

1. 打开生成的 HTML 文件
2. 按 `Ctrl+P` (Windows) 或 `Cmd+P` (Mac)
3. 选择 "另存为 PDF"
4. 设置：横向、无边距、启用背景图形

### Q: 生成报错怎么办？

```bash
# 检查 Python 版本
python3 --version  # 需要 3.8+

# 检查 JSON 格式
python3 -m json.tool my-ppt.json
```

---

## 📁 文件结构

```
ppt-generator/
├── scripts/
│   └── generate-ppt.py      # 生成脚本
├── templates/
│   └── ppt-template.html    # HTML 模板
├── examples/
│   ├── templates/           # 场景模板
│   │   ├── tech-talk.json
│   │   ├── product-launch.json
│   │   ├── training.json
│   │   └── project-report.json
│   ├── v2-demo.json
│   └── style-demo.json
├── output/                  # 生成输出目录
├── SKILL.md                 # 技能说明
└── USAGE.md                 # 本文档
```

---

## 🔗 相关资源

- [Mermaid 语法文档](https://mermaid.js.org/)
- [Prism.js 支持语言](https://prismjs.com/#supported-languages)
- [在线 Mermaid 编辑器](https://mermaid.live/)

---

**🎉 开始制作你的专业演示文稿吧！**
