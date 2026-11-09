# Learning Record 0002: Agent State and Checkpoint Recovery

## Context

裸 Agent Loop 把消息历史保存在 `run()` 的局部变量中。进程退出后，Worker 无法判断模型已经完成几轮决策、哪些工具已经执行、下一轮应看到哪些结果。

## Insight

可恢复 Agent 需要把运行事实与运行资源分开。消息历史、已完成轮数、状态、最终答案和工具指纹属于可序列化运行事实；模型客户端、数据库连接、JWT 和函数引用属于新进程重新建立的运行资源。

检查点只能写在完整状态边界。工具批次完成后保存 assistant 申请和全部 tool 结果，恢复时才能直接进入下一轮模型决策。

## Decision

- 使用显式 `AgentState` 保存恢复所需状态。
- `AgentWorker` 依赖 `CheckpointStore` 端口，不直接依赖 SQLite。
- SQLite 检查点使用版本字段和条件更新实现乐观锁。
- `SUCCEEDED` 状态重复读取时直接返回最终答案，不再调用模型或工具。
- 本阶段允许模型异常后从上一完整检查点恢复；写工具的副作用幂等留到后续工具执行状态机处理。

## Evidence

- 教程代码从 Markdown 重建后共有十四个测试通过。
- 两个独立 Python 进程把同一 Run 从检查点版本 2 推进到版本 3。
- 第三次读取成功态时出现 `run.already_completed`，没有执行模型和工具。
