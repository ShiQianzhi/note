# Mission: 从 Python Agent Worker 学会企业级 Agent 开发

## Why
通过一篇可以从头跟做的渐进式教程，先吃透 Python Agent Worker 的核心循环，再逐步接入工具、状态、RAG、人工审批、Go 接入层和异步基础设施，最终具备设计与上线企业级 Agent 系统的能力。

## Success looks like
- 能从空目录开始，不依赖 Agent 框架手写带工具调用、退出条件和错误处理的 Python Agent Loop
- 能设计带权限、幂等、超时、重试和审计的工具接口
- 能搭建包含 RAG、会话状态、人工审批和断点恢复的业务工作流
- 能通过评测集、链路追踪、成本指标和安全护栏判断系统是否可上线
- 能解释 Python Worker 与 Go 接入层的职责边界，并按教程把两者连接起来

## Constraints
- 单篇 Markdown 教程是主交付物，代码是读者跟随教程逐步写出的练习结果
- 每个阶段都给出前置条件、完整代码、运行命令、预期输出、故障排查和验证关卡
- 优先学习稳定协议和工程原理，再学习 LangGraph 或 Eino 等框架
- 先从最小 Python Worker 开始，再以企业工单助手为贯穿案例逐步扩展
- 复杂概念使用中文名称（英文术语）和后端工程类比解释

## Out of scope
- 大模型预训练和微调算法研究
- 一开始就构建多 Agent 自组织系统
- 一开始就安装 Kafka、Redis、PostgreSQL 等基础设施
- 在没有评测和护栏前接入高风险生产写操作
