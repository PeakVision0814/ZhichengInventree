---
title: 数据导出 Mixin（Data Export Mixin）
---

## DataExportMixin

`DataExportMixin` 类提供了一个插件，使其能够自定义数据导出过程。[InvenTree API](../../api/index.md) 提供了一种集成方法，可以将数据集导出到表格文件中。默认的导出过程是通用的，只是简单地将通过 API 呈现的数据导出为表格文件格式。

自定义数据导出插件允许调整此过程：

- 可以添加或删除数据列
- 可以删除或添加行
- 可以执行自定义计算或注释。

### 支持的导出类型

每个插件都可以使用 `supports_export` 方法来指示支持哪些数据集。这允许插件动态指定是否可以由用户为给定的导出会话选择它。

::: plugin.base.integration.DataExport.DataExportMixin.supports_export
    options:
      show_bases: False
      show_root_heading: False
      show_root_toc_entry: False
      summary: False
      members: []
      extra:
        show_source: True

默认实现对所有数据类型返回 `True`。

### 文件名生成

`generate_filename` 方法为导出的文件构造文件名。

::: plugin.base.integration.DataExport.DataExportMixin.generate_filename
    options:
      show_bases: False
      show_root_heading: False
      show_root_toc_entry: False
      summary: False
      members: []
      extra:
        show_source: True

### 调整列

`update_headers` 方法允许插件调整选择要导出到文件的列。

::: plugin.base.integration.DataExport.DataExportMixin.update_headers
    options:
      show_bases: False
      show_root_heading: False
      show_root_toc_entry: False
      summary: False
      members: []
      extra:
        show_source: True

### Queryset 过滤

`filter_queryset` 方法允许插件在导出之前，为数据库查询提供自定义过滤。

::: plugin.base.integration.DataExport.DataExportMixin.filter_queryset
    options:
      show_bases: False
      show_root_heading: False
      show_root_toc_entry: False
      summary: False
      members: []
      extra:
        show_source: True

### 导出数据

`export_data` 方法执行将 [Django QuerySet]({% include "django.html" %}/ref/models/querysets/) 转换为可由 [tablib](https://tablib.readthedocs.io/en/stable/) 库处理的数据集的步骤。

::: plugin.base.integration.DataExport.DataExportMixin.export_data
    options:
      show_bases: False
      show_root_heading: False
      show_root_toc_entry: False
      summary: False
      members: []
      extra:
        show_source: True

请注意，默认实现仅使用提供的序列化器类的内置制表功能。在大多数情况下，这已足够。

## 自定义导出选项

为了向用户提供自定义选项，以在 *导出时* 控制导出过程的行为，插件可以定义自定义序列化器类。

要启用此功能，请在插件类上定义一个 `ExportOptionsSerializer` 属性，该属性指向 DRF 序列化器类。有关更多信息，请参阅以下示例。

### 内置导出器类

InvenTree 提供了以下内置数据导出器类。

### InvenTreeExporter

一个通用的导出器类，它只是将 API 输出序列化到数据文件中。

::: plugin.builtin.exporter.inventree_exporter.InvenTreeExporter
    options:
        show_bases: False
        show_root_heading: False
        show_root_toc_entry: False
        show_source: True
        members: []

### BOM 导出器

一个自定义导出器，仅支持 [物料清单](../../manufacturing/bom.md) 导出。

::: plugin.builtin.exporter.bom_exporter.BomExporterPlugin
    options:
        show_bases: False
        show_root_heading: False
        show_root_toc_entry: False
        show_source: True
        members: []

## 源代码

`DataExportMixin` 类的完整源代码：

{{ includefile("src/backend/InvenTree/plugin/base/integration/DataExport.py", title="DataExportMixin") }}
