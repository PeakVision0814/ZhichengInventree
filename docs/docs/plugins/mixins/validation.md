---
标题: 验证混合类（Validation Mixin）
---

## 验证混合类

`ValidationMixin` 类允许插件对数据库中的对象执行自定义验证。

下面描述的任何方法都可以在自定义插件中实现，以提供所需的功能。

!!! info "更多信息"
    如需了解下面描述的任何方法的更多信息，请参考 InvenTree 源代码。[一个可用的工作示例作为起点]({{ sourcefile("src/backend/InvenTree/plugin/samples/integration/validation_sample.py") }})。

!!! info "多插件支持"
    可以同时加载多个支持验证方法的插件。例如，在验证字段时，如果一个插件返回 null 值（`None`），则会查询下一个插件（如果有的话）。

## 模型删除

任何继承 `PluginValidationMixin` 类的模型都会暴露给插件系统，以便进行自定义删除验证。在从数据库中删除模型之前，它首先被传递给插件生态系统以检查是否真的应该被删除。

自定义插件可以实现 `validate_model_deletion` 方法，以在模型被删除之前执行自定义验证。

::: plugin.base.integration.ValidationMixin.ValidationMixin.validate_model_deletion
    options:
      show_bases: False
      show_root_heading: False
      show_root_toc_entry: False
      extra:
        show_source: True
      summary: False
      members: []

## 模型验证

任何继承 `PluginValidationMixin` 混合类的模型都会暴露给插件系统，以便进行自定义验证。在模型保存到数据库（无论是创建还是更新）之前，它首先被传递给插件生态系统进行验证。

任何继承 `ValidationMixin` 的插件都可以实现 `validate_model_instance` 方法，并运行自定义验证程序。

::: plugin.base.integration.ValidationMixin.ValidationMixin.validate_model_instance
    options:
      show_bases: False
      show_root_heading: False
      show_root_toc_entry: False
      extra:
        show_source: True
      summary: False
      members: []

### 错误信息

任何错误信息都必须作为 `ValidationError` 异常抛出。`ValidationMixin` 类提供了 `raise_error` 方法，这是一个简单的包装方法，用于抛出 `ValidationError`

#### 实例错误

为了指示一个 *实例* 验证错误（即验证错误适用于整个模型实例），错误信息的内容应为一个字符串，或字符串的列表。

#### 字段错误

为了指示一个 *字段* 验证错误（即验证错误仅适用于模型实例上的单个字段），错误信息的内容应为一个字典，其中字典的键对应模型的字段。

请注意，一个错误可以适用于多个模型实例字段。

### 示例插件

下面是一个实现 `validate_model_instance` 方法的简单工作示例插件：

```python
from plugin import InvenTreePlugin
from plugin.mixins import ValidationMixin

import part.models


class MyValidationMixin(ValidationMixin, InvenTreePlugin):
    """自定义验证插件。"""

    def validate_model_instance(self, instance, deltas=None):
        """自定义模型验证示例。

        - 零件名称和类别名称必须以相同的字母开头
        - 零件类别描述字段一旦创建后不能缩短
        """

        if isinstance(instance, part.models.Part):
            if category := instance.category:
                if category.name[0] != part.name[0]:
                    self.raise_error({
                        "name": "零件名称和类别名称必须以相同的字母开头"
                    })

        if isinstance(instance, part.models.PartCategory):
            if deltas and 'description' in deltas:
                d_new = deltas['description']['new']
                d_old = deltas['description']['old']

                if len(d_new) < len(d_old):
                    self.raise_error({
                        "description": "描述不能被缩短"
                    })

```

## 字段验证

除了上面提供的通用模型实例验证程序外，以下字段还支持自定义验证程序：

### 零件名称

默认情况下，零件名称不受任何特定命名规范或要求的限制。如果需要自定义验证，则可以实现 `validate_part_name` 方法，以确保零件名称符合所需规范。

如果自定义方法确定零件名称是 *不可接受的*，则应抛出一个 `ValidationError`，该错误将由上游的父调用方法处理。

::: plugin.base.integration.ValidationMixin.ValidationMixin.validate_part_name
    options:
      show_bases: False
      show_root_heading: False
      show_root_toc_entry: False
      extra:
        show_source: True
      summary: False
      members: []

### 零件IPN

零件IPN（内部零件编号）字段的验证通过 `validate_part_ipn` 方法暴露给自定义插件。任何扩展 `ValidationMixin` 类的插件都可以实现此方法，并在IPN值不符合所需规范时抛出 `ValidationError`

::: plugin.base.integration.ValidationMixin.ValidationMixin.validate_part_ipn
    options:
      show_bases: False
      show_root_heading: False
      show_root_toc_entry: False
      extra:
        show_source: True
      summary: False
      members: []

### 零件参数值

[零件参数](../../part/parameter.md) 也可以通过实现 `validate_part_parameter` 方法应用自定义验证规则。如果零件参数值不符合所需规范，实现此方法的插件应抛出一个带有适当信息的 `ValidationError`

::: plugin.base.integration.ValidationMixin.ValidationMixin.validate_part_parameter
    options:
      show_bases: False
      show_root_heading: False
      show_root_toc_entry: False
      extra:
        show_source: True
      summary: False
      members: []

### 批次编号

[批次编号](../../stock/tracking.md#batch-codes) 可以通过自定义插件生成和/或验证。

#### 验证批次编号

`validate_batch_code` 方法允许插件在用户输入的批次编号不符合特定模式时抛出错误。

::: plugin.base.integration.ValidationMixin.ValidationMixin.validate_batch_code
    options:
      show_bases: False
      show_root_heading: False
      show_root_toc_entry: False
      extra:
        show_source: True
      summary: False
      members: []

#### 生成批次编号

可以实现 `generate_batch_code` 方法，根据提供的信息生成新的批次编号。

::: plugin.base.integration.ValidationMixin.ValidationMixin.generate_batch_code
    options:
      show_bases: False
      show_root_heading: False
      show_root_toc_entry: False
      extra:
        show_source: True
      summary: False
      members: []

## 序列号

序列号的要求根据应用程序的不同可能会有很大差异。InvenTree 不尝试提供一个适用于所有情况的序列号实现，而是允许通过插件实现自定义序列号方案。

默认的 InvenTree [序列号系统](../../stock/tracking.md#serial-numbers) 使用一个简单的算法来验证和递增序列号。更复杂的行为可以通过 `ValidationMixin` 插件类和以下自定义方法实现：

#### 序列号验证

可以使用 `validate_serial_number` 方法实现自定义序列号验证。一个 *提议* 的序列号被传递给此方法，该方法有机会抛出 `ValidationError` 以指示序列号无效。

::: plugin.base.integration.ValidationMixin.ValidationMixin.validate_serial_number
    options:
      show_bases: False
      show_root_heading: False
      show_root_toc_entry: False
      extra:
        show_source: True
      summary: False
      members: []

!!! info "库存项"
    如果提供了 `stock_item` 参数，那么该库存项已经被分配了提供的序列号。该库存项在后续检查 *唯一性* 时应被排除。`stock_item` 参数是可选的，如果在没有库存项的上下文中进行序列号验证，它可能是 `None`

##### 示例

继续上面的十六进制示例，该方法可能实现如下：

```python
def validate_serial_number(self, serial: str, part: Part, stock_item: StockItem = None):
    """验证提供的序列号

    参数:
        serial: 提议的序列号（字符串）
        part: 该序列号正在被验证的 Part 实例
        stock_item: 该序列号正在被验证的 StockItem 实例
    """

    try:
        # 尝试整数转换
        int(serial, 16)
    except ValueError:
        raise ValidationError("序列号必须是有效的十六进制值")
```

#### 序列号排序

虽然 InvenTree 支持序列号字段中的任意文本值，但后台会尝试将这些值转换为整数表示，以实现更高效的排序。

自定义插件可以实现 `convert_serial_to_int` 方法，以确定特定的序列号如何转换为整数表示。

::: plugin.base.integration.ValidationMixin.ValidationMixin.convert_serial_to_int
    options:
      show_bases: False
      show_root_heading: False
      show_root_toc_entry: False
      extra:
        show_source: True
      summary: False
      members: []

!!! info "非必需"
    如果未实现此方法，或者序列号无法转换为整数，则排序算法将回退到文本（字符串）值

#### 序列号递增

InvenTree 序列号系统的一个核心组件是 *递增* 序列号的能力 - 以确定序列中的 *下一个* 序列号值。

对于自定义的序列号方案，重要的是提供一个方法，根据当前值生成 *下一个* 序列号。插件可以通过实现 `increment_serial_number` 方法来达到此目的。

::: plugin.base.integration.ValidationMixin.ValidationMixin.increment_serial_number
    options:
      show_bases: False
      show_root_heading: False
      show_root_toc_entry: False
      extra:
        show_source: True
      summary: False
      members: []

!!! info "无效递增"
    如果提供的数字无法递增（或发生错误），该方法应返回 `None`

##### 示例

继续上面的十六进制示例，该方法可能实现如下：

```python
def increment_serial_number(self, serial: str):
    """提供序列中的下一个十六进制数字"""

    try:
        val = int(serial, 16) + 1
        val = hex(val).upper()[2:]
    except ValueError:
        val = None

    return val
```

## 示例插件

一个实现自定义验证程序的示例插件在 InvenTree 源代码中提供：

::: plugin.samples.integration.validation_sample.SampleValidatorPlugin
    options:
        show_bases: False
        show_root_heading: False
        show_root_toc_entry: False
        show_source: True
        members: []
