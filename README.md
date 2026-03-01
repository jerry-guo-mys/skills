# OpenClaw Skills

🚀 专业的 AI 编程助手技能集合 - 代码分析、文档改进、PPT 生成

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Skill-green.svg)](https://docs.openclaw.ai)
[![Cursor](https://img.shields.io/badge/Cursor-Compatible-purple.svg)](https://cursor.sh)
[![Claude](https://img.shields.io/badge/Claude-Compatible-orange.svg)](https://claude.ai)
[![Stars](https://img.shields.io/github/stars/jerry-guo-mys/skills)](https://github.com/jerry-guo-mys/skills)

> 支持 **Cursor** | **Claude** | **OpenClaw** | **opencode** 等 AI 编程助手

---

## 📋 技能总览

| 技能 | 功能 | 版本 |
|------|------|------|
| 🎯 [code-analyzer](#-code-analyzer-旗舰技能) | 深度代码分析、架构识别、DDD 分析 | v1.0.0 |
| 📝 [docs-improver](#-docs-improver-旗舰技能) | 文档质量评估、生成、改进 | v1.0.0 |
| 🎨 [ppt-generator](#-ppt-generator-旗舰技能) | HTML 演示文稿生成、12 种幻灯片类型 | v2.1.0 |

### 平台兼容性

| 平台 | 安装方式 | 使用方式 |
|------|----------|----------|
| **Cursor** | 克隆到本地 + .cursor/rules 配置 | @技能名 对话调用 |
| **Claude** | 上传 SKILL.md 或 Project Knowledge | 提示词调用 |
| **OpenClaw** | openclaw.json 配置 | @技能名 或命令行 |
| **opencode** | config.yaml 配置 | /skill 命令或内联 |

👉 [详细安装和使用说明](#️-在不同-ai-助手中使用)

---

## 📦 已发布的 Skills

### 🎯 code-analyzer (旗舰技能)

**深度代码分析工具 - 理解任何代码库的架构、业务逻辑和领域模型**

[![Version](https://img.shields.io/badge/version-1.0.0-blue)](https://github.com/jerry-guo-mys/skills/tree/main/code-analyzer)
[![Size](https://img.shields.io/github/languages/code-size/jerry-guo-mys/skills/code-analyzer)](https://github.com/jerry-guo-mys/skills/tree/main/code-analyzer)

#### 核心功能

| 分析维度 | 描述 |
|----------|------|
| 🏗️ **架构分析** | 架构风格识别、层次划分、模块组织 |
| 🚀 **执行流程** | 入口点识别、调用图、执行路径追踪 |
| 💧 **数据流** | 数据源→目的地、转换、触发器 |
| 📜 **业务规则** | 验证逻辑、业务约束、工作流提取 |
| 🔗 **外部依赖** | 第三方库、API、数据库、关键性评估 |
| 📊 **数据模型** | 实体、DTO、值对象、关系映射 |
| 🏛️ **DDD 分析** | 聚合根、实体、值对象、领域服务、仓储、领域事件、限界上下文 |
| 📈 **质量评分** | 可维护性、可测试性、文档、复杂度 |
| 💡 **改进建议** | 快速获胜、短期、长期路线图 |

#### 支持语言

- ✅ **深度支持**: Python, JavaScript, TypeScript, Rust
- ⚙️ **基础支持**: Java, Go, C/C++, C#, Ruby, PHP, Swift

#### 快速开始

```bash
# 完整深度分析
python3 code-analyzer/scripts/analyze.py --path /path/to/project --output report.md

# DDD 专项分析
python3 code-analyzer/scripts/ddd-analyzer.py --path /path/to/project --output ddd-report.md

# 排除特定目录
python3 code-analyzer/scripts/analyze.py --path . --exclude "node_modules,vendor,target" --output report.md
```

#### 输出示例

```markdown
# 🔍 Deep Code Analysis Report

## Executive Summary
- Total Files: 105
- Total Lines: 24,780
- Architecture: Layered
- Entry Points: 5
- Data Models: 45
- Business Rules: 23

## Quality Metrics
| Metric | Score | Status |
|--------|-------|--------|
| Maintainability | 75/100 | 👍 |
| Testability | 82/100 | ✅ |
| Documentation | 68/100 | ⚠️ |
| Complexity | 71/100 | 👍 |
```

#### 适用场景

1. **新项目熟悉** - 快速理解代码库结构和业务逻辑
2. **架构文档生成** - 自动生成架构文档
3. **代码审查准备** - 识别潜在问题和改进点
4. **技术债务评估** - 量化技术债务和优先级
5. **知识传承** - 记录系统核心逻辑
6. **DDD 模式识别** - 发现领域模型和模式

📖 **[完整文档](code-analyzer/SKILL.md)**

---

### 📝 docs-improver (旗舰技能)

**专业技术文档提升工具 - 评估、生成、改进技术文档**

[![Version](https://img.shields.io/badge/version-1.0.0-blue)](https://github.com/jerry-guo-mys/skills/tree/main/docs-improver)
[![Size](https://img.shields.io/github/languages/code-size/jerry-guo-mys/skills/docs-improver)](https://github.com/jerry-guo-mys/skills/tree/main/docs-improver)

#### 核心功能

| 功能模块 | 描述 |
|----------|------|
| 📊 **质量评估** | 完整性、准确性、清晰度、结构化、可维护性 5 维度评分 |
| 📝 **文档生成** | README、API 文档、架构文档自动生成 |
| 🔍 **一致性检查** | API 文档 vs 代码、示例代码 vs 实际代码、链接检查 |
| 💡 **改进建议** | 分优先级推荐（快速获胜、短期、长期） |
| 📋 **文档模板** | 6+ 专业文档模板（README、API、架构、ADR 等） |
| 🎨 **图表模板** | 10+ Mermaid 图表模板（架构图、流程图、序列图等） |
| 📚 **风格指南** | 技术文档写作风格指南 |
| 📖 **最佳实践** | 行业文档最佳实践 |

#### 使用示例

```bash
# 完整流程：分析 + 生成 + 检查 + 改进
python3 docs-improver/scripts/docs-improver.py --path /path/to/project --mode all --report report.md

# 仅质量评估
python3 docs-improver/scripts/analyze.py --path /path/to/project --output quality.md

# 仅文档生成
python3 docs-improver/scripts/generate.py --path /path/to/project --type readme

# 仅一致性检查
python3 docs-improver/scripts/consistency-check.py --path /path/to/project --output issues.md

# 仅改进建议
python3 docs-improver/scripts/improve.py --path /path/to/project --output plan.md
```

#### 输出示例

```markdown
# 📊 Documentation Quality Report

## Overall Score: 88/100 ✅

| Dimension | Score | Status |
|-----------|-------|--------|
| Completeness | 80/100 | ✅ Good |
| Clarity | 100/100 | ✅ Good |
| Structure | 85/100 | ✅ Good |
| Maintainability | 100/100 | ✅ Good |

## Recommendations

### Quick Wins (Hours)
- [ ] Add project description and badges
- [ ] Add code examples

### Short Term (Days)
- [ ] Create API documentation
- [ ] Add architecture diagram
```

#### 适用场景

1. **文档质量审计** - 评估现有文档质量
2. **缺失文档生成** - 自动生成 README、API 文档等
3. **文档一致性检查** - 确保文档与代码一致
4. **文档改进规划** - 获得专业改进建议
5. **新项目文档** - 快速建立完整文档体系
6. **发布前检查** - 确保文档质量

📖 **[完整文档](docs-improver/SKILL.md)**

---

### 🎨 ppt-generator (旗舰技能)

**专业级 HTML 演示文稿生成工具 - 炫酷科技感 PPT**

[![Version](https://img.shields.io/badge/version-2.1.0-blue)](https://github.com/jerry-guo-mys/skills/tree/main/ppt-generator)

#### 核心功能

| 功能 | 描述 |
|------|------|
| 📐 **12 种幻灯片** | title, list, grid, quote, code, mermaid, timeline, stats 等 |
| 🎨 **6 种主题** | dark, light, ocean, forest, sunset, mono |
| ✨ **6 种风格** | default, minimal, gradient, neon, corporate, playful |
| 📋 **4 种模板** | 技术分享、产品发布、培训课程、项目汇报 |
| 💻 **代码高亮** | Prism.js 支持 15+ 编程语言 |
| 📊 **Mermaid 图表** | 流程图、时序图、类图、甘特图等 |
| ✨ **分步显示** | fragments 逐个显示列表项 |
| 📝 **演讲者笔记** | 按 S 键查看笔记 |
| 🖨️ **PDF 导出** | 打印样式优化 |

#### 快速开始

```bash
# 使用模板
cp ppt-generator/examples/templates/tech-talk.json my-ppt.json

# 编辑 JSON（替换 {{占位符}}）

# 生成 PPT
python3 ppt-generator/scripts/generate-ppt.py -c my-ppt.json -o output/my-ppt.html
```

#### 输出示例

生成带有神经网络粒子背景、玻璃拟物卡片的炫酷 HTML 演示文稿，支持：
- ⌨️ 键盘控制（方向键/空格）
- 🖱️ 鼠标点击翻页
- 📱 触摸滑动（移动端）
- 🎮 快捷键（O 概览、S 笔记、T 计时器）

📖 **[完整文档](ppt-generator/SKILL.md)** | **[使用指南](ppt-generator/USAGE.md)**

---

## 🚀 安装方法

### 方法 1: 克隆仓库（推荐）

```bash
git clone https://github.com/jerry-guo-mys/skills.git ~/.openclaw/skills
```

### 方法 2: 下载单个 Skill

```bash
# 下载 code-analyzer
curl -L https://github.com/jerry-guo-mys/skills/raw/main/code-analyzer.skill \
  -o ~/.openclaw/skills/code-analyzer.skill

# 下载 docs-improver
curl -L https://github.com/jerry-guo-mys/skills/raw/main/docs-improver.skill \
  -o ~/.openclaw/skills/docs-improver.skill
```

### 方法 3: 使用 ClawHub

```bash
# 安装 clawhub
npm install -g clawhub

# 同步 skills
clawhub sync
```

---

## 🖥️ 在不同 AI 助手中使用

### 在 Cursor 中使用

**安装配置：**

1. 将 skills 仓库克隆到 Cursor 可访问的目录：

```bash
git clone https://github.com/jerry-guo-mys/skills.git ~/.openclaw/skills
```

2. 在 Cursor 项目中创建 `.cursor/rules/skills.mdc`：

```markdown
---
description: OpenClaw Skills - 代码分析、文档改进、PPT 生成
globs: ["**/*"]
alwaysApply: true
---

可用技能：
- @code-analyzer: 深度代码分析
- @docs-improver: 文档质量评估和改进
- @ppt-generator: HTML 演示文稿生成

技能目录：~/.openclaw/skills/
```

**使用示例：**

```
@code-analyzer 分析这个项目的架构

@docs-improver 评估 README.md 的质量并给出改进建议

@ppt-generator 创建一个关于微服务架构的技术分享 PPT
```

---

### 在 Claude 中使用

**方式 1：直接提供 SKILL.md 内容**

```
我有一个代码分析技能，以下是说明文档：

[粘贴 code-analyzer/SKILL.md 内容]

请使用这个技能分析我的项目...
```

**方式 2：使用 Claude Projects**

1. 创建新 Project
2. 上传 skills 文件夹作为 Project Knowledge
3. 在对话中直接使用技能

**使用示例：**

```
使用 code-analyzer 技能分析以下代码的架构：
[粘贴代码]

使用 ppt-generator 技能，帮我创建一个产品发布 PPT 的 JSON 配置：
- 主题：AI 编程助手
- 风格：neon + ocean
- 包含：产品介绍、核心功能、竞品对比、定价方案
```

**提示词模板：**

```
你是一个专业的 [代码分析师/文档专家/PPT 设计师]。

请按照以下结构生成输出：
[参考 SKILL.md 中的输出格式]

分析/生成的内容：
[用户输入]
```

---

### 在 OpenClaw 中使用

**安装配置：**

```bash
# 1. 克隆仓库
git clone https://github.com/jerry-guo-mys/skills.git ~/.openclaw/skills

# 2. 配置 openclaw.json
cat >> ~/.openclaw/openclaw.json << 'EOF'
{
  "skills": {
    "entries": {
      "code-analyzer": { "path": "~/.openclaw/skills/code-analyzer" },
      "docs-improver": { "path": "~/.openclaw/skills/docs-improver" },
      "ppt-generator": { "path": "~/.openclaw/skills/ppt-generator" }
    }
  }
}
EOF

# 3. 重启 Gateway
openclaw-cn gateway restart
```

**使用示例：**

```bash
# 命令行调用
openclaw run code-analyzer --path /path/to/project --output report.md

openclaw run docs-improver --path /path/to/project --mode all

openclaw run ppt-generator --template tech-talk --output my-ppt.html
```

**对话模式：**

```
@code-analyzer 深度分析当前项目

@docs-improver 评估并改进 README.md

@ppt-generator 使用培训课程模板创建 Python 入门教程
```

**YAML 配置调用：**

```yaml
skill: ppt-generator
action: create
params:
  template: tech-talk
  title: "微服务架构分享"
  theme: ocean
  style: neon
```

---

### 在 opencode 中使用

**安装配置：**

```bash
# 1. 克隆仓库
git clone https://github.com/jerry-guo-mys/skills.git ~/.openclaw/skills

# 2. 配置 opencode（~/.config/opencode/config.yaml）
cat >> ~/.config/opencode/config.yaml << 'EOF'
skills:
  path: ~/.openclaw/skills
  autoload: true
EOF
```

**内联命令：**

```bash
# 代码分析
opencode "使用 code-analyzer 分析 ./src 目录的架构"

# 文档改进
opencode "使用 docs-improver 评估 README.md 并生成改进建议"

# PPT 生成
opencode "使用 ppt-generator 创建一个 Docker 入门的培训 PPT"
```

**交互模式：**

```
> /skill code-analyzer
analyzer> analyze --path ./src --focus architecture
analyzer> export report.md

> /skill ppt-generator
ppt> create --template tech-talk
ppt> set title "容器化最佳实践"
ppt> set theme ocean --style neon
ppt> generate output/docker-ppt.html
```

**配置文件模式：**

创建 `.opencode/skills.yaml`：

```yaml
code-analyzer:
  default-output: ./reports
  exclude: ["node_modules", "vendor"]

ppt-generator:
  default-theme: dark
  default-style: neon
  output-dir: ./presentations
```

---

### 跨平台通用脚本

无论使用哪个 AI 助手，都可以直接运行脚本：

```bash
# 代码分析
python3 ~/.openclaw/skills/code-analyzer/scripts/analyze.py \
  --path /path/to/project \
  --output report.md

# DDD 分析
python3 ~/.openclaw/skills/code-analyzer/scripts/ddd-analyzer.py \
  --path /path/to/project \
  --output ddd-report.md

# 文档评估
python3 ~/.openclaw/skills/docs-improver/scripts/analyze.py \
  --path /path/to/project \
  --output quality.md

# PPT 生成
python3 ~/.openclaw/skills/ppt-generator/scripts/generate-ppt.py \
  --config config.json \
  --output presentation.html
```

---

## 📝 配置参考

### OpenClaw 配置

在 `~/.openclaw/openclaw.json` 中添加：

```json
{
  "skills": {
    "entries": {
      "code-analyzer": {
        "path": "~/.openclaw/skills/code-analyzer"
      },
      "docs-improver": {
        "path": "~/.openclaw/skills/docs-improver"
      },
      "ppt-generator": {
        "path": "~/.openclaw/skills/ppt-generator"
      }
    }
  }
}
```

然后重启 Gateway：

```bash
openclaw-cn gateway restart
```

### Cursor 配置

创建 `.cursor/rules/openclaw-skills.mdc`：

```markdown
---
description: OpenClaw Skills Collection
globs: ["**/*"]
alwaysApply: true
---

# 可用技能

## @code-analyzer
深度代码分析工具，支持架构分析、DDD 分析、质量评估。
路径：~/.openclaw/skills/code-analyzer/SKILL.md

## @docs-improver
文档质量评估和改进工具。
路径：~/.openclaw/skills/docs-improver/SKILL.md

## @ppt-generator
HTML 演示文稿生成工具。
路径：~/.openclaw/skills/ppt-generator/SKILL.md

使用方式：@技能名 + 任务描述
```

### opencode 配置

编辑 `~/.config/opencode/config.yaml`：

```yaml
skills:
  path: ~/.openclaw/skills
  autoload: true
  defaults:
    code-analyzer:
      exclude: ["node_modules", "vendor", ".git"]
    ppt-generator:
      theme: dark
      style: default
```

---

## 🛠️ 开发新 Skill

### 基本结构

```
skill-name/
├── SKILL.md                      # 必需 - Skill 说明
├── scripts/                      # 可选 - 可执行脚本
│   └── analyze.py
├── references/                   # 可选 - 参考文档
│   └── best-practices.md
└── assets/                       # 可选 - 资源文件
    └── templates/
```

### 创建流程

```bash
# 1. 初始化 skill
python3 ~/Documents/GitHub/openclaw/skills/skill-creator/scripts/init_skill.py my-skill --path ~/.openclaw/skills

# 2. 编辑 SKILL.md 和添加资源
# 编辑 ~/.openclaw/skills/my-skill/SKILL.md

# 3. 打包 skill
python3 ~/Documents/GitHub/openclaw/skills/skill-creator/scripts/package_skill.py ~/.openclaw/skills/my-skill

# 4. 测试 skill
# 在 OpenClaw 中使用

# 5. 提交到 Git
git add .
git commit -m "Add my-skill"
git push
```

---

## 📚 资源

### 官方文档

- [OpenClaw 文档](https://docs.openclaw.ai)
- [ClawHub](https://clawhub.com) - 发现和分享 skills
- [OpenClaw GitHub](https://github.com/openclaw/openclaw)

### 社区

- [Discord](https://discord.gg/clawd)
- [GitHub Discussions](https://github.com/openclaw/openclaw/discussions)

---

## 🤝 贡献

欢迎贡献！

### 提交新 Skill

1. Fork 本仓库
2. 创建你的 Skill (`git checkout -b feature/AmazingSkill`)
3. 提交更改 (`git commit -m 'Add AmazingSkill'`)
4. 推送到分支 (`git push origin feature/AmazingSkill`)
5. 开启 Pull Request

### 报告问题

- 使用 GitHub Issues 报告 bug
- 使用 GitHub Discussions 提问

### 改进建议

欢迎提交改进建议，特别是：
- 新语言支持
- 新的分析维度
- 性能优化
- 文档改进

---

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE)

---

## 🌟 致谢

感谢 [OpenClaw](https://github.com/openclaw/openclaw) 团队提供的优秀框架！

---

## 📊 统计

![GitHub stars](https://img.shields.io/github/stars/jerry-guo-mys/skills?style=social)
![GitHub forks](https://img.shields.io/github/forks/jerry-guo-mys/skills?style=social)
![GitHub issues](https://img.shields.io/github/issues/jerry-guo-mys/skills)
![Last Commit](https://img.shields.io/github/last-commit/jerry-guo-mys/skills)

---

**Happy Coding!** 🐱
