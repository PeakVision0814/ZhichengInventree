---
title: 报告混入（Report Mixin）
---

## 报告混入

`ReportMixin` 类为插件提供了扩展自定义[报告模板](../../report/report.md)功能的能力。实现 ReportMixin 混入类的插件可以向报告模板添加自定义上下文数据以进行渲染。

### 添加报告上下文

实现 ReportMixin 混入的插件可以定义 `add_report_context` 方法，允许在打印时将自定义上下文数据添加到报告模板中。

### 添加标签上下文

此外，`add_label_context` 方法允许在打印时将自定义上下文数据添加到标签模板中。

### 示例插件

一个为报告模板提供额外上下文数据的示例插件如下：

::: plugin.samples.integration.report_plugin_sample.SampleReportPlugin
    options:
        show_bases: False
        show_root_heading: False
        show_root_toc_entry: False
        show_source: True
        members: []
