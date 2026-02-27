---
name: java-performance-optimizer
description: Java 性能优化专家。JVM 调优、GC 分析、内存泄漏检测、CPU 性能分析、线程性能分析、锁优化。支持 GC 日志分析、Heap Dump 分析、Thread Dump 分析。使用场景：性能调优、故障排查、容量规划、系统优化。
---

# Java Performance Optimizer - Java 性能优化专家

专业的 Java 性能分析和优化工具。

## 快速开始

```bash
# JVM 参数优化建议
python3 scripts/jvm-tuning.py \
  --heap-size 4g \
  --gc-type G1 \
  --output JVM 调优建议.md

# GC 日志分析
python3 scripts/gc-analysis.py \
  --gc-log gc.log \
  --output GC 分析报告.md

# 内存泄漏分析
python3 scripts/memory-leak.py \
  --heap-dump heap.hprof \
  --output 内存泄漏分析.md

# 线程性能分析
python3 scripts/thread-analysis.py \
  --thread-dump thread.txt \
  --output 线程分析报告.md
```

## 核心功能

### ⚙️ JVM 调优

| 功能 | 说明 |
|------|------|
| **堆内存优化** | 优化 Xmx/Xms 参数 |
| **GC 选择** | 推荐合适的 GC |
| **GC 参数调优** | 优化 GC 参数 |
| **元空间优化** | 优化 Metaspace |

### ♻️ GC 分析

| 功能 | 说明 |
|------|------|
| **GC 日志解析** | 解析 GC 日志 |
| **停顿分析** | 分析 Stop-the-world |
| **频率分析** | 分析 GC 频率 |
| **问题识别** | 识别 GC 问题 |

### 🧠 内存分析

| 功能 | 说明 |
|------|------|
| **泄漏检测** | 检测内存泄漏 |
| **堆分析** | 分析堆内存使用 |
| **对象分布** | 分析对象分布 |
| **优化建议** | 提供优化建议 |

### 🔀 线程分析

| 功能 | 说明 |
|------|------|
| **死锁检测** | 检测死锁 |
| **瓶颈识别** | 识别性能瓶颈 |
| **锁竞争分析** | 分析锁竞争 |
| **优化建议** | 提供优化建议 |

## 输出示例

```markdown
# JVM 性能优化报告

**分析时间:** 2026-02-27 22:30:00  
**JVM 版本:** OpenJDK 17.0.1  
**堆配置:** -Xmx2g -Xms512m

---

## 📊 当前配置评估

| 指标 | 当前值 | 建议值 | 状态 |
|------|--------|--------|------|
| **堆内存** | 2GB | 4GB | ⚠️ 不足 |
| **初始堆** | 512MB | 4GB | ❌ 过小 |
| **GC 类型** | G1 | G1 | ✅ 合理 |
| **GC 停顿** | 250ms | <100ms | ⚠️ 过长 |

---

## 🔍 问题分析

### 问题 1: 堆内存配置不当
**严重性:** ⚠️ 主要

**当前配置:**
```
-Xmx2g -Xms512m
```

**问题:**
- 初始堆和最大堆差距过大
- 导致频繁 GC 和堆扩展
- 影响应用性能

**建议:**
```
-Xmx4g -Xms4g
```

### 问题 2: Full GC 频繁
**严重性:** 🔴 严重

**现象:**
- Full GC 频率：每小时 5 次
- 平均停顿时间：250ms
- 最长达 1.2 秒

**原因:**
- 老年代空间不足
- 存在内存泄漏嫌疑
- Metaspace 配置过小

**建议:**
1. 增加堆内存到 4GB
2. 检查内存泄漏
3. 调整 Metaspace：-XX:MaxMetaspaceSize=512m

### 问题 3: 线程池配置不当
**严重性:** 🟡 主要

**当前配置:**
```java
Executors.newFixedThreadPool(10);
```

**问题:**
- 固定线程数未考虑 CPU 核心数
- 无界队列可能导致 OOM
- 缺少拒绝策略

**建议:**
```java
new ThreadPoolExecutor(
    corePoolSize,
    maxPoolSize,
    keepAliveTime,
    TimeUnit.SECONDS,
    new ArrayBlockingQueue<>(1000),
    new ThreadPoolExecutor.CallerRunsPolicy()
);
```

---

## ✅ 优化建议

### JVM 参数
```bash
# 堆内存
-Xmx4g -Xms4g

# GC 参数
-XX:+UseG1GC
-XX:MaxGCPauseMillis=100
-XX:G1HeapRegionSize=16m

# 元空间
-XX:MaxMetaspaceSize=512m

# GC 日志
-Xlog:gc*:file=gc.log:time,uptime:filecount=5,filesize=10M
```

### 预期效果
| 指标 | 优化前 | 优化后 | 提升 |
|------|--------|--------|------|
| GC 停顿 | 250ms | 80ms | 68%↓ |
| Full GC | 5 次/小时 | 0 次/小时 | 100%↓ |
| 吞吐量 | 85% | 95% | 12%↑ |
```

## 使用场景

### 1. 性能调优
```bash
python3 scripts/jvm-tuning.py \
  --heap-size 4g \
  --workload "web-app" \
  --output JVM 优化方案.md
```

### 2. GC 问题分析
```bash
python3 scripts/gc-analysis.py \
  --gc-log /var/log/gc.log \
  --output GC 问题分析.md
```

### 3. 内存泄漏排查
```bash
python3 scripts/memory-leak.py \
  --heap-dump /tmp/heap.hprof \
  --output 内存泄漏排查.md
```

### 4. 线程问题诊断
```bash
python3 scripts/thread-analysis.py \
  --thread-dump thread.txt \
  --output 线程问题诊断.md
```

## 支持的 GC 类型

| GC 类型 | 适用场景 |
|---------|----------|
| **G1 GC** | 大堆、低延迟 |
| **ZGC** | 超大堆、超低延迟 |
| **Shenandoah** | 大堆、低延迟 |
| **Parallel GC** | 吞吐量优先 |
| **Serial GC** | 单线程、小应用 |

## 性能指标参考

| 指标 | 优秀 | 良好 | 需优化 |
|------|------|------|--------|
| **GC 停顿** | <50ms | <100ms | >200ms |
| **GC 频率** | <1 次/分钟 | <5 次/分钟 | >10 次/分钟 |
| **吞吐量** | >95% | >90% | <85% |
| **堆使用率** | 60-80% | 50-90% | <40% 或 >95% |

## 最佳实践

详见 [references/best-practices.md](references/best-practices.md)：
- JVM 参数调优指南
- GC 选择策略
- 内存优化技巧
- 线程池最佳实践

## 参见

- [OpenClaw 文档](https://docs.openclaw.ai)
- [ClawHub Skills](https://clawhub.com)
