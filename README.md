# My OpenClaw Skills

个人收藏和创建的 OpenClaw skills 集合。

## 📦 已完成的 Skills

### code-analyzer ⭐
**专业的代码分析工具 - 生成带质量评分和改进建议的深度分析报告**

**核心功能：**
- 📊 质量评分（可维护性、可测试性、文档、复杂度）
- ⚠️ 问题检测（严重、主要、次要）
- 🎯 可执行的建议（快速获胜、短期、长期）
- 🏗️ 架构风格识别
- 🔄 循环依赖检测

**使用示例：**
```bash
# 完整分析报告
python3 code-analyzer/scripts/analyze.py --path /path/to/code --output report.md

# 快速概览
python3 code-analyzer/scripts/analyze.py --path /path/to/code

# 排除特定目录
python3 code-analyzer/scripts/analyze.py --path /path/to/code --exclude "node_modules,vendor"
```

**输出示例：**
```markdown
# 代码分析报告

## 执行摘要
- 综合评分：73/100
- 发现问题：5 个

## 质量指标
| 指标 | 评分 | 状态 |
|------|------|------|
| 可维护性 | 62/100 | ⚠️ 需改进 |
| 可测试性 | 89/100 | ✅ 优秀 |

## 发现的问题
### 严重
- 循环依赖：module_a → module_b → module_a

### 主要
- 高复杂度函数 calculate_score (复杂度=25)

## 改进建议
### 快速获胜（几小时）
- [ ] 添加类型注解
- [ ] 移除未使用的导入
```

**支持语言：** Python, JavaScript, TypeScript, Java, Go, Rust, C/C++, C#, Ruby, PHP, Swift 等 20+ 语言

**文件结构：**
```
code-analyzer/
├── SKILL.md                          # Skill 说明
├── scripts/
│   └── analyze.py                   # 主分析脚本（增强版）
└── references/
    └── best-practices.md            # 最佳实践指南
```

## 🚀 安装方法

### 方法 1: 克隆仓库
```bash
git clone https://github.com/jerry-guo-mys/skills.git ~/.openclaw/skills/my-skills
```

### 方法 2: 下载单个 Skill
```bash
# 下载 code-analyzer
curl -L https://github.com/jerry-guo-mys/skills/raw/main/code-analyzer.skill -o ~/.openclaw/skills/code-analyzer.skill
```

### 方法 3: 使用 clawhub (推荐)
```bash
# 安装 clawhub
npm install -g clawhub

# 同步 skills
clawhub sync
```

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

## 🛠️ 创建新 Skill

参考 [skill-creator](https://github.com/openclaw/openclaw/tree/main/skills/skill-creator) 文档。

### 基本结构
```
skill-name/
├── SKILL.md                      # 必需
├── scripts/                      # 可选
│   └── your-script.py
├── references/                   # 可选
│   └── docs.md
└── assets/                       # 可选
    └── template.html
```

### 打包 Skill
```bash
python3 package_skill.py ./skill-name
```

## 📚 资源

- [OpenClaw 文档](https://docs.openclaw.ai)
- [ClawHub](https://clawhub.com) - 发现和分享 skills
- [OpenClaw GitHub](https://github.com/openclaw/openclaw)

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License
