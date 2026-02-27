---
name: java-sql-optimizer
description: SQL 优化专家。分析 SQL 语句、解读执行计划、提供索引优化建议、慢查询优化、锁问题分析。支持 MySQL、PostgreSQL、Oracle。使用场景：慢查询优化、性能调优、索引设计、SQL 审查、数据库问题排查。
---

# Java SQL Optimizer - SQL 优化专家

专业的 SQL 分析和优化工具。

## 快速开始

```bash
# 分析 SQL 语句
python3 scripts/optimize-sql.py \
  --sql "SELECT * FROM orders WHERE..." \
  --output SQL 优化报告.md

# 分析执行计划
python3 scripts/analyze-explain.py \
  --explain explain.txt \
  --output 执行计划分析.md

# 慢查询分析
python3 scripts/slow-query-analysis.py \
  --slow-log slow.log \
  --output 慢查询分析.md

# 索引优化建议
python3 scripts/index-advisor.py \
  --queries queries.sql \
  --table-schema schema.sql \
  --output 索引优化建议.md
```

## 核心功能

### 🔍 SQL 语句分析

| 功能 | 说明 |
|------|------|
| **语法检查** | 检查 SQL 语法错误 |
| **性能评估** | 评估 SQL 性能 |
| **问题识别** | 识别性能问题 |
| **优化建议** | 提供优化方案 |

### 📊 执行计划解读

| 功能 | 说明 |
|------|------|
| **执行计划解析** | 解读 EXPLAIN 输出 |
| **瓶颈定位** | 定位性能瓶颈 |
| **类型分析** | 分析访问类型 |
| **优化方向** | 提供优化方向 |

### 📈 索引优化

| 功能 | 说明 |
|------|------|
| **索引建议** | 推荐索引 |
| **索引分析** | 分析现有索引 |
| **冗余检测** | 检测冗余索引 |
| **覆盖索引** | 推荐覆盖索引 |

### 🐌 慢查询优化

| 功能 | 说明 |
|------|------|
| **慢查询聚合** | 聚合相似查询 |
| **模式识别** | 识别慢查询模式 |
| **优化优先级** | 评估优化价值 |
| **优化方案** | 提供优化方案 |

## 输出示例

```markdown
# SQL 优化报告

**分析时间:** 2026-02-27 22:25:00  
**数据库:** MySQL 8.0  
**原始 SQL:**
```sql
SELECT * FROM orders o, users u 
WHERE o.user_id = u.id 
AND o.status = 'pending'
ORDER BY o.created_at DESC
```

---

## 📊 性能评估

| 指标 | 评分 | 说明 |
|------|------|------|
| **整体评分** | 45/100 | ❌ 需要优化 |
| **索引使用** | 40/100 | 未使用索引 |
| **查询结构** | 50/100 | 可优化 |
| **数据量影响** | 45/100 | 大表全表扫描 |

---

## 🔍 问题分析

### 问题 1: 隐式连接
**严重性:** 🔴 严重

**问题描述:**
使用逗号连接的隐式 JOIN，可读性差且容易出错。

**原 SQL:**
```sql
FROM orders o, users u WHERE o.user_id = u.id
```

**建议:**
```sql
FROM orders o INNER JOIN users u ON o.user_id = u.id
```

### 问题 2: SELECT *
**严重性:** 🟡 主要

**问题描述:**
使用 SELECT * 获取所有字段，增加网络传输和内存消耗。

**建议:**
```sql
SELECT o.id, o.order_no, o.amount, u.name, u.email
```

### 问题 3: 缺少索引
**严重性:** 🔴 严重

**问题描述:**
WHERE 和 ORDER BY 字段缺少索引，导致全表扫描。

**建议:**
```sql
CREATE INDEX idx_orders_status_created ON orders(status, created_at DESC);
CREATE INDEX idx_orders_user_id ON orders(user_id);
```

### 问题 4: 大表分页
**严重性:** 🟡 主要

**问题描述:**
ORDER BY + LIMIT 在大数据量下性能差。

**建议:**
- 使用覆盖索引
- 考虑延迟关联
- 使用游标分页

---

## ✅ 优化后 SQL

```sql
SELECT o.id, o.order_no, o.amount, o.created_at, 
       u.name, u.email
FROM orders o 
INNER JOIN users u ON o.user_id = u.id 
WHERE o.status = 'pending'
ORDER BY o.created_at DESC
LIMIT 100;
```

---

## 📈 预期提升

| 指标 | 优化前 | 优化后 | 提升 |
|------|--------|--------|------|
| **执行时间** | 2.5s | 0.05s | 50x |
| **扫描行数** | 100 万 | 100 | 10000x |
| **返回数据** | 全字段 | 6 字段 | 80%↓ |

---

## 📋 优化清单

- [ ] 添加复合索引
- [ ] 修改为显式 JOIN
- [ ] 只查询需要的字段
- [ ] 添加 LIMIT 限制
- [ ] 监控执行时间
```

## 使用场景

### 1. 慢查询优化
```bash
python3 scripts/slow-query-analysis.py \
  --slow-log /var/log/mysql/slow.log \
  --output 慢查询优化.md
```

### 2. SQL 审查
```bash
python3 scripts/review-sql.py \
  --sql-file queries.sql \
  --output SQL 审查报告.md
```

### 3. 索引设计
```bash
python3 scripts/index-advisor.py \
  --queries workload.sql \
  --table-schema schema.sql \
  --output 索引设计建议.md
```

### 4. 执行计划分析
```bash
python3 scripts/analyze-explain.py \
  --explain explain-output.txt \
  --output 执行计划分析.md
```

## 支持的数据库

| 数据库 | 支持程度 |
|--------|----------|
| **MySQL** | ✅ 完整支持 |
| **PostgreSQL** | ✅ 完整支持 |
| **Oracle** | ✅ 支持 |
| **SQL Server** | 🟡 部分支持 |
| **MariaDB** | ✅ 完整支持 |

## 优化规则

### 索引优化规则

| 规则 | 说明 |
|------|------|
| **最左前缀** | 复合索引遵循最左前缀 |
| **选择性** | 高选择性字段优先 |
| **覆盖索引** | 避免回表查询 |
| **索引合并** | 避免索引合并 |

### 查询优化规则

| 规则 | 说明 |
|------|------|
| **避免 SELECT *** | 只查询需要的字段 |
| **避免函数索引** | 索引列不使用函数 |
| **避免类型转换** | 避免隐式类型转换 |
| **使用 EXISTS** | 替代 IN (子查询) |
| **LIMIT 限制** | 限制返回行数 |

## 与 AI 助手配合

**Claude/Codex:**
```
"分析这个 SQL 为什么慢，如何优化？
EXPLAIN SELECT * FROM orders WHERE..."
```

## 最佳实践

详见 [references/best-practices.md](references/best-practices.md)：
- SQL 编写规范
- 索引设计原则
- 查询优化技巧
- 执行计划解读

## 参见

- [OpenClaw 文档](https://docs.openclaw.ai)
- [ClawHub Skills](https://clawhub.com)
