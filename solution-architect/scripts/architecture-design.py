#!/usr/bin/env python3
"""
Architecture Designer - Generate system architecture diagrams and documentation
"""

import argparse
from datetime import datetime
from pathlib import Path


def generate_architecture(requirements: str, output: str):
    """Generate architecture design document"""
    
    print("🏗️  Generating architecture design...")
    
    content = f"""# Architecture Design Document

**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

## 📋 Overview

### System Context

```mermaid
graph TB
    subgraph External["External Systems"]
        A[Users]
        B[Third-party APIs]
        C[Legacy Systems]
    end
    
    subgraph System["Our System"]
        D[API Gateway]
        E[Core Services]
        F[Data Stores]
    end
    
    A --> D
    B <--> E
    C <--> F
    D --> E
    E --> F
```

### Architecture Principles

1. **Scalability** - Horizontal scaling, stateless design
2. **Reliability** - Redundancy, failover, monitoring
3. **Security** - Defense in depth, least privilege
4. **Maintainability** - Modularity, documentation, testing
5. **Cost-effectiveness** - Right-sizing, automation

---

## 🏛️ Architecture Views

### Logical View

```mermaid
graph TB
    subgraph Presentation["Presentation Layer"]
        A[Web UI]
        B[Mobile UI]
        C[API]
    end
    
    subgraph Business["Business Layer"]
        D[Service 1]
        E[Service 2]
        F[Service 3]
    end
    
    subgraph Data["Data Layer"]
        G[(Primary DB)]
        H[(Cache)]
        I[(Analytics)]
    end
    
    A & B & C --> D & E & F
    D & E & F --> G & H & I
```

### Physical View

```mermaid
graph TB
    subgraph Region1["Region 1 (Primary)"]
        subgraph AZ1["Availability Zone 1"]
            A1[App Server 1]
            B1[(DB Primary)]
        end
        subgraph AZ2["Availability Zone 2"]
            A2[App Server 2]
            B2[(DB Replica)]
        end
        LB1[Load Balancer]
    end
    
    subgraph Region2["Region 2 (DR)"]
        A3[App Server 3]
        B3[(DB Replica)]
        LB2[Load Balancer]
    end
    
    LB1 --> A1 & A2
    LB2 --> A3
    B1 --> B2
    B2 -.-> B3
```

### Data Flow View

```mermaid
sequenceDiagram
    participant U as User
    participant LB as Load Balancer
    participant API as API Service
    participant DB as Database
    participant Cache as Cache
    
    U->>LB: Request
    LB->>API: Route request
    API->>Cache: Check cache
    Cache-->>API: Cache miss
    API->>DB: Query data
    DB-->>API: Return data
    API->>Cache: Store in cache
    API-->>U: Response
```

---

## 🔧 Component Design

### Component 1: API Gateway

**Responsibilities:**
- Request routing
- Authentication/Authorization
- Rate limiting
- Request/Response transformation

**Technologies:**
- Kong / AWS API Gateway / Nginx

**Interfaces:**
```yaml
Endpoints:
  - POST /api/v1/resource
  - GET /api/v1/resource/{id}
  - PUT /api/v1/resource/{id}
  - DELETE /api/v1/resource/{id}
```

### Component 2: Core Service

**Responsibilities:**
- Business logic execution
- Data validation
- Integration with other services

**Technologies:**
- Node.js / Python / Go

**Dependencies:**
- Database
- Cache
- Message Queue

---

## 📊 Data Design

### Entity Relationship

```mermaid
erDiagram
    USER ||--o{ ORDER : places
    ORDER ||--|{ ORDER_ITEM : contains
    PRODUCT ||--o{ ORDER_ITEM : "ordered in"
    CATEGORY ||--|{ PRODUCT : belongs
    
    USER {
        string id PK
        string email
        string password_hash
        datetime created_at
    }
    
    ORDER {
        string id PK
        string user_id FK
        decimal total
        string status
        datetime created_at
    }
    
    PRODUCT {
        string id PK
        string name
        decimal price
        string category_id FK
    }
```

### Data Lifecycle

```mermaid
stateDiagram-v2
    [*] --> Created
    Created --> Active: Activated
    Active --> Archived: Archived
    Active --> Deleted: Deleted
    Archived --> Deleted: Purged
    Deleted --> [*]
```

---

## 🔒 Security Design

### Security Layers

```mermaid
graph TB
    subgraph Perimeter["Perimeter Security"]
        A[WAF]
        B[DDoS Protection]
    end
    
    subgraph Network["Network Security"]
        C[Firewall]
        D[VPC]
    end
    
    subgraph Application["Application Security"]
        E[Authentication]
        F[Authorization]
        G[Input Validation]
    end
    
    subgraph Data["Data Security"]
        H[Encryption]
        I[Masking]
    end
    
    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
    F --> G
    G --> H
    H --> I
```

### Authentication Flow

```mermaid
sequenceDiagram
    participant U as User
    participant App as Application
    participant Auth as Auth Service
    participant DB as User DB
    
    U->>App: Login credentials
    App->>Auth: Validate credentials
    Auth->>DB: Query user
    DB-->>Auth: User data
    Auth->>Auth: Verify password
    Auth-->>App: JWT token
    App-->>U: Session token
```

---

## 📈 Scalability Design

### Scaling Strategy

| Component | Scaling Approach | Trigger |
|-----------|-----------------|---------|
| **Web Servers** | Horizontal | CPU > 70% |
| **Database** | Read replicas | Read latency > 100ms |
| **Cache** | Cluster mode | Memory > 80% |
| **API Gateway** | Horizontal | Requests > 1000/s |

### Performance Targets

| Metric | Target | Measurement |
|--------|--------|-------------|
| Response Time (P50) | < 100ms | APM |
| Response Time (P99) | < 500ms | APM |
| Throughput | 10,000 req/s | Load testing |
| Error Rate | < 0.1% | Monitoring |

---

## 🔄 Integration Design

### External Integrations

```mermaid
graph LR
    System[Our System] --> Payment[Payment Gateway]
    System --> Email[Email Service]
    System --> SMS[SMS Service]
    System --> Analytics[Analytics Platform]
```

### API Contracts

**Request Example:**
```json
{
  "method": "POST",
  "path": "/api/v1/resource",
  "headers": {
    "Authorization": "Bearer {token}",
    "Content-Type": "application/json"
  },
  "body": {
    "field1": "value1",
    "field2": "value2"
  }
}
```

**Response Example:**
```json
{
  "status": "success",
  "data": {
    "id": "123",
    "field1": "value1",
    "field2": "value2"
  },
  "timestamp": "2024-01-01T00:00:00Z"
}
```

---

## 📋 Architecture Decisions

### Decision Log

| ID | Decision | Rationale | Status |
|----|----------|-----------|--------|
| ADR-001 | Use microservices | Scalability, team autonomy | Approved |
| ADR-002 | PostgreSQL for primary DB | ACID compliance, maturity | Approved |
| ADR-003 | Redis for caching | Performance, data structures | Approved |
| ADR-004 | AWS as cloud provider | Service breadth, global reach | Approved |

---

## 📎 Appendices

### A. Technology Stack Summary

| Layer | Technology | Version | Justification |
|-------|------------|---------|---------------|
| Frontend | React | 18.x | Ecosystem, performance |
| Backend | Node.js | 20.x | JavaScript, async |
| Database | PostgreSQL | 15.x | ACID, scalability |
| Cache | Redis | 7.x | Performance |
| Cloud | AWS | - | Services, global |

### B. Diagrams Index

1. System Context Diagram
2. Logical Architecture
3. Physical Architecture
4. Data Flow Diagram
5. Entity Relationship Diagram
6. Security Architecture
7. Integration Architecture

---

**Document Control**

| Version | Date | Author | Status |
|---------|------|--------|--------|
| 0.1 | {{Date}} | {{Author}} | Draft |
| 1.0 | {{Date}} | {{Author}} | Approved |

"""
    
    output_path = Path(output)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Architecture design generated: {output_path}")
    return content


def main():
    parser = argparse.ArgumentParser(description='Generate architecture design')
    parser.add_argument('--requirements', '-r', required=True, help='Requirements')
    parser.add_argument('--output', '-o', default='architecture-design.md', help='Output file')
    
    args = parser.parse_args()
    
    generate_architecture(args.requirements, args.output)


if __name__ == '__main__':
    main()
