# My OpenClaw Skills

个人收藏和创建的 OpenClaw skills 集合。

## 📦 已完成的 Skills

### code-analyzer
快速准确的代码分析工具。

**功能：**
- 代码库结构分析
- 依赖关系分析
- 代码复杂度计算
- 多语言支持（Python, JS/TS, Java, Go, Rust 等）

**使用示例：**
```bash
# 分析代码库结构
python3 scripts/analyze.py --path /path/to/code --mode structure

# 完整分析
python3 scripts/analyze.py --path /path/to/code --mode full --output report.md

# 分析单个文件
python3 scripts/analyze.py --file /path/to/file.py
```

**文件结构：**
```
code-analyzer/
├── SKILL.md                      # Skill 说明
├── scripts/
│   └── analyze.py               # 主分析脚本
└── references/
    └── best-practices.md        # 最佳实践指南
```

## 🚀 安装方法

### 方法 1: 克隆仓库
```bash
git clone https://github.com/YOUR_USERNAME/skills.git ~/.openclaw/skills/my-skills
```

### 方法 2: 下载单个 Skill
```bash
# 下载 code-analyzer
curl -L https://github.com/YOUR_USERNAME/skills/raw/main/code-analyzer.skill -o ~/.openclaw/skills/code-analyzer.skill
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
