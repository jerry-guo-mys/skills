# Mermaid 图表使用指南

## 🚀 快速开始

### 1. 创建配置文件

```json
{
  "title": "我的演示",
  "slides": [
    {
      "type": "title",
      "emoji": "📊",
      "title": "系统架构",
      "subtitle": "使用 Mermaid 绘制流程图"
    },
    {
      "type": "mermaid",
      "title": "系统架构图",
      "description": "微服务架构流程图",
      "chart": "flowchart",
      "code": "flowchart TD\n    A[用户] --> B[网关]\n    B --> C[服务 A]\n    B --> D[服务 B]"
    }
  ]
}
```

### 2. 生成 PPT

```bash
python3 scripts/generate-ppt.py \
  --config my-config.json \
  --output output/my-presentation.html
```

### 3. 打开查看

```bash
open output/my-presentation.html
```

---

## 📊 图表类型示例

### 流程图 (Flowchart)

```json
{
  "type": "mermaid",
  "title": "业务流程",
  "code": "flowchart LR\n    A[开始] --> B[处理]\n    B --> C{判断}\n    C -->|是 | D[成功]\n    C -->|否 | E[失败]"
}
```

### 时序图 (Sequence Diagram)

```json
{
  "type": "mermaid",
  "title": "API 调用流程",
  "code": "sequenceDiagram\n    participant C as 客户端\n    participant S as 服务器\n    C->>S: GET /api/data\n    S-->>C: 返回 JSON"
}
```

### 类图 (Class Diagram)

```json
{
  "type": "mermaid",
  "title": "领域模型",
  "code": "classDiagram\n    class Order {\n        +String id\n        +checkout()\n    }\n    class Item {\n        +int quantity\n    }\n    Order --> Item"
}
```

### 状态图 (State Diagram)

```json
{
  "type": "mermaid",
  "title": "订单状态",
  "code": "stateDiagram-v2\n    [*] --> Pending\n    Pending --> Paid\n    Paid --> Shipped\n    Shipped --> Delivered"
}
```

### 甘特图 (Gantt)

```json
{
  "type": "mermaid",
  "title": "项目计划",
  "code": "gantt\n    title 开发计划\n    dateFormat  YYYY-MM-DD\n    section 前端\n    页面开发 :2026-03-01, 7d\n    section 后端\n    API 开发 :2026-03-01, 10d"
}
```

### 饼图 (Pie)

```json
{
  "type": "mermaid",
  "title": "时间分配",
  "code": "pie title 工作日\n    \"工作\" : 8\n    \"学习\" : 2\n    \"休息\" : 2\n    \"睡眠\" : 8\n    \"其他\" : 4"
}
```

---

## 💡 技巧

### 1. 多行字符串

在 JSON 中使用 `\n` 换行：

```json
"code": "flowchart TD\n    A --> B\n    B --> C"
```

### 2. 特殊字符转义

- 引号：`\"`
- 反斜杠：`\\`
- 换行：`\n`

### 3. 布局方向

```
flowchart TD   # 从上到下
flowchart LR   # 从左到右
flowchart RL   # 从右到左
flowchart BT   # 从下到上
```

### 4. 节点样式

```
A[矩形节点]
B(圆角节点)
C((圆形节点))
D{菱形判断}
E[/平行四边形/]
```

---

## 🎨 主题配置

在 `ppt-template.html` 中修改 Mermaid 主题：

```javascript
mermaid.initialize({ 
    theme: 'dark',  // 可选：'default', 'dark', 'forest', 'neutral'
    themeVariables: {
        primaryColor: '#06b6d4',
        primaryTextColor: '#f8fafc',
        primaryBorderColor: '#06b6d4'
    }
});
```

---

## 🔗 参考资源

- [Mermaid 官方文档](https://mermaid.js.org/)
- [在线编辑器](https://mermaid.live/)
- [语法示例](https://mermaid.js.org/syntax/flowchart.html)

---

**🎉 开始绘制你的图表吧！** 📊
