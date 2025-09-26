---
title: 条形码混合类（Barcode Mixin）
---

## BarcodeMixin

InvenTree 支持通过 **条形码插件** 接口解码任意条形码数据和生成内部条形码格式。POST 到 `/api/barcode/` 端点的条形码数据将提供给所有已加载的条形码插件，并且第一个成功解释条形码数据的插件将向客户端返回响应。

InvenTree 可以生成原生 QR 码来表示数据库对象（例如，单个库存项目）。然后，可以使用此条形码在数据库中执行库存项目或位置的快速查找。客户端应用程序（例如 InvenTree 移动应用程序）扫描条形码，并将条形码数据发送到 InvenTree 服务器。然后，服务器使用 **InvenTreeBarcodePlugin**（位于 `src/backend/InvenTree/plugin/builtin/barcodes/inventree_barcode.py`）来解码提供的条形码数据。

任何第三方条形码都可以通过编写匹配的插件来解码条形码数据。然后，这些插件可以执行服务器端操作或将 JSON 响应渲染回客户端以进行进一步操作。

条形码集成的一些可能用途示例：

- 通过扫描物品箱上的条形码进行库存查找
- 通过扫描供应商条形码接收针对采购订单的货物
- 执行库存调整操作（例如，每当扫描条形码时从库存中取出 10 个零件）

条形码数据以如下方式 POST 到服务器：

```
POST {
    barcode_data: "[(>插件知道如何处理的某些条形码数据"
}
```

### 内置插件

InvenTree 服务器包含一个内置条形码插件，可以生成和解码 QR 码。默认情况下启用此插件。

::: plugin.builtin.barcodes.inventree_barcode.InvenTreeInternalBarcodePlugin
    options:
        show_bases: False
        show_root_heading: False
        show_root_toc_entry: False
        show_source: True
        members: []


### 示例插件

请在下面找到一个非常简单的示例，用于在条形码以 `PART-` 开头时返回一个零件

```python
from plugin import InvenTreePlugin
from plugin.mixins import BarcodeMixin
from part.models import Part

class InvenTreeBarcodePlugin(BarcodeMixin, InvenTreePlugin):

    NAME = "MyBarcode"
    TITLE = "我的条形码"
    DESCRIPTION = "支持条形码"
    VERSION = "0.0.1"
    AUTHOR = "Michael"

    def scan(self, barcode_data):
        if barcode_data.startswith("PART-"):
            try:
                pk = int(barcode_data.split("PART-")[1])
                instance = Part.objects.get(pk=pk)
                label = Part.barcode_model_type()

                return {label: instance.format_matched_response()}
            except Part.DoesNotExist:
                pass
```

要尝试它，只需将文件复制到 src/InvenTree/plugins 并重启服务器。打开扫描条形码窗口并开始扫描代码或手动输入文本。每次达到超时时，插件将执行并打印出结果。超时可以在 `设置->条形码支持->条形码输入延迟` 中更改。

### 自定义内部格式

要实现自定义内部条形码格式，需要重写 Barcode Mixin 中的 `generate(...)` 方法。然后可以在 `系统设置 > 条形码 > 条形码生成插件` 中选择插件。

```python
from InvenTree.models import InvenTreeBarcodeMixin
from plugin import InvenTreePlugin
from plugin.mixins import BarcodeMixin

class InvenTreeBarcodePlugin(BarcodeMixin, InvenTreePlugin):
    NAME = "MyInternalBarcode"
    TITLE = "我的内部条形码"
    DESCRIPTION = "支持自定义内部条形码"
    VERSION = "0.0.1"
    AUTHOR = "InvenTree contributors"

    def generate(self, model_instance: InvenTreeBarcodeMixin):
        return f'{model_instance.barcode_model_type()}: {model_instance.pk}'
```

!!! info "需要扫描实现"
    还需要实现自定义格式的解析，以便生成的 QR 码的扫描可以解析为正确的零件。
