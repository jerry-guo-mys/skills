#!/usr/bin/env python3
"""
Solution Optimizer - Optimize existing technical solution documents
"""

import argparse
import re
from datetime import datetime
from pathlib import Path


def evaluate_solution(content: str) -> dict:
    """Evaluate technical solution quality"""
    
    scores = {
        'completeness': 0,
        'accuracy': 0,
        'feasibility': 0,
        'clarity': 0,
        'risk_management': 0,
        'cost_control': 0
    }
    
    issues = {
        'critical': [],
        'major': [],
        'minor': []
    }
    
    # Check completeness (12 chapters)
    required_chapters = [
        '需求背景', '产品目标', '系统目标', '系统架构',
        '业务流程', '资金流程', '数据流程', '数据模型',
        'API 设计', '表设计', '影响面分析', '任务拆分'
    ]
    
    found_chapters = []
    for chapter in required_chapters:
        if chapter in content:
            found_chapters.append(chapter)
    
    scores['completeness'] = len(found_chapters) * 100 // 12
    
    if len(found_chapters) < 12:
        missing = set(required_chapters) - set(found_chapters)
        issues['critical'].append(f'缺少章节：{", ".join(missing)}')
    
    # Check diagrams
    diagram_patterns = ['```mermaid', 'graph ', 'sequenceDiagram', 'erDiagram', 'flowchart']
    has_diagrams = any(p in content for p in diagram_patterns)
    
    if not has_diagrams:
        issues['major'].append('缺少架构图表')
        scores['clarity'] -= 20
    
    # Check code examples
    if '```sql' not in content:
        issues['minor'].append('缺少 SQL 示例')
    
    if '```http' not in content and 'POST' not in content and 'GET' not in content:
        issues['minor'].append('缺少 API 示例')
    
    # Check tables
    if '|' not in content:
        issues['minor'].append('缺少表格')
    
    # Check task breakdown
    if '任务拆分' in content:
        if 'DEV-' not in content and '任务' not in content:
            issues['major'].append('任务拆分不够详细')
    
    # Calculate overall score
    scores['overall'] = sum(scores.values()) // len(scores)
    
    return {
        'scores': scores,
        'issues': issues,
        'found_chapters': found_chapters
    }


def optimize_solution(content: str, level: str = 'standard') -> str:
    """Optimize technical solution document"""
    
    print(f"🔧 开始优化技术方案文档（{level}级别）...")
    
    optimized = content
    
    # Add missing sections
    required_sections = {
        '## 1. 需求背景': '### 1.1 业务背景\n\n{{业务背景}}\n\n### 1.2 用户痛点\n\n{{用户痛点}}',
        '## 2. 产品目标': '### 2.1 核心目标\n\n1. **目标 1**\n2. **目标 2**',
        '## 3. 系统目标': '### 3.1 性能目标\n\n| 指标 | 目标 |\n|------|------|\n| 响应时间 | < 200ms |',
        '## 4. 系统架构': '### 4.1 系统上下文\n\n```mermaid\ngraph TB\n    A[用户] --> B[系统]\n```',
        '## 5. 业务流程': '### 5.1 主流程\n\n```mermaid\nflowchart TD\n    A[开始] --> B[结束]\n```',
        '## 8. 数据模型': '### 8.1 实体关系\n\n```mermaid\nerDiagram\n    ENTITY1 ||--o{ ENTITY2 : relationship\n```',
        '## 9. API 设计': '### 9.2 接口详情\n\n```http\nPOST /api/v1/resource\n```\n\n```json\n{"status": "success"}\n```',
        '## 10. 表设计': '### 10.1 表结构\n\n```sql\nCREATE TABLE table_name (\n  id bigint PRIMARY KEY\n);\n```',
        '## 12. 任务拆分': '### 12.1 开发任务\n\n| 任务 | 负责人 | 估算 |\n|------|--------|------|\n| DEV-001 | 张三 | 2 天 |'
    }
    
    for section, template in required_sections.items():
        if section not in optimized:
            print(f"  ➕ 添加缺失章节：{section}")
            # Find appropriate place to insert
            optimized += f"\n\n{section}\n\n{template}\n"
    
    # Improve existing sections
    if level in ['standard', 'deep']:
        # Add more details to architecture
        if '系统架构' in optimized and '```mermaid' not in optimized:
            print("  📊 添加架构图...")
            arch_diagram = """
```mermaid
graph TB
    subgraph Client["客户端"]
        A[Web 端]
        B[移动端]
    end
    
    subgraph Gateway["网关层"]
        C[API Gateway]
    end
    
    subgraph Service["服务层"]
        D[业务服务]
    end
    
    subgraph Data["数据层"]
        E[(数据库)]
        F[缓存]
    end
    
    A & B --> C
    C --> D
    D --> E & F
```
"""
            optimized = optimized.replace('## 4. 系统架构', f'## 4. 系统架构\n{arch_diagram}')
        
        # Add task breakdown if missing
        if '任务拆分' in optimized and '|' not in optimized.split('任务拆分')[1].split('##')[0]:
            print("  📋 添加任务拆分表格...")
            task_table = """
| 任务 ID | 任务名称 | 负责人 | 优先级 | 估算 (天) |
|---------|----------|--------|--------|-----------|
| DEV-001 | 数据库设计 | 张三 | P0 | 2 |
| DEV-002 | API 开发 | 李四 | P0 | 5 |
| DEV-003 | 前端开发 | 王五 | P1 | 5 |
| DEV-004 | 测试 | 赵六 | P0 | 3 |
"""
            optimized = optimized.replace('## 12. 任务拆分', f'## 12. 任务拆分\n{task_table}')
    
    if level == 'deep':
        # Deep optimization: restructure and enhance
        print("  🔍 深度优化：增强内容...")
        
        # Add risk assessment if missing
        if '风险' not in optimized:
            risk_section = """
## 风险评估

| 风险项 | 概率 | 影响 | 缓解措施 |
|--------|------|------|----------|
| 性能风险 | 中 | 高 | 压测 + 扩容 |
| 数据风险 | 低 | 高 | 备份 + 对账 |
| 进度风险 | 中 | 中 | 缓冲时间 |
"""
            optimized += risk_section
        
        # Add success metrics if missing
        if '成功指标' not in optimized and '指标' not in optimized:
            metrics_section = """
## 成功指标

| 指标类型 | 指标名称 | 基线值 | 目标值 |
|----------|----------|--------|--------|
| 业务指标 | DAU | 10,000 | 15,000 |
| 技术指标 | 响应时间 | 500ms | 200ms |
"""
            optimized = optimized.replace('## 2. 产品目标', f'## 2. 产品目标\n{metrics_section}')
    
    return optimized


def generate_optimization_report(evaluation: dict, output: str):
    """Generate optimization report"""
    
    scores = evaluation['scores']
    issues = evaluation['issues']
    
    report = f"""# 技术方案优化报告

**生成时间:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

## 📊 质量评分

### 总体评分：**{scores['overall']}/100**

| 维度 | 评分 | 状态 |
|------|------|------|
| 完整性 | {scores['completeness']}/100 | {'✅' if scores['completeness'] >= 80 else '⚠️'} |
| 准确性 | {scores['accuracy']}/100 | {'✅' if scores['accuracy'] >= 80 else '⚠️'} |
| 可行性 | {scores['feasibility']}/100 | {'✅' if scores['feasibility'] >= 80 else '⚠️'} |
| 清晰度 | {scores['clarity']}/100 | {'✅' if scores['clarity'] >= 80 else '⚠️'} |
| 风险控制 | {scores['risk_management']}/100 | {'✅' if scores['risk_management'] >= 80 else '⚠️'} |
| 成本控制 | {scores['cost_control']}/100 | {'✅' if scores['cost_control'] >= 80 else '⚠️'} |

---

## ⚠️ 发现的问题

### 严重问题 ({len(issues['critical'])})

"""
    
    for i, issue in enumerate(issues['critical'], 1):
        report += f"{i}. **{issue}**\n"
    
    report += f"\n### 主要问题 ({len(issues['major'])})\n\n"
    for i, issue in enumerate(issues['major'], 1):
        report += f"{i}. {issue}\n"
    
    report += f"\n### 次要问题 ({len(issues['minor'])})\n\n"
    for i, issue in enumerate(issues['minor'], 1):
        report += f"{i}. {issue}\n"
    
    report += """
---

## 💡 优化建议

### 立即优化
1. 补充缺失的章节
2. 添加必要的架构图
3. 完善任务拆分

### 短期优化
1. 增强技术选型对比
2. 补充风险评估
3. 细化时间估算

### 长期优化
1. 建立技术方案模板
2. 积累最佳实践
3. 定期 review 和更新

---

## 📋 优化清单

- [ ] 补充缺失章节
- [ ] 添加架构图
- [ ] 完善 API 设计
- [ ] 补充表设计
- [ ] 细化任务拆分
- [ ] 添加风险评估
- [ ] 补充成功指标

"""
    
    output_path = Path(output)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"✅ 优化报告已生成：{output_path}")


def main():
    parser = argparse.ArgumentParser(description='Optimize technical solution document')
    parser.add_argument('--input', '-i', required=True, help='Input solution file')
    parser.add_argument('--output', '-o', default='optimized-solution.md', help='Output file')
    parser.add_argument('--level', '-l', default='standard', 
                       choices=['light', 'standard', 'deep'],
                       help='Optimization level')
    parser.add_argument('--report', '-r', help='Optimization report file')
    
    args = parser.parse_args()
    
    # Read input file
    input_path = Path(args.input)
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Evaluate
    print("📊 评估现有方案...")
    evaluation = evaluate_solution(content)
    
    print(f"\n质量评分：{evaluation['scores']['overall']}/100")
    print(f"发现问题：{len(evaluation['issues']['critical'])}严重 + {len(evaluation['issues']['major'])}主要 + {len(evaluation['issues']['minor'])}次要")
    
    # Optimize
    optimized = optimize_solution(content, args.level)
    
    # Write optimized file
    output_path = Path(args.output)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(optimized)
    
    print(f"\n✅ 优化完成：{output_path}")
    print(f"📊 文档长度：{len(optimized.split())} 字")
    
    # Generate report
    if args.report:
        generate_optimization_report(evaluation, args.report)


if __name__ == '__main__':
    main()
