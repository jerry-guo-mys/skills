#!/usr/bin/env python3
"""
Feedback Analyzer - Analyze feedback data and generate insights
"""

import argparse
from datetime import datetime
from pathlib import Path
from collections import defaultdict


def analyze_feedback(feedback_files: list, output: str):
    """Analyze feedback from multiple sources"""
    
    print(f"📊 分析反馈数据...")
    
    stats = {
        'total_feedback': 0,
        'by_type': defaultdict(int),
        'by_severity': defaultdict(int),
        'by_skill': defaultdict(int),
        'by_month': defaultdict(int),
        'avg_resolution_days': 0
    }
    
    # Parse feedback files
    for file_path in feedback_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Count feedback items
            stats['total_feedback'] += content.count('## 问题描述') + content.count('## 建议描述')
            
            # Count by type
            stats['by_type']['Bug'] += content.count('🔴 Bug')
            stats['by_type']['功能缺失'] += content.count('🟡 功能缺失')
            stats['by_type']['体验优化'] += content.count('🟢 体验优化')
            stats['by_type']['新功能'] += content.count('✨ 新功能')
            stats['by_type']['性能优化'] += content.count('🚀 性能优化')
            stats['by_type']['文档改进'] += content.count('📝 文档改进')
            
            # Count by severity
            stats['by_severity']['P0'] += content.count('🔴 严重')
            stats['by_severity']['P1'] += content.count('🟡 主要')
            stats['by_severity']['P2'] += content.count('🟢 一般')
            
        except Exception as e:
            print(f"  ⚠️ 读取失败 {file_path}: {e}")
    
    # Generate analysis report
    total = max(1, stats['total_feedback'])
    
    report = f"""# 反馈数据分析报告

**分析时间:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**反馈来源:** {len(feedback_files)} 个文件  
**总反馈数:** {stats['total_feedback']} 条

---

## 📊 总体统计

### 反馈类型分布

| 类型 | 数量 | 占比 |
|------|------|------|
| **Bug** | {stats['by_type']['Bug']} | {stats['by_type']['Bug'] * 100 // total}% |
| **功能缺失** | {stats['by_type']['功能缺失']} | {stats['by_type']['功能缺失'] * 100 // total}% |
| **体验优化** | {stats['by_type']['体验优化']} | {stats['by_type']['体验优化'] * 100 // total}% |
| **新功能** | {stats['by_type']['新功能']} | {stats['by_type']['新功能'] * 100 // total}% |
| **性能优化** | {stats['by_type']['性能优化']} | {stats['by_type']['性能优化'] * 100 // total}% |
| **文档改进** | {stats['by_type']['文档改进']} | {stats['by_type']['文档改进'] * 100 // total}% |

### 严重程度分布

| 优先级 | 数量 | 占比 | 响应时间 |
|--------|------|------|----------|
| **P0 严重** | {stats['by_severity']['P0']} | {stats['by_severity']['P0'] * 100 // total}% | 24 小时 |
| **P1 重要** | {stats['by_severity']['P1']} | {stats['by_severity']['P1'] * 100 // total}% | 1 周 |
| **P2 一般** | {stats['by_severity']['P2']} | {stats['by_severity']['P2'] * 100 // total}% | 1 月 |

---

## 📈 趋势分析

### 月度反馈趋势

```
2 月 ████████████████████ {stats['total_feedback']} 条
```

### 反馈类型趋势

| 类型 | 2 月 | 趋势 |
|------|------|------|
| Bug | {stats['by_type']['Bug']} | {'↑' if stats['by_type']['Bug'] > 5 else '→'} |
| 新功能 | {stats['by_type']['新功能']} | {'↑' if stats['by_type']['新功能'] > 3 else '→'} |
| 体验优化 | {stats['by_type']['体验优化']} | {'↑' if stats['by_type']['体验优化'] > 5 else '→'} |

---

## 🎯 关键发现

### 优势
"""
    
    # Identify strengths
    if stats['by_severity']['P0'] == 0:
        report += "- ✅ 无严重 Bug，质量稳定\n"
    
    if stats['by_type']['新功能'] > stats['by_type']['Bug']:
        report += "- ✅ 新功能需求多于 Bug，产品健康发展\n"
    
    report += """
### 需改进
"""
    
    # Identify areas for improvement
    if stats['by_type']['Bug'] > 10:
        report += "- ⚠️ Bug 数量较多，需要加强质量控制\n"
    
    if stats['by_severity']['P0'] > 0:
        report += f"- 🔴 有 {stats['by_severity']['P0']} 个严重问题，需要立即处理\n"
    
    report += f"""
---

## 💡 改进建议

### 质量改进
"""
    
    if stats['by_type']['Bug'] > 5:
        report += "- [ ] 加强代码审查\n"
        report += "- [ ] 增加自动化测试\n"
        report += "- [ ] 建立 Bug 预防机制\n"
    
    report += """
### 流程改进
- [ ] 建立反馈响应 SLA
- [ ] 定期反馈分析会议
- [ ] 用户反馈闭环机制

### 产品改进
"""
    
    if stats['by_type']['新功能'] > 3:
        report += "- [ ] 评估高需求新功能\n"
        report += "- [ ] 制定产品路线图\n"
    
    report += f"""
---

## 📋 行动计划

### 本周完成
- [ ] 解决所有 P0 问题 ({stats['by_severity']['P0']}个)
- [ ] 回复所有未回复反馈
- [ ] 召开反馈分析会议

### 本月完成
- [ ] 解决 P1 问题 ({stats['by_severity']['P1']}个)
- [ ] 启动 Top3 新功能评估
- [ ] 建立反馈响应流程

### 下月计划
- [ ] Bug 数量减少 50%
- [ ] 用户满意度提升到 4.5+
- [ ] 建立自动化反馈收集

---

## 📊 数据明细

### 原始数据源
"""
    
    for file in feedback_files:
        report += f"- {file}\n"
    
    report += f"""
---

**生成工具:** skill-manager/analyze-feedback.py  
**下次分析:** 2026-03-27
"""
    
    output_path = Path(output)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"✅ 分析报告已生成：{output_path}")
    print(f"\n📊 关键指标:")
    print(f"  总反馈：{stats['total_feedback']} 条")
    print(f"  Bug: {stats['by_type']['Bug']} 个")
    print(f"  严重问题：{stats['by_severity']['P0']} 个")
    print(f"  新功能需求：{stats['by_type']['新功能']} 个")


def main():
    parser = argparse.ArgumentParser(description='Analyze feedback data')
    parser.add_argument('--files', '-f', nargs='+', required=True, help='Feedback files')
    parser.add_argument('--output', '-o', default='反馈分析报告.md', help='Output file')
    
    args = parser.parse_args()
    
    analyze_feedback(args.files, args.output)


if __name__ == '__main__':
    main()
