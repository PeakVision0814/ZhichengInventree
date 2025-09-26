---
title: 调度 Mixin（Schedule Mixin）
---

## ScheduleMixin

ScheduleMixin 类提供了一个插件，使其能够以固定时间间隔调用函数。

- 函数通过 InvenTree worker 注册，InvenTree worker 以后台进程运行。
- 调度函数不接受任何参数。
- 可以调用插件成员函数。
- 可以使用点分表示法指定全局函数。

!!! tip "启用调度集成"
    必须启用“启用调度集成”选项，才能激活调度插件事件。

{{ image("plugin/enable_schedule.png", "启用调度集成") }}

### 示例插件

一个支持调度任务的插件示例：

::: plugin.samples.integration.scheduled_task.ScheduledTaskPlugin
    options:
        show_bases: False
        show_root_heading: False
        show_root_toc_entry: False
        show_source: True
        members: []
