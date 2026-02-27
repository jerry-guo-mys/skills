#!/usr/bin/env python3
"""
Skill Feedback Collector - Collect and manage user feedback for skills
"""

import argparse
import json
from datetime import datetime
from pathlib import Path


def collect_feedback(skill_name: str, output: str):
    """Collect feedback for a skill"""
    
    print(f"📝 收集技能反馈：{skill_name}")
    
    feedback_template = f"""# {skill_name} 使用反馈

**收集时间:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**技能版本:** v1.0  
**反馈状态:** 收集中

---

## 📋 反馈指南

请按照以下格式提供反馈：

### 问题反馈

```markdown
## 问题描述
[详细描述遇到的问题]

### 复现步骤
1. 运行命令
2. 看到输出
3. 期望输出

### 环境信息
- Python 版本：
- 操作系统：
- 技能版本：

### 影响程度
- [ ] 🔴 无法使用
- [ ] 🟡 影响效率
- [ ] 🟢 轻微影响
```

### 改进建议

```markdown
## 建议描述
[详细描述改进建议]

### 使用场景
[描述使用场景]

### 预期收益
- 效率提升：
- 用户体验：
- 覆盖范围：

### 实现难度
- [ ] 🟢 简单（<1 天）
- [ ] 🟡 中等（1-3 天）
- [ ] 🔴 复杂（>3 天）
```

---

## 📊 反馈记录

### 问题反馈

#### 反馈 #1
**提交时间:** YYYY-MM-DD  
**问题类型:** 🔴 Bug / 🟡 功能缺失 / 🟢 体验优化  
**状态:** 📝 待处理 / 🔧 处理中 / ✅ 已解决

**问题描述:**


**复现步骤:**


**影响程度:**


---

#### 反馈 #2
...

### 改进建议

#### 建议 #1
**提交时间:** YYYY-MM-DD  
**建议类型:** ✨ 新功能 / 🚀 性能优化 / 📝 文档改进  
**状态:** 📝 待评估 / ✅ 已采纳 / ❌ 不采纳

**建议描述:**


**使用场景:**


**预期收益:**


**实现难度:**


---

## 📈 统计信息

| 类型 | 数量 | 已解决 | 待处理 |
|------|------|--------|--------|
| 🔴 严重问题 | 0 | 0 | 0 |
| 🟡 主要问题 | 0 | 0 | 0 |
| 🟢 次要问题 | 0 | 0 | 0 |
| ✨ 新功能 | 0 | 0 | 0 |
| 🚀 性能优化 | 0 | 0 | 0 |
| 📝 文档改进 | 0 | 0 | 0 |

---

## 🔗 相关链接

- [技能文档](../{skill_name}/SKILL.md)
- [GitHub Issues](https://github.com/jerry-guo-mys/skills/issues)
- [改进建议](改进建议.md)
"""
    
    output_path = Path(output)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(feedback_template)
    
    print(f"✅ 反馈模板已生成：{output_path}")
    print(f"\n📋 使用说明:")
    print(f"1. 将模板分享给用户")
    print(f"2. 收集用户反馈")
    print(f"3. 运行 generate-improvements.py 生成改进建议")


def main():
    parser = argparse.ArgumentParser(description='Collect skill feedback')
    parser.add_argument('--skill', '-s', required=True, help='Skill name')
    parser.add_argument('--output', '-o', default='反馈收集.md', help='Output file')
    
    args = parser.parse_args()
    
    collect_feedback(args.skill, args.output)


if __name__ == '__main__':
    main()
