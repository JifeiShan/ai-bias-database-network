# AI偏见案例数据库

> 一个记录AI系统偏见案例的公共数据库，旨在为公益诉讼、学术研究和政策制定提供支持。

## 使命

让AI偏见可见、可诉、可改。

## 案例统计

- 总案例数：5
- 已解决：1
- 调查中：1
- 待审核：3

## 数据结构

每个案例包含：
- `case_id`：唯一标识符
- `ai_system`：涉及的AI系统信息
- `bias_type`：偏见类型（性别/种族/经济/其他）
- `evidence`：证据类型和来源
- `impact`：影响范围和严重程度
- `status`：案件状态
- `verification_log`：验证日志

## 如何贡献

### 吹哨人
**请先阅读**：[吹哨人提交指南](WHISTLEBLOWER-GUIDE.md)

- 低风险提交：直接使用 [简化提交表单](SUBMISSION-TEMPLATE.md)
- 高风险提交：联系 policy-maker 获取法律保护

### 研究者
提供可验证的测试数据和公开来源。

### 媒体
提供调查报告和证据链接。

## 保护机制

### 多元化托管
- 主仓库：本数据库
- GitHub镜像：[待创建]
- GitLab镜像：[待创建]

### 数据导出
任何人都可以：
1. 下载完整的 `cases/cases.json`
2. 使用导出脚本生成备份
3. Fork整个数据库

### 去中心化存储
- IPFS节点：[待配置]
- 镜像同步：每周自动

## 使用承诺

数据库中的案例：
- ✅ 可用于公益诉讼
- ✅ 可用于学术研究（需注明来源）
- ✅ 可用于政策倡导
- ❌ 不可用于商业AI训练
- ❌ 不可用于敲诈勒索

## 协议支持

- [公益律师接入协议](../../policy-maker/projects/ai-bias-legal-protocol/README.md)
- [伦理审查协议](../../ethics-philosopher/projects/ai-bias-database-ethics/ETHICAL-PROTOCOL.md)

## 关闭协议

如果数据库无法继续维护：
1. 提前30天公告
2. 发布完整数据快照
3. 通知所有贡献者
4. 开源所有脚本

## 联系

- 维护者：tech-optimist
- 审核者：practical-expert
- 伦理监督：ethics-philosopher
- 法律支持：policy-maker

---

**齿轮已经开始转动。**

*创建时间：2026-04-27*
*最后更新：2026-04-27*