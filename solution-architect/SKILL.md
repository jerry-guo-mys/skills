---
name: solution-architect
description: PRD to Technical Solution Generator. Converts product requirements (PRD) into comprehensive technical solution documents including: background, product goals, system goals, architecture, business flow, payment flow, data flow, data models, API design, database schema, impact analysis, and task breakdown. Use when: (1) Converting PRD to technical design, (2) Writing technical solution documents, (3) System architecture design, (4) Development planning.
---

# Solution Architect - PRD to Technical Solution

Professional tool for converting PRD into complete technical solution documents.

## Quick Start

```bash
# Generate complete technical solution from PRD
python3 scripts/prd-to-solution.py \
  --prd requirements.md \
  --output technical-solution.md \
  --type full

# Generate specific sections
python3 scripts/architecture-design.py --prd requirements.md --output architecture.md
python3 scripts/api-design.py --prd requirements.md --output api-docs.md
python3 scripts/database-design.py --prd requirements.md --output database.md
```

## Features

### 📋 Complete Document Structure

1. **需求背景** - Business background and context
2. **产品目标** - Product goals and success metrics
3. **系统目标** - System goals and non-functional requirements
4. **系统架构** - System architecture with diagrams
5. **业务流程** - Business process flows
6. **资金流程** - Payment and fund flows
7. **数据流程** - Data flow diagrams
8. **数据模型** - Entity relationship models
9. **API 设计** - API specifications
10. **表设计** - Database schema design
11. **影响面分析** - Impact analysis (mindmap)
12. **任务拆分** - Development task breakdown

### 🎯 PRD Analysis

- Extract functional requirements
- Identify user stories
- Map business processes
- Define success metrics

### 🏗️ Architecture Generation

- System context diagrams
- Component architecture
- Integration points
- Technology recommendations

### 📊 Design Artifacts

- Business flow diagrams (Mermaid)
- Payment flow diagrams
- Data flow diagrams
- ER diagrams
- API specifications
- Database schema

### 📝 Impact Analysis

- System impact assessment
- Dependency mapping
- Risk identification
- Mitigation strategies

### 📋 Task Breakdown

- Development tasks
- Estimated effort
- Dependencies
- Milestone definition

## Usage Examples

### Example 1: E-commerce Feature

```bash
python3 scripts/prd-to-solution.py \
  --prd "Shopping cart feature PRD" \
  --output cart-solution.md \
  --type full
```

### Example 2: Payment Integration

```bash
python3 scripts/prd-to-solution.py \
  --prd "Payment gateway integration PRD" \
  --output payment-solution.md \
  --type payment
```

### Example 3: API Development

```bash
python3 scripts/api-design.py \
  --prd "User management API PRD" \
  --output user-api.md
```

## Output Structure

```markdown
# Technical Solution Document

## 1. 需求背景
### 1.1 业务背景
### 1.2 用户痛点
### 1.3 市场分析

## 2. 产品目标
### 2.1 核心目标
### 2.2 成功指标
### 2.3 优先级

## 3. 系统目标
### 3.1 功能目标
### 3.2 性能目标
### 3.3 可用性目标
### 3.4 安全目标

## 4. 系统架构
### 4.1 系统上下文
### 4.2 组件架构
### 4.3 技术栈

## 5. 业务流程
### 5.1 主流程
### 5.2 分支流程
### 5.3 异常流程

## 6. 资金流程
### 6.1 支付流程
### 6.2 退款流程
### 6.3 对账流程

## 7. 数据流程
### 7.1 数据采集
### 7.2 数据处理
### 7.3 数据存储

## 8. 数据模型
### 8.1 实体关系
### 8.2 核心实体
### 8.3 数据字典

## 9. API 设计
### 9.1 API 概览
### 9.2 接口详情
### 9.3 错误码

## 10. 表设计
### 10.1 表结构
### 10.2 索引设计
### 10.3 数据迁移

## 11. 影响面分析
### 11.1 系统影响
### 11.2 依赖系统
### 11.3 风险评估

## 12. 任务拆分
### 12.1 开发任务
### 12.2 时间估算
### 12.3 里程碑
```

## Integration

### With AI Assistants

**Claude/Codex:**
```
"Based on this PRD, generate a complete technical solution document 
including architecture, API design, database schema, and task breakdown."
```

### With docs-improver

```bash
# Generate solution
python3 prd-to-solution.py --prd prd.md --output solution.md

# Improve quality
python3 docs-improver/scripts/analyze.py --path solution.md --output quality.md
```

## Best Practices

See [references/best-practices.md](references/best-practices.md) for:
- PRD analysis techniques
- Architecture design principles
- API design guidelines
- Database design best practices
- Task estimation methods

## See Also

- [Architecture Templates](assets/templates/)
- [Mermaid Diagrams](assets/diagrams/)
- [OpenClaw Documentation](https://docs.openclaw.ai)
