# OpenClaw Skills

🚀 专业的代码分析技能集合 - Professional Code Analysis Skills for OpenClaw

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Skill-green.svg)](https://docs.openclaw.ai)

---

## 📦 已发布的 Skills

### 🎯 code-analyzer (旗舰技能)

**深度代码分析工具 - 理解任何代码库的架构、业务逻辑和领域模型**

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

#### 使用示例

```bash
# 完整深度分析
python3 code-analyzer/scripts/analyze.py --path /path/to/project --output report.md

# 排除特定目录
python3 code-analyzer/scripts/analyze.py --path . --exclude "node_modules,vendor,target" --output report.md

# DDD 专项分析
python3 code-analyzer/scripts/ddd-analyzer.py --path /path/to/project --output ddd-report.md

# 快速概览
python3 code-analyzer/scripts/analyze.py --path /path/to/project
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

## Architecture
Style: Layered
Layers: api/, service/, repository/, domain/

## Entry Points
### process_message
- Location: agent.rs
- Parameters: components, context, user_input
- Business Logic: ✅ Yes

## Data Models
### Core Entities
**User** (domain/user.rs)
- Identity: id
- Methods: update_profile, change_email

### Value Objects
**Email** (common/email.rs)
- Immutable: ✅ Yes
- Attributes: value

## Business Rules
### Validation Rules (15)
**rule_1:** Validation on user input
- Location: agent.rs
- Priority: high

## Data Flows
- external → process_message
  Data: user_input
  Trigger: API call

## DDD Analysis
### Aggregates
**Order** (order/order.rs)
- Entities: OrderItem, ShippingInfo
- Value Objects: OrderId, Money, Address
- Invariants: 5

### Bounded Contexts
**Order Processing** (order/)
- Aggregates: Order, Payment, Shipping
```

#### 适用场景

1. **新项目熟悉** - 快速理解代码库结构和业务逻辑
2. **架构文档生成** - 自动生成架构文档
3. **代码审查准备** - 识别潜在问题和改进点
4. **技术债务评估** - 量化技术债务和优先级
5. **知识传承** - 记录系统核心逻辑
6. **DDD 模式识别** - 发现领域模型和模式

---

## 🚀 安装方法

### 方法 1: 克隆仓库（推荐）

```bash
git clone https://github.com/jerry-guo-mys/skills.git ~/.openclaw/skills/my-skills
```

### 方法 2: 下载单个 Skill

```bash
# 下载 code-analyzer
curl -L https://github.com/jerry-guo-mys/skills/raw/main/code-analyzer.skill \
  -o ~/.openclaw/skills/code-analyzer.skill
```

### 方法 3: 使用 ClawHub

```bash
# 安装 clawhub
npm install -g clawhub

# 同步 skills
clawhub sync
```

---

## 📝 配置

在 `~/.openclaw/openclaw.json` 中添加：

```json
{
  "skills": {
    "entries": {
      "code-analyzer": {
        "path": "~/.openclaw/skills/code-analyzer"
      }
    }
  }
}
```

然后重启 Gateway：

```bash
openclaw-cn gateway restart
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
    └── template.html
```

### 创建流程

```bash
# 1. 初始化 skill
python3 scripts/init_skill.py my-skill --path ~/.openclaw/skills

# 2. 编辑 SKILL.md 和添加资源
# 编辑 ~/.openclaw/skills/my-skill/SKILL.md

# 3. 打包 skill
python3 scripts/package_skill.py ~/.openclaw/skills/my-skill

# 4. 测试 skill
# 在 OpenClaw 中使用

# 5. 提交到 Git
git add .
git commit -m "Add my-skill"
git push
```

### SKILL.md 模板

```markdown
---
name: skill-name
description: 清晰描述 skill 的功能和使用场景。Use when: (1) 场景 1, (2) 场景 2, (3) 场景 3.
---

# Skill Name

简要说明。

## Quick Start

```bash
command example
```

## Features

- Feature 1
- Feature 2

## Usage

详细说明。
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

---

**Happy Coding!** 🐱
