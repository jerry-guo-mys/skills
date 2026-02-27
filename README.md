# OpenClaw Skills

🚀 专业的代码分析和文档生成技能集合 - Professional Code Analysis & Documentation Skills for OpenClaw

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Skill-green.svg)](https://docs.openclaw.ai)
[![Stars](https://img.shields.io/github/stars/jerry-guo-mys/skills)](https://github.com/jerry-guo-mys/skills)

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

## 📝 配置

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
