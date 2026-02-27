#!/usr/bin/env python3
"""
PRD to Technical Solution Generator
Converts Product Requirements Document into comprehensive technical solution
"""

import argparse
import json
from datetime import datetime
from pathlib import Path


def generate_technical_solution(prd_content: str, output: str, solution_type: str = 'full'):
    """Generate complete technical solution from PRD"""
    
    print(f"🏗️  Generating technical solution from PRD...")
    print(f"📋 PRD: {prd_content[:100]}...")
    
    content = f"""# 技术方案文档

**文档版本:** 1.0  
**生成时间:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**文档类型:** {solution_type.title()}  
**状态:** 草稿

---

## 📋 1. 需求背景

### 1.1 业务背景

{{业务背景描述}}

**市场现状:**
- 市场趋势分析
- 竞争对手情况
- 用户需求变化

**业务痛点:**
- 当前问题分析
- 影响范围
- 紧迫性评估

### 1.2 用户痛点

| 用户群体 | 痛点描述 | 影响程度 | 频率 |
|----------|----------|----------|------|
| 用户群体 1 | 痛点 1 | 高 | 每天 |
| 用户群体 2 | 痛点 2 | 中 | 每周 |

### 1.3 项目范围

**In Scope (范围内):**
- 功能 1
- 功能 2
- 功能 3

**Out of Scope (范围外):**
- 不包含功能 1
- 不包含功能 2

---

## 🎯 2. 产品目标

### 2.1 核心目标

1. **目标 1:** {{SMART 目标}}
   - 衡量指标：{{Metric}}
   - 目标值：{{Target}}
   - 时间线：{{Timeline}}

2. **目标 2:** {{SMART 目标}}
   - 衡量指标：{{Metric}}
   - 目标值：{{Target}}
   - 时间线：{{Timeline}}

### 2.2 成功指标

| 指标类型 | 指标名称 | 基线值 | 目标值 | 提升 |
|----------|----------|--------|--------|------|
| **业务指标** | DAU | 10,000 | 15,000 | +50% |
| **体验指标** | 转化率 | 5% | 8% | +60% |
| **技术指标** | 响应时间 | 500ms | 200ms | -60% |

### 2.3 优先级

| 优先级 | 功能 | 价值 | 复杂度 | ROI |
|--------|------|------|--------|-----|
| P0 | 核心功能 1 | 高 | 中 | 高 |
| P1 | 重要功能 2 | 高 | 高 | 中 |
| P2 | 优化功能 3 | 中 | 低 | 高 |

---

## 🎯 3. 系统目标

### 3.1 功能目标

- [ ] 实现核心功能 1
- [ ] 实现核心功能 2
- [ ] 支持第三方集成

### 3.2 性能目标

| 指标 | 目标 | 测量方法 |
|------|------|----------|
| **响应时间 (P50)** | < 200ms | APM 监控 |
| **响应时间 (P99)** | < 500ms | APM 监控 |
| **吞吐量** | > 1000 TPS | 压测 |
| **并发用户** | > 10,000 | 压测 |

### 3.3 可用性目标

| 指标 | 目标 | 保障措施 |
|------|------|----------|
| **系统可用性** | 99.9% | 多可用区部署 |
| **数据可靠性** | 99.99% | 备份 + 冗余 |
| **灾备能力** | RTO<1h, RPO<5min | 灾备方案 |

### 3.4 安全目标

- ✅ 数据加密（传输 + 存储）
- ✅ 访问控制（RBAC）
- ✅ 审计日志
- ✅ 合规要求（GDPR/SOC2）

---

## 🏗️ 4. 系统架构

### 4.1 系统上下文

```mermaid
graph TB
    subgraph External["外部系统"]
        A[用户]
        B[第三方支付]
        C[短信服务]
        D[邮件服务]
    end
    
    subgraph System["本系统"]
        E[API 网关]
        F[业务服务]
        G[(数据库)]
        H[缓存]
    end
    
    A --> E
    E --> F
    F --> G & H
    F --> B & C & D
```

### 4.2 组件架构

```mermaid
graph TB
    subgraph Client["客户端"]
        A[Web 端]
        B[移动端]
        C[小程序]
    end
    
    subgraph Gateway["网关层"]
        D[API Gateway]
        E[Load Balancer]
    end
    
    subgraph Service["服务层"]
        F[用户服务]
        G[订单服务]
        H[支付服务]
        I[通知服务]
    end
    
    subgraph Data["数据层"]
        J[(MySQL)]
        K[(Redis)]
        L[(MongoDB)]
    end
    
    A & B & C --> D
    D --> E
    E --> F & G & H & I
    F & G & H & I --> J & K & L
```

### 4.3 技术栈

| 层级 | 技术选型 | 版本 | 理由 |
|------|----------|------|------|
| **前端** | React | 18.x | 生态完善，性能好 |
| **后端** | Node.js | 20.x | 全栈 JS，异步高效 |
| **数据库** | MySQL | 8.0 | ACID，成熟稳定 |
| **缓存** | Redis | 7.x | 高性能，数据结构丰富 |
| **消息队列** | RabbitMQ | 3.x | 可靠，路由灵活 |
| **云服务** | AWS | - | 服务全，全球覆盖 |

---

## 🔄 5. 业务流程

### 5.1 主流程

```mermaid
flowchart TD
    Start([用户发起请求]) --> A[验证用户身份]
    A --> B{验证通过？}
    B -->|是 | C[执行核心业务逻辑]
    B -->|否 | D[返回错误]
    C --> E[更新数据库]
    E --> F[发送通知]
    F --> G[返回结果]
    G --> End([结束])
    D --> End
```

### 5.2 分支流程

```mermaid
flowchart LR
    A[主流程] --> B{条件判断}
    B -->|分支 1| C[分支流程 1]
    B -->|分支 2| D[分支流程 2]
    B -->|分支 3| E[分支流程 3]
    C & D & E --> F[汇合点]
    F --> G[继续主流程]
```

### 5.3 异常流程

| 异常场景 | 触发条件 | 处理方式 | 通知方式 |
|----------|----------|----------|----------|
| 系统异常 | 服务不可用 | 降级 + 重试 | 邮件 + 短信 |
| 数据异常 | 数据不一致 | 回滚 + 告警 | 邮件 |
| 业务异常 | 规则不满足 | 返回错误 | 前端提示 |

---

## 💰 6. 资金流程

### 6.1 支付流程

```mermaid
sequenceDiagram
    participant U as 用户
    participant S as 系统
    participant P as 支付渠道
    participant B as 银行
    
    U->>S: 发起支付
    S->>P: 创建支付订单
    P->>B: 请求扣款
    B-->>P: 扣款结果
    P-->>S: 支付结果
    S->>S: 更新订单状态
    S-->>U: 支付成功
```

### 6.2 退款流程

```mermaid
sequenceDiagram
    participant U as 用户
    participant S as 系统
    participant P as 支付渠道
    participant B as 银行
    
    U->>S: 申请退款
    S->>S: 审核退款
    S->>P: 发起退款
    P->>B: 退款到卡
    B-->>P: 退款结果
    P-->>S: 退款成功
    S->>S: 更新订单状态
    S-->>U: 退款成功通知
```

### 6.3 对账流程

```mermaid
flowchart TB
    A[下载对账单] --> B[数据解析]
    B --> C[数据比对]
    C --> D{是否一致？}
    D -->|是 | E[对账成功]
    D -->|否 | F[差异分析]
    F --> G[人工核查]
    G --> H[调账处理]
    H --> I[对账完成]
    E --> I
```

---

## 💧 7. 数据流程

### 7.1 数据采集

```mermaid
graph LR
    A[用户行为] --> B[SDK 采集]
    C[业务数据] --> D[数据库同步]
    E[第三方数据] --> F[API 对接]
    B & D & F --> G[数据湖]
    G --> H[数据仓库]
```

### 7.2 数据处理

| 处理阶段 | 处理方式 | 工具 | 频率 |
|----------|----------|------|------|
| **实时处理** | 流式计算 | Flink | 实时 |
| **批量处理** | ETL | Airflow | 每天 |
| **数据清洗** | 规则引擎 | 自研 | 实时 |

### 7.3 数据存储

| 数据类型 | 存储方案 | 保留期 | 容量 |
|----------|----------|--------|------|
| **热数据** | Redis | 7 天 | 100GB |
| **温数据** | MySQL | 1 年 | 1TB |
| **冷数据** | S3 | 永久 | 10TB |

---

## 📊 8. 数据模型

### 8.1 实体关系

```mermaid
erDiagram
    USER ||--o{ ORDER : places
    ORDER ||--|{ ORDER_ITEM : contains
    PRODUCT ||--o{ ORDER_ITEM : "ordered in"
    CATEGORY ||--|{ PRODUCT : belongs
    PAYMENT ||--|| ORDER : pays
    
    USER {
        bigint id PK
        varchar email
        varchar password_hash
        datetime created_at
    }
    
    ORDER {
        bigint id PK
        bigint user_id FK
        decimal amount
        varchar status
        datetime created_at
    }
    
    PRODUCT {
        bigint id PK
        varchar name
        decimal price
        bigint category_id FK
    }
    
    PAYMENT {
        bigint id PK
        bigint order_id FK
        varchar channel
        varchar status
        datetime paid_at
    }
```

### 8.2 核心实体

#### User (用户)

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| id | bigint | ✅ | 主键 |
| email | varchar | ✅ | 邮箱 |
| password_hash | varchar | ✅ | 密码哈希 |
| status | tinyint | ✅ | 状态 |
| created_at | datetime | ✅ | 创建时间 |

#### Order (订单)

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| id | bigint | ✅ | 主键 |
| user_id | bigint | ✅ | 用户 ID |
| amount | decimal | ✅ | 金额 |
| status | varchar | ✅ | 状态 |
| created_at | datetime | ✅ | 创建时间 |

### 8.3 数据字典

| 数据项 | 代码 | 说明 | 取值 |
|--------|------|------|------|
| 订单状态 | order_status | 订单生命周期状态 | pending/paid/shipped/completed |
| 支付状态 | payment_status | 支付结果 | success/failed/refunded |
| 用户状态 | user_status | 用户账号状态 | active/banned/deleted |

---

## 🔌 9. API 设计

### 9.1 API 概览

| 模块 | 接口数 | 认证 | 限流 |
|------|--------|------|------|
| **用户** | 5 | OAuth2 | 1000/min |
| **订单** | 8 | OAuth2 | 500/min |
| **支付** | 4 | OAuth2 | 200/min |
| **商品** | 6 | 公开 | 2000/min |

### 9.2 接口详情

#### 创建订单

```http
POST /api/v1/orders
Content-Type: application/json
Authorization: Bearer {token}

{
  "items": [
    {
      "product_id": 123,
      "quantity": 2
    }
  ],
  "shipping_address": {
    "name": "张三",
    "phone": "13800138000",
    "address": "北京市朝阳区 xxx"
  }
}
```

**响应:**

```json
{
  "code": 0,
  "message": "success",
  "data": {
    "order_id": "ORD20240227001",
    "amount": 299.00,
    "status": "pending",
    "created_at": "2024-02-27T10:00:00Z"
  }
}
```

#### 查询订单

```http
GET /api/v1/orders/{order_id}
Authorization: Bearer {token}
```

**响应:**

```json
{
  "code": 0,
  "data": {
    "order_id": "ORD20240227001",
    "user_id": 456,
    "items": [...],
    "amount": 299.00,
    "status": "paid",
    "created_at": "2024-02-27T10:00:00Z"
  }
}
```

### 9.3 错误码

| 错误码 | 说明 | 处理建议 |
|--------|------|----------|
| 0 | 成功 | - |
| 1001 | 参数错误 | 检查请求参数 |
| 1002 | 认证失败 | 检查 token |
| 1003 | 权限不足 | 申请权限 |
| 2001 | 资源不存在 | 检查 ID |
| 2002 | 资源已存在 | 更换唯一标识 |
| 5001 | 系统异常 | 联系技术支持 |

---

## 🗄️ 10. 表设计

### 10.1 表结构

#### users (用户表)

```sql
CREATE TABLE `users` (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT '用户 ID',
  `email` varchar(255) NOT NULL COMMENT '邮箱',
  `password_hash` varchar(255) NOT NULL COMMENT '密码哈希',
  `nickname` varchar(100) DEFAULT NULL COMMENT '昵称',
  `avatar` varchar(500) DEFAULT NULL COMMENT '头像',
  `status` tinyint NOT NULL DEFAULT 1 COMMENT '状态：1-正常 0-禁用',
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_email` (`email`),
  KEY `idx_status` (`status`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='用户表';
```

#### orders (订单表)

```sql
CREATE TABLE `orders` (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT '订单 ID',
  `order_no` varchar(32) NOT NULL COMMENT '订单号',
  `user_id` bigint NOT NULL COMMENT '用户 ID',
  `amount` decimal(10,2) NOT NULL COMMENT '订单金额',
  `status` varchar(20) NOT NULL DEFAULT 'pending' COMMENT '订单状态',
  `remark` varchar(500) DEFAULT NULL COMMENT '备注',
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_order_no` (`order_no`),
  KEY `idx_user_id` (`user_id`),
  KEY `idx_status` (`status`),
  KEY `idx_created_at` (`created_at`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='订单表';
```

### 10.2 索引设计

| 表名 | 索引名 | 字段 | 类型 | 说明 |
|------|--------|------|------|------|
| users | uk_email | email | UNIQUE | 邮箱唯一索引 |
| users | idx_status | status | NORMAL | 状态查询 |
| orders | uk_order_no | order_no | UNIQUE | 订单号唯一 |
| orders | idx_user_id | user_id | NORMAL | 用户订单查询 |
| orders | idx_created_at | created_at | NORMAL | 时间范围查询 |

### 10.3 数据迁移

```sql
-- 数据迁移脚本
-- 版本：1.0
-- 日期：2024-02-27

-- 1. 创建新表
CREATE TABLE new_table LIKE old_table;

-- 2. 数据迁移
INSERT INTO new_table SELECT * FROM old_table;

-- 3. 数据验证
SELECT COUNT(*) FROM old_table;
SELECT COUNT(*) FROM new_table;

-- 4. 切换表名
RENAME TABLE old_table TO old_table_backup, new_table TO old_table;
```

---

## 🎯 11. 影响面分析

### 11.1 系统影响

```mermaid
mindmap
  root((本次变更))
    前端系统
      Web 端
      移动端
      小程序
    后端系统
      用户服务
      订单服务
      支付服务
    数据层
      MySQL
      Redis
      MongoDB
    外部依赖
      支付渠道
      短信服务
      邮件服务
```

### 11.2 依赖系统

| 系统名称 | 依赖类型 | 影响程度 | 负责人 |
|----------|----------|----------|--------|
| 用户中心 | 强依赖 | 高 | 张三 |
| 支付中心 | 强依赖 | 高 | 李四 |
| 消息中心 | 弱依赖 | 中 | 王五 |
| 数据中心 | 弱依赖 | 低 | 赵六 |

### 11.3 风险评估

| 风险项 | 概率 | 影响 | 缓解措施 | 负责人 |
|--------|------|------|----------|--------|
| 性能下降 | 中 | 高 | 压测 + 扩容 | 张三 |
| 数据不一致 | 低 | 高 | 对账 + 监控 | 李四 |
| 接口不兼容 | 中 | 中 | 版本控制 | 王五 |
| 上线延期 | 中 | 中 | 缓冲时间 | 赵六 |

---

## 📋 12. 任务拆分

### 12.1 开发任务

| 任务 ID | 任务名称 | 负责人 | 优先级 | 估算 (天) | 状态 |
|---------|----------|--------|--------|-----------|------|
| DEV-001 | 数据库设计 | 张三 | P0 | 2 | TODO |
| DEV-002 | API 开发 - 用户模块 | 李四 | P0 | 3 | TODO |
| DEV-003 | API 开发 - 订单模块 | 王五 | P0 | 5 | TODO |
| DEV-004 | API 开发 - 支付模块 | 赵六 | P0 | 4 | TODO |
| DEV-005 | 前端开发 - Web | 钱七 | P1 | 5 | TODO |
| DEV-006 | 前端开发 - 移动端 | 孙八 | P1 | 5 | TODO |
| DEV-007 | 单元测试 | 全员 | P0 | 2 | TODO |
| DEV-008 | 集成测试 | 测试组 | P0 | 3 | TODO |

### 12.2 时间估算

```mermaid
gantt
    title 项目开发计划
    dateFormat  YYYY-MM-DD
    section 设计阶段
    数据库设计      :done,    des1, 2024-03-01, 2d
    API 设计        :active,  des2, 2024-03-03, 2d
    section 开发阶段
    后端开发        :         dev1, 2024-03-05, 10d
    前端开发        :         dev2, 2024-03-10, 8d
    section 测试阶段
    单元测试        :         test1, 2024-03-15, 3d
    集成测试        :         test2, 2024-03-18, 5d
    section 上线阶段
    预发布          :         stage1, 2024-03-23, 2d
    正式上线        :         prod1, 2024-03-25, 1d
```

### 12.3 里程碑

| 里程碑 | 日期 | 交付物 | 验收标准 |
|--------|------|--------|----------|
| **设计评审** | 2024-03-04 | 设计文档 | 评审通过 |
| **开发完成** | 2024-03-14 | 代码 + 单测 | 覆盖率>80% |
| **测试完成** | 2024-03-22 | 测试报告 | 无 P0/P1 bug |
| **正式上线** | 2024-03-25 | 线上服务 | 运行稳定 |

---

## 📎 附录

### A. 参考资料

- [产品需求文档](prd-link)
- [UI 设计稿](design-link)
- [竞品分析报告](analysis-link)

### B. 术语表

| 术语 | 说明 |
|------|------|
| DAU | 日活跃用户 |
| GMV | 商品交易总额 |
| ROI | 投资回报率 |
| SLA | 服务等级协议 |

### C. 变更记录

| 版本 | 日期 | 作者 | 变更内容 |
|------|------|------|----------|
| 1.0 | 2024-02-27 | {{Author}} | 初始版本 |

---

**文档审批**

| 角色 | 姓名 | 日期 | 意见 |
|------|------|------|------|
| 产品负责人 | | | |
| 技术负责人 | | | |
| 测试负责人 | | | |
| 项目经理 | | | |

"""
    
    # Write to file
    output_path = Path(output)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ 技术方案文档已生成：{output_path}")
    print(f"📊 文档长度：{len(content.split())} 字")
    
    return content


def main():
    parser = argparse.ArgumentParser(description='Generate technical solution from PRD')
    parser.add_argument('--prd', '-p', required=True, help='PRD content or file path')
    parser.add_argument('--output', '-o', default='technical-solution.md', help='Output file')
    parser.add_argument('--type', '-t', default='full', 
                       choices=['full', 'api', 'database', 'architecture'],
                       help='Solution type')
    
    args = parser.parse_args()
    
    # Read PRD from file if provided
    prd_content = args.prd
    if Path(prd_content).exists():
        with open(prd_content, 'r', encoding='utf-8') as f:
            prd_content = f.read()
    
    generate_technical_solution(prd_content, args.output, args.type)


if __name__ == '__main__':
    main()
