---
name: java-code-review
description: Java 代码审查专家。自动检查代码规范（Checkstyle/PMD）、代码异味、最佳实践、安全漏洞、性能问题、并发问题。支持 Maven/Gradle 项目。使用场景：日常 Code Review、PR 审查、代码质量审计、技术债务评估、团队代码规范检查。
---

# Java Code Review - Java 代码审查专家

专业的 Java 代码自动审查工具，帮助发现代码质量问题。

## 快速开始

```bash
# 完整代码审查
python3 scripts/review.py \
  --path ./src/main/java \
  --output 代码审查报告.md

# 仅安全检查
python3 scripts/review.py --path ./src --check security --output 安全报告.md

# 仅性能检查
python3 scripts/review.py --path ./src --check performance --output 性能报告.md

# PR 审查模式
python3 scripts/review.py --path ./src --pr-mode --output pr-review.md
```

## 核心功能

### 🔍 代码规范检查

| 检查项 | 说明 |
|--------|------|
| **命名规范** | 类名、方法名、变量名命名 |
| **代码格式** | 缩进、空格、换行 |
| **注释规范** | JavaDoc、行注释 |
| **文件结构** | import 顺序、类结构 |

### 🐛 代码异味检测

| 异味类型 | 说明 |
|----------|------|
| **过长方法** | 方法超过 50 行 |
| **过大类** | 类超过 500 行 |
| **重复代码** | 复制粘贴代码 |
| **过长参数列表** | 参数超过 5 个 |
| **过度耦合** | 依赖过多 |

### 🔒 安全漏洞扫描

| 漏洞类型 | 说明 |
|----------|------|
| **SQL 注入** | 拼接 SQL 语句 |
| **XSS** | 未转义用户输入 |
| **敏感信息泄露** | 硬编码密码/密钥 |
| **不安全随机数** | 使用 Random 而非 SecureRandom |
| **路径遍历** | 未验证文件路径 |

### ⚡ 性能问题识别

| 问题类型 | 说明 |
|----------|------|
| **N+1 查询** | 循环中查询数据库 |
| **资源未关闭** | IO/数据库连接未关闭 |
| **字符串拼接** | 循环中使用 + 拼接 |
| **不当集合使用** | ArrayList vs LinkedList |
| **同步滥用** | 过度使用 synchronized |

### 🔀 并发问题检查

| 问题类型 | 说明 |
|----------|------|
| **线程安全问题** | 非线程安全集合 |
| **死锁风险** | 锁顺序不一致 |
| **竞态条件** | 检查后使用模式 |
| **可见性问题** | 缺少 volatile |

## 输出示例

```markdown
# Java 代码审查报告

**审查时间:** 2026-02-27 22:15:00  
**审查路径:** ./src/main/java  
**审查文件:** 45 个  
**总代码行数:** 12,450

---

## 📊 总体评分：75/100

| 维度 | 评分 | 问题数 |
|------|------|--------|
| 代码规范 | 80/100 | 12 |
| 代码异味 | 70/100 | 8 |
| 安全性 | 65/100 | 5 |
| 性能 | 75/100 | 6 |
| 并发性 | 80/100 | 3 |

---

## 🔴 严重问题 (5)

### 1. [安全] SQL 注入风险
**位置:** `UserService.java:45`
**代码:**
```java
String sql = "SELECT * FROM users WHERE id = " + userId;
```
**建议:**
```java
String sql = "SELECT * FROM users WHERE id = ?";
preparedStatement.setString(1, userId);
```

### 2. [安全] 硬编码密码
**位置:** `DatabaseConfig.java:23`
**代码:**
```java
private static final String PASSWORD = "admin123";
```
**建议:** 使用环境变量或配置中心

### 3. [性能] N+1 查询
**位置:** `OrderService.java:128`
**代码:**
```java
for (Order order : orders) {
    User user = userService.getUser(order.getUserId());
}
```
**建议:** 使用批量查询或 JOIN

### 4. [性能] 资源未关闭
**位置:** `FileHandler.java:67`
**代码:**
```java
InputStream is = new FileInputStream(file);
// 未关闭
```
**建议:** 使用 try-with-resources

### 5. [并发] 线程安全问题
**位置:** `CacheManager.java:34`
**代码:**
```java
private static Map<String, Object> cache = new HashMap<>();
```
**建议:** 使用 ConcurrentHashMap

---

## 🟡 主要问题 (12)

### 1. [规范] 过长的方法
**位置:** `ReportService.generate(): 85 行`
**建议:** 拆分为多个小方法

### 2. [规范] 缺少 JavaDoc
**位置:** `UserService.java` 公共方法
**建议:** 添加完整的 JavaDoc

### 3. [异味] 过大的类
**位置:** `OrderController.java: 650 行`
**建议:** 按职责拆分

...

---

## 📋 改进建议

### 立即修复
- [ ] 修复所有 SQL 注入风险
- [ ] 移除硬编码密码
- [ ] 关闭未关闭的资源

### 短期优化
- [ ] 重构过长的方法
- [ ] 优化 N+1 查询
- [ ] 修复线程安全问题

### 长期改进
- [ ] 引入代码审查 checklist
- [ ] 配置 CI 自动检查
- [ ] 建立代码规范文档
```

## 使用场景

### 1. 日常 Code Review
```bash
python3 scripts/review.py --path ./src --output review-$(date +%Y%m%d).md
```

### 2. PR 审查
```bash
python3 scripts/review.py --path ./src --pr-mode --output pr-123-review.md
```

### 3. 代码质量审计
```bash
python3 scripts/review.py --path ./src --comprehensive --output audit.md
```

### 4. 安全检查
```bash
python3 scripts/review.py --path ./src --check security --output security.md
```

### 5. 技术债务评估
```bash
python3 scripts/review.py --path ./src --debt-mode --output debt.md
```

## 配置选项

### 检查规则配置

创建 `.code-review-config.json`:
```json
{
  "rules": {
    "naming": {
      "enabled": true,
      "maxMethodLength": 50,
      "maxClassLength": 500,
      "maxParameters": 5
    },
    "security": {
      "enabled": true,
      "checkSQLInjection": true,
      "checkXSS": true,
      "checkHardcodedPassword": true
    },
    "performance": {
      "enabled": true,
      "checkNPlusOne": true,
      "checkResourceLeak": true,
      "checkStringConcat": true
    }
  },
  "exclude": [
    "**/generated/**",
    "**/test/**",
    "**/target/**"
  ]
}
```

## 与 CI/CD 集成

### GitHub Actions
```yaml
- name: Java Code Review
  run: |
    python3 scripts/review.py --path ./src --output review.md
    # 如果有严重问题则失败
    grep -q "严重问题" review.md && exit 1 || exit 0
```

### Jenkins
```groovy
sh 'python3 scripts/review.py --path ./src --output review.md'
archiveArtifacts 'review.md'
```

## 最佳实践

详见 [references/best-practices.md](references/best-practices.md)：
- Java 编码规范
- 安全编码指南
- 性能优化技巧
- 并发编程最佳实践

## 参见

- [OpenClaw 文档](https://docs.openclaw.ai)
- [ClawHub Skills](https://clawhub.com)
