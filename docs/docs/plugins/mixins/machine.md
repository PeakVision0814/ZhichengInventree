---
title: 机器混合(Machine Mixin)
---

## 机器驱动混合

`MachineDriverMixin` 类用于在 InvenTree 中实现自定义机器驱动程序（或机器类型）。

InvenTree 支持通过使用插件提供的设备驱动程序与[外部机器](../machines/overview.md)集成。

### 获取机器驱动程序

要注册自定义机器驱动程序，必须实现 `get_machine_drivers` 方法。此方法应返回插件支持的机器驱动程序类列表。

::: plugin.base.integration.MachineMixin.MachineDriverMixin.get_machine_drivers
    选项：
      show_bases: False
      show_root_heading: False
      show_root_toc_entry: False
      summary: False
      members: []
      extra:
        show_source: True

默认实现返回一个空列表，表示没有注册自定义机器驱动程序。

### 获取机器类型

要注册自定义机器类型，必须实现 `get_machine_types` 方法。此方法应返回插件支持的机器类型类列表。

::: plugin.base.integration.MachineMixin.MachineDriverMixin.get_machine_types
    选项：
      show_bases: False
      show_root_heading: False
      show_root_toc_entry: False
      summary: False
      members: []
      extra:
        show_source: True

默认实现返回一个空列表，表示没有注册自定义机器类型。

## 示例插件

提供了一个示例插件，它实现了一个简单的[标签打印](../machines/label_printer.md)机器驱动程序：

::: plugin.samples.machines.sample_printer.SamplePrinterMachine
    选项：
        show_bases: False
        show_root_heading: False
        show_root_toc_entry: False
        show_source: True
        members: []
