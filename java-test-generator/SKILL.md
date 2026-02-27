---
name: java-test-generator
description: Java 单元测试生成工具。自动生成 JUnit 测试用例，支持 Mockito Mock，生成边界条件测试，分析测试覆盖率，补充缺失测试。支持 JUnit4/JUnit5。使用场景：单元测试编写、测试覆盖率提升、TDD 开发、遗留代码补测试。
---

# Java Test Generator - Java 测试生成专家

专业的 Java 单元测试自动生成工具。

## 快速开始

```bash
# 生成单元测试
python3 scripts/generate-test.py \
  --source UserService.java \
  --output UserServiceTest.java \
  --framework junit5

# 分析测试覆盖率
python3 scripts/coverage-analysis.py \
  --source ./src/main/java \
  --test ./src/test/java \
  --output 测试覆盖率报告.md

# 补充缺失测试
python3 scripts/missing-tests.py \
  --source ./src/main/java \
  --output 待补充测试列表.md
```

## 核心功能

### 🧪 测试用例生成

| 功能 | 说明 |
|------|------|
| **方法分析** | 分析公共方法 |
| **参数识别** | 识别方法参数 |
| **返回值处理** | 处理各种返回类型 |
| **异常测试** | 生成异常场景测试 |
| **边界条件** | 生成边界值测试 |

### 🎭 Mock 支持

| 功能 | 说明 |
|------|------|
| **依赖识别** | 识别依赖对象 |
| **Mock 生成** | 自动生成 Mock |
| **Stub 配置** | 配置返回值 |
| **Verify 支持** | 生成验证代码 |

### 📊 覆盖率分析

| 功能 | 说明 |
|------|------|
| **行覆盖率** | 分析行覆盖 |
| **分支覆盖** | 分析分支覆盖 |
| **方法覆盖** | 分析方法覆盖 |
| **缺失识别** | 识别未测试代码 |

### 🎯 测试补充

| 功能 | 说明 |
|------|------|
| **缺失方法** | 识别未测试方法 |
| **缺失场景** | 识别缺失场景 |
| **优先级评估** | 评估补充优先级 |
| **测试生成** | 生成补充测试 |

## 输出示例

```java
// UserServiceTest.java
package com.example.service;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import java.util.Optional;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

@ExtendWith(MockitoExtension.class)
class UserServiceTest {

    @Mock
    private UserRepository userRepository;

    @InjectMocks
    private UserService userService;

    @Test
    @DisplayName("获取用户信息 - 成功场景")
    void getUserInfo_Success() {
        // Given
        Long userId = 1L;
        User mockUser = new User(userId, "test@example.com");
        when(userRepository.findById(userId)).thenReturn(Optional.of(mockUser));

        // When
        User result = userService.getUserInfo(userId);

        // Then
        assertNotNull(result);
        assertEquals(userId, result.getId());
        verify(userRepository, times(1)).findById(userId);
    }

    @Test
    @DisplayName("获取用户信息 - 用户不存在")
    void getUserInfo_UserNotFound() {
        // Given
        Long userId = 999L;
        when(userRepository.findById(userId)).thenReturn(Optional.empty());

        // When & Then
        assertThrows(UserNotFoundException.class, () -> {
            userService.getUserInfo(userId);
        });
    }

    @Test
    @DisplayName("创建用户 - 邮箱已存在")
    void createUser_EmailExists() {
        // Given
        String email = "existing@example.com";
        when(userRepository.existsByEmail(email)).thenReturn(true);

        // When & Then
        assertThrows(EmailExistsException.class, () -> {
            userService.createUser(email);
        });
    }

    @Test
    @DisplayName("更新用户信息 - 成功场景")
    void updateUser_Success() {
        // Given
        Long userId = 1L;
        UserUpdateRequest request = new UserUpdateRequest("new@example.com");
        User existingUser = new User(userId, "old@example.com");
        when(userRepository.findById(userId)).thenReturn(Optional.of(existingUser));
        when(userRepository.save(any(User.class))).thenAnswer(i -> i.getArguments()[0]);

        // When
        User result = userService.updateUser(userId, request);

        // Then
        assertNotNull(result);
        assertEquals("new@example.com", result.getEmail());
        verify(userRepository).save(existingUser);
    }
}
```

## 使用场景

### 1. 新项目测试生成
```bash
python3 scripts/generate-test.py \
  --source ./src/main/java/com/example/service/*.java \
  --output ./src/test/java/ \
  --framework junit5
```

### 2. 遗留代码补测试
```bash
python3 scripts/missing-tests.py \
  --source ./src/main/java \
  --test ./src/test/java \
  --output 待补充测试.md
```

### 3. 测试覆盖率分析
```bash
python3 scripts/coverage-analysis.py \
  --source ./src/main/java \
  --test ./src/test/java \
  --output 覆盖率报告.md
```

### 4. PR 测试审查
```bash
python3 scripts/review-tests.py \
  --source ./src/main/java \
  --test ./src/test/java \
  --output 测试审查报告.md
```

## 支持的测试框架

| 框架 | 支持程度 |
|------|----------|
| **JUnit 5** | ✅ 完整支持 |
| **JUnit 4** | ✅ 完整支持 |
| **TestNG** | 🟡 部分支持 |
| **Mockito** | ✅ 完整支持 |
| **PowerMock** | 🟡 部分支持 |

## 生成的测试类型

| 测试类型 | 说明 |
|----------|------|
| **正常场景** | 基本功能测试 |
| **异常场景** | 异常处理测试 |
| **边界条件** | 边界值测试 |
| **空值处理** | null 值测试 |
| **参数验证** | 参数校验测试 |
| **集成测试** | 集成场景测试 |

## 测试质量检查

| 检查项 | 说明 |
|--------|------|
| **断言充分** | 断言是否充分 |
| **Mock 合理** | Mock 使用是否合理 |
| **命名规范** | 测试方法命名 |
| **独立性** | 测试是否独立 |
| **可重复性** | 测试是否可重复 |

## 与 CI/CD 集成

### Maven
```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-surefire-plugin</artifactId>
    <version>3.0.0</version>
</plugin>
```

### Gradle
```groovy
test {
    useJUnitPlatform()
    testLogging {
        events "passed", "skipped", "failed"
    }
}
```

## 最佳实践

详见 [references/best-practices.md](references/best-practices.md)：
- 单元测试最佳实践
- Mock 使用规范
- 测试命名规范
- 测试覆盖率目标

## 参见

- [OpenClaw 文档](https://docs.openclaw.ai)
- [ClawHub Skills](https://clawhub.com)
