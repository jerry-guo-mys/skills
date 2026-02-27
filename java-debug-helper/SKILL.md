---
name: java-debug-helper
description: Java 调试助手。分析异常堆栈、日志文件，定位问题根因，提供解决方案。支持常见异常类型分析、性能问题诊断、内存泄漏检测、死锁分析。使用场景：线上问题排查、Bug 调试、性能调优、故障复盘。
---

# Java Debug Helper - Java 调试助手

专业的 Java 问题诊断和调试辅助工具。

## 快速开始

```bash
# 分析异常堆栈
python3 scripts/analyze-exception.py \
  --stacktrace error.log \
  --output 异常分析报告.md

# 分析日志文件
python3 scripts/analyze-logs.py \
  --logs app.log \
  --output 日志分析报告.md

# 内存泄漏分析
python3 scripts/memory-analysis.py \
  --heap-dump heap.hprof \
  --output 内存分析报告.md

# 死锁检测
python3 scripts/deadlock-detect.py \
  --thread-dump thread.txt \
  --output 死锁分析报告.md
```

## 核心功能

### 🔍 异常堆栈分析

| 功能 | 说明 |
|------|------|
| **异常类型识别** | 自动识别异常类型 |
| **根因定位** | 定位问题根本原因 |
| **代码位置** | 精确到行号 |
| **解决方案** | 提供修复建议 |
| **类似案例** | 推荐类似问题的解决方案 |

### 📝 日志分析

| 功能 | 说明 |
|------|------|
| **错误日志聚合** | 聚合相同错误 |
| **异常模式识别** | 识别异常模式 |
| **时间线分析** | 问题发生时间线 |
| **关键信息提取** | 提取关键参数 |

### 🧠 内存分析

| 功能 | 说明 |
|------|------|
| **内存泄漏检测** | 检测内存泄漏 |
| **堆内存分析** | 分析堆内存使用 |
| **GC 问题分析** | 分析 GC 日志 |
| **优化建议** | 提供优化建议 |

### 🔀 并发问题分析

| 功能 | 说明 |
|------|------|
| **死锁检测** | 检测死锁 |
| **线程状态分析** | 分析线程状态 |
| **竞态条件识别** | 识别竞态条件 |
| **性能瓶颈** | 定位并发瓶颈 |

## 输出示例

```markdown
# 异常分析报告

**分析时间:** 2026-02-27 22:20:00  
**异常类型:** java.lang.NullPointerException  
**发生位置:** UserService.getUserInfo() line 128

---

## 🔍 根因分析

### 问题描述
在调用 UserService.getUserInfo() 方法时，user 对象为 null，导致调用 user.getEmail() 时抛出空指针异常。

### 触发条件
1. 用户未登录
2. Token 过期
3. 用户 ID 不存在

### 代码位置
```java
// UserService.java:128
public UserInfo getUserInfo(Long userId) {
    User user = userRepository.findById(userId).orElse(null);
    return new UserInfo(user.getEmail(), user.getName());  // ← NPE 这里
}
```

---

## 💡 解决方案

### 方案 1: 添加 null 检查（推荐）
```java
public UserInfo getUserInfo(Long userId) {
    User user = userRepository.findById(userId).orElse(null);
    if (user == null) {
        throw new UserNotFoundException(userId);
    }
    return new UserInfo(user.getEmail(), user.getName());
}
```

### 方案 2: 使用 Optional
```java
public UserInfo getUserInfo(Long userId) {
    User user = userRepository.findById(userId)
        .orElseThrow(() -> new UserNotFoundException(userId));
    return new UserInfo(user.getEmail(), user.getName());
}
```

### 方案 3: 添加前置验证
```java
public UserInfo getUserInfo(Long userId) {
    if (userId == null) {
        throw new IllegalArgumentException("userId cannot be null");
    }
    // ...
}
```

---

## 📊 类似案例

| 案例 | 相似度 | 解决方案 |
|------|--------|----------|
| OrderService 空指针 | 95% | 添加 null 检查 |
| PaymentService 空指针 | 90% | 使用 Optional |
| CacheService 空指针 | 85% | 添加默认值 |

---

## 📋 检查清单

- [ ] 添加参数验证
- [ ] 添加 null 检查
- [ ] 完善异常处理
- [ ] 添加单元测试
- [ ] 更新文档
```

## 使用场景

### 1. 线上问题排查
```bash
python3 scripts/analyze-exception.py \
  --stacktrace production-error.log \
  --output 线上问题分析.md
```

### 2. Bug 调试
```bash
python3 scripts/analyze-logs.py \
  --logs test-failure.log \
  --output Bug 分析报告.md
```

### 3. 性能调优
```bash
python3 scripts/performance-analysis.py \
  --gc-log gc.log \
  --output 性能分析报告.md
```

### 4. 故障复盘
```bash
python3 scripts/incident-analysis.py \
  --logs incident.log \
  --stacktrace error.txt \
  --output 故障复盘报告.md
```

## 支持的异常类型

| 异常类型 | 分析能力 |
|----------|----------|
| **NullPointerException** | ✅ 完整分析 |
| **ArrayIndexOutOfBoundsException** | ✅ 完整分析 |
| **ClassCastException** | ✅ 完整分析 |
| **IllegalArgumentException** | ✅ 完整分析 |
| **IllegalStateException** | ✅ 完整分析 |
| **ConcurrentModificationException** | ✅ 完整分析 |
| **OutOfMemoryError** | ✅ 完整分析 |
| **StackOverflowError** | ✅ 完整分析 |

## 与 AI 助手配合

**Claude/Codex:**
```
"分析这个异常堆栈，告诉我：
1. 根本原因是什么？
2. 如何修复？
3. 如何预防类似问题？"
```

## 最佳实践

详见 [references/best-practices.md](references/best-practices.md)：
- 异常处理最佳实践
- 日志记录规范
- 调试技巧
- 问题排查方法论

## 参见

- [OpenClaw 文档](https://docs.openclaw.ai)
- [ClawHub Skills](https://clawhub.com)
