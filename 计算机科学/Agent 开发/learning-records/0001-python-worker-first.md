# Learning Record 0001: Python Agent Worker First

## Context

最初课程设计从完整的 Go + Python 混合项目和基础设施开始，读者需要先面对多个服务、目录和运行依赖，Agent 的核心执行循环反而出现得较晚。

## Insight

课程应先让读者亲手完成 Python Agent Worker 的最小闭环：模型提出工具调用、Worker 校验并执行工具、工具结果回灌、模型输出最终答案。Go 网关、消息队列和持久化都建立在这个闭环之上，适合在核心机制可解释、可测试之后引入。

## Decision

- 单篇 Markdown 教程是主交付物。
- 第一阶段使用 Fake Model，核心学习不依赖网络和模型密钥。
- 先完成裸 Python Agent Loop，再接真实模型和 Agent 框架。
- Go、Kafka、Redis、PostgreSQL 放到后续扩展阶段。

## Consequence

每章必须给出完整文件、精确命令、预期输出、故障排查和验证关卡。配套代码只作为跟随教程产生的练习结果，不作为需要读者自行理解的独立项目交付。
