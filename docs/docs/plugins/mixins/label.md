---
title: 标签混合类(Label Mixin)
---

## LabelPrintingMixin

`LabelPrintingMixin` 类允许插件提供自定义标签打印功能。标签打印插件的具体实现非常灵活，允许以下功能（作为一个起点）：

- 将单个标签打印到文件，并允许用户下载
- 将多个标签合并到单个页面上
- 支持专有的标签纸格式
- 将标签打印卸载到外部打印机

### 入口点

当针对特定插件打印标签时，入口点是 `print_labels` 方法。此方法的默认实现会迭代每个提供的项目，渲染 PDF，并为每个项目调用 `print_label` 方法，从而提供渲染后的 PDF 数据。

`print_labels` 和 `print_label` 方法都可以被插件覆盖，从而实现复杂的功能。

例如，可以重新实现 `print_labels` 方法，将所有标签合并到单个更大的页面中，并返回单个页面以进行打印。

### 返回类型

`print_labels` 方法*必须*返回一个 JsonResponse 对象。如果该方法未返回此类响应，服务器将引发错误。

### 文件生成

如果标签打印插件生成了一个真实的文件，则应将其作为 `LabelOutput` 实例存储在数据库中，并在 JsonResponse 结果中的 'file' 键下返回。

例如，内置的 `InvenTreeLabelPlugin` 插件生成一个 PDF 文件，该文件包含所有提供的标签连接在一起。下面显示了该代码的片段（有关完整详细信息，请参阅源代码）：

```python
# 将生成的文件保存到数据库
output = LabelOutput.objects.create(
    label=output_file,
    user=request.user
)

return JsonResponse({
    'file': output.label.url,
    'success': True,
    'message': f'{len(items)} 个标签已生成'
})
```

### 后台打印

对于某些标签打印过程（例如将打印卸载到外部网络打印机），最好使用后台工作进程，而不是阻塞前端服务器。
该插件提供了一种简便的方法，可以将打印卸载到后台线程。

只需覆盖类属性 `BLOCKING_PRINT`，如下所示：

```python
class MyPrinterPlugin(LabelPrintingMixin, InvenTreePlugin):
    BLOCKING_PRINT = False
```

如果未更改 `print_labels` 方法，则这将在后台工作线程中运行 `print_label` 方法。

!!! info "示例插件"
    查看 [inventree-brother-plugin](https://github.com/inventree/inventree-brother-plugin)，它为兄弟 QL 和 PT 系列网络标签打印机提供本机支持

!!! tip "自定义代码"
    如果您的插件覆盖了 `print_labels` 方法，则必须确保将标签打印正确地卸载到后台工作线程。查看插件混合类中的 `offload_label` 方法，以了解如何实现此目的。

### 打印选项

打印插件可以将自定义选项定义为一个名为 `PrintingOptionsSerializer` 的序列化器类，该类会显示在打印屏幕上，并作为名为 `printing_options` 的 kwarg 传递给 `print_labels` / `print_label` 函数。这可以用于例如，让用户为每个打印作业动态选择标签的方向、颜色模式等等。
以下简单示例演示了如何实现方向选择。有关如何定义字段的更多信息，请参阅 django rest framework (DRF) [文档](https://www.django-rest-framework.org/api-guide/fields/)。

```py
from rest_framework import serializers

class MyLabelPrinter(LabelPrintingMixin, InvenTreePlugin):
    ...

    class PrintingOptionsSerializer(serializers.Serializer):
        orientation = serializers.ChoiceField(choices=[
            ("landscape", "Landscape"),
            ("portrait", "Portrait"),
        ])

    def print_label(self, **kwargs):
        print(kwargs["printing_options"]) # -> {"orientation": "landscape"}
        ...
```

!!! tip "动态返回序列化器实例"
    如果您的插件想要根据请求动态公开选项，则可以实现 `get_printing_options_serializer` 函数，如果定义了 `PrintingOptionsSerializer` 类，该函数默认返回该类的实例。

### 辅助方法

该插件类提供了许多其他辅助方法，这些方法对于生成标签可能很有用：

| 方法 | 描述 |
| --- | --- |
| render_to_pdf | 将标签模板渲染为内存中的 PDF 对象 |
| render_to_html | 将标签模板渲染为原始 HTML 字符串 |
| render_to_png | 将 PDF 数据转换为内存中的 PNG 图像 |

!!! info "使用源代码"
    这些方法可用于更复杂的实现 - 有关更多信息，请参阅源代码！

### 合并标签

要将多个标签合并（组合）到单个输出中（例如，在单张纸上打印多个标签），插件必须覆盖 `print_labels` 方法并实现所需的功能。

## 集成

### Web 集成

如果启用了标签打印插件，则可以直接从 InvenTree Web 界面使用它们：

{{ image("plugin/print_label_select_plugin.png", "通过插件打印标签") }}

### App 集成

标签打印插件还允许通过 [移动应用程序](../../app/stock.md#print-label) 直接打印标签。

## 实施

可以通过简单地提供 `print_label` 方法来实现实现了 `LabelPrintingMixin` 混合类的插件。

### 简单示例

```python
from dummy_printer import printer_backend

class MyLabelPrinter(LabelPrintingMixin, InvenTreePlugin):
    """
    一个简单的示例插件，它为虚拟打印机提供支持。

    更复杂的插件将与实际打印机通信！
    """

    NAME = "MyLabelPrinter"
    SLUG = "mylabel"
    TITLE = "一个虚拟打印机"

    # 将 BLOCKING_PRINT 设置为 false 以立即返回
    BLOCKING_PRINT = False

    def print_label(self, **kwargs):
        """
        将标签发送到打印机

        kwargs:
            pdf_data: 渲染标签的原始 PDF 数据
            filename: 此 PDF 标签的文件名
            label_instance: 触发 print_label() 方法的标签模型的实例
            item_instance: 针对其打印标签的数据库模型的实例
            user: 触发此打印作业的用户
            width: 标签的预期宽度（以毫米为单位）
            height: 标签的预期高度（以毫米为单位）
            printing_options: 为 PrintingOptionsSerializer 中定义的此打印作业设置的打印选项
        """

        width = kwargs['width']
        height = kwargs['height']

        # 此虚拟打印机支持打印原始图像文件
        printer_backend.print(png_file, w=width, h=height)
```

### 默认插件

InvenTree 开箱即用地提供了 `InvenTreeLabelPlugin`，它生成一个 PDF 文件，用户可以立即下载该文件。

默认插件还具有一个 *DEBUG* 模式，该模式生成原始 HTML 输出，而不是 PDF。这对于跟踪标签中的任何模板渲染错误很有用。

::: plugin.builtin.labels.inventree_label.InvenTreeLabelPlugin
    options:
        show_bases: False
        show_root_heading: False
        show_root_toc_entry: False
        show_source: True
        members: []

### 可用数据

*标签*数据以 `PDF` 和 `PNG` 格式提供给插件。这提供了与各种标签打印机的“开箱即用”的兼容性。转换成其他格式（如果需要）留给插件开发人员。

上面代码示例中记录了提供给 `print_label` 函数的其他参数。
