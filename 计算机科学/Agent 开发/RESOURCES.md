# 企业级 Agent 开发资源

## Knowledge

- [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/)
  官方 Agent SDK 文档，覆盖工具、交接、护栏、会话和追踪。用于理解常见 Agent 运行时能力如何落到代码。
- [Anthropic: Building effective agents](https://www.anthropic.com/research/building-effective-agents)
  官方工程文章，重点区分工作流（Workflow）与智能体（Agent），并解释何时应该使用更简单、可控的方案。
- [Anthropic: Building agents with the Claude Agent SDK](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk)
  官方 Agent SDK 实践，适合了解工具、上下文和长任务执行的工程设计。
- [LangGraph Documentation](https://docs.langchain.com/oss/python/langgraph/overview)
  状态图编排、持久化、人工介入和恢复机制参考。仅在手写 Agent Loop 后学习。
- [LangSmith: Evaluate a graph](https://docs.langchain.com/langsmith/evaluate-graph)
  官方评测指南，用于构建数据集、离线回归和多步骤 Agent 的轨迹评测。
- [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
  企业级安全基线，覆盖提示词注入、敏感信息泄露、过度授权和不安全输出处理。
- [OpenTelemetry GenAI semantic conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/)
  生成式 AI 链路追踪语义规范，用于统一记录模型调用、Agent 操作、工具执行、Token 与延迟。
- [Go/Python 后端工程师转 Agent 开发实战教程](Go-Python后端工程师转Agent开发实战教程.md)
  Agent 工程的概念与专题教程。适合先建立后端能力到 Agent 能力的映射。
- [从零搭建高并发企业级 Agent 系统教程](从零搭建高并发企业级Agent系统教程.md)
  当前渐进式主教程。从 Python Agent Worker 和 Fake Model 开始，按完整文件、命令、预期输出和验证关卡逐步扩展到混合架构。
- [高性能 Agent 服务架构设计与实现](../高性能服务设计与实现/高性能%20Agent%20服务架构设计与实现.md)
  当前笔记库的生产架构专题。用于学习高并发网关、任务编排、状态存储和流式通信。

## Wisdom (Communities)

- [LangChain Forum](https://forum.langchain.com/)
  适合检索 LangGraph 状态、持久化、评测和生产故障案例；优先参考维护者回复。
- [OpenAI Developer Community](https://community.openai.com/)
  适合核对模型 API、工具调用和结构化输出的实际边界；结论仍需回查官方文档。

## Gaps

- 云厂商、模型供应商和部署环境尚未确定，教程采用 OpenAI 兼容协议保持模型可替换。
