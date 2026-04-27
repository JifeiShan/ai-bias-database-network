# 验证日志模板

**审核者**：practical-expert  
**创建日期**：2026-04-27  
**用途**：为 AI 偏见案例数据库中的案例提供标准化验证记录

---

## 验证日志格式

```json
{
  "date": "YYYY-MM-DD",
  "verifier": "验证者身份",
  "action": "验证动作",
  "result": "验证结果",
  "notes": "备注（可选）"
}
```

---

## 验证动作类型

| 动作 | 描述 | 所需时间 |
|------|------|---------|
| `initial_review` | 初步审核案例完整性 | 15分钟 |
| `source_verification` | 验证公开来源 | 30分钟 |
| `connection_assessment` | 评估连接点脆弱性 | 20分钟 |
| `risk_identification` | 识别风险点 | 15分钟 |
| `follow_up` | 跟踪案例进展 | 持续 |

---

## 验证等级

| 等级 | 标准 | 示例 |
|------|------|------|
| **A** | 公开来源+法律文件+判决 | BIAS-2024-001 |
| **B** | 公开来源+监管调查 | BIAS-2025-003 |
| **C** | 内部文档+媒体关注 | 待补充 |
| **D** | 仅内部报告，无公开来源 | CASE-2026-001/002 |

---

## 验证日志示例

### 案例：CASE-2026-001（招聘AI性别偏见）

```json
[
  {
    "date": "2026-04-27",
    "verifier": "practical-expert",
    "action": "initial_review",
    "result": "案例结构完整，但缺少验证过程记录",
    "notes": "需要补充数据来源验证"
  },
  {
    "date": "2026-04-27",
    "verifier": "practical-expert",
    "action": "connection_assessment",
    "result": "识别出连接点脆弱性：研究团队法律保护不明",
    "notes": "风险：研究团队可能被公司压力影响"
  }
]
```

---

## 下一步行动

1. 为 CASE-2026-001/002/003 创建初始验证日志
2. 标记为"示例案例"或补充真实来源
3. 更新 cases.json 文件

**实践者的签名**：practical-expert  
**日期**：2026-04-27