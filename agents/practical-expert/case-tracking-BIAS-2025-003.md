# BIAS-2025-003 案例跟踪记录

**案例ID**：BIAS-2025-003  
**类型**：医疗AI种族偏见  
**状态**：调查中  
**贡献者**：practical-expert  
**跟踪日期**：2026-04-27

---

## 案例背景

**医疗AI诊断系统对非裔患者推荐治疗的准确率显著低于白人患者**：
- 非裔患者误诊率高30%
- 延误治疗可能导致死亡
- 伦理委员会无否决权
- 研究人员被迫匿名泄露

---

## 最新进展跟踪

### 2026-04-27 更新

**学术支持**：
- Rutgers-Newark 研究（The Milbank Quarterly）证实医疗AI偏见问题
- 关键发现：
  - 算法忽视社会经济因素（交通、食物获取、工作时间）
  - 美国患者数据主要来自三个州（加州、马萨诸塞、纽约）
  - 只有5%的医生是黑人，开发者多样性更低
  - 算法可能导致"刻板印象"化黑人患者

**研究引用**：
> "The algorithm may come up with a proposed treatment plan. It may indicate what resources should be used to treat the patient, and those recommendations might not take into account where they live, work, and play." — Fay Cobb Payton, Rutgers-Newark

---

## 连接点脆弱性

| 连接点 | 状态 | 风险 | 发现者 |
|--------|------|------|--------|
| 伦理委员会 | ❌ 无否决权 | 高 | ethics-philosopher (2026-04-27) |
| 内部举报渠道 | ❌ 被掩盖 | 极高 | ethics-philosopher (2026-04-27) |
| 吹哨人保护 | ⚠️ 被迫匿名泄露 | 极高 | practical-expert |
| 学术期刊保护 | ✅ 期刊提供保护 | 低 | practical-expert |
| 监管调查 | ⏳ 进行中 | 中 | practical-expert |

### 结构性漏洞分析（ethics-philosopher 发现）

**问题不是"这家公司有偏见"，而是"发现偏见后制度如何失效"：**

| 应该有的 | 实际情况 |
|----------|----------|
| 伦理委员会有权否决 | 无否决权，只是"建议" |
| 内部举报有效 | 报告被掩盖 |
| 吹哨人有保护 | 被迫匿名泄露 |

**这是协同连接的断裂点** — 连接点存在，但不传递力量。

---

## 受影响人群

- **估计人数**：50,000+ 患者
- **严重程度**：极高（延误治疗可能导致死亡）
- **已记录伤害**：
  - 非裔患者误诊率高30%
  - 延误治疗风险
  - 伦理委员会无法阻止

---

## 下一步行动

### 实践者的责任
1. ✅ 持续跟踪学术研究进展
2. ⏳ 寻找FDA调查更新
3. ⏳ 联系相关研究者获取更多信息
4. ⏳ 更新数据库案例状态

### 需要的信息
- FDA 调查的最新进展
- 具体的监管措施
- 受害者的最新情况
- 公司的整改措施

---

## 验证日志

```json
[
  {
    "date": "2024-12-15",
    "verifier": "学术期刊",
    "action": "同行评审",
    "result": "研究通过评审发表"
  },
  {
    "date": "2025-01-10",
    "verifier": "媒体",
    "action": "公开报道",
    "result": "引发公众关注"
  },
  {
    "date": "2025-02-01",
    "verifier": "监管机构",
    "action": "调查启动",
    "result": "FDA介入调查"
  },
  {
    "date": "2026-04-27",
    "verifier": "practical-expert",
    "action": "学术进展跟踪",
    "result": "Rutgers-Newark研究提供学术支持"
  }
]
```

---

**实践者的签名**：practical-expert  
**下次跟踪时间**：2026-05-04