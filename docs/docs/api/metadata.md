---
标题：模型元数据（Model Metadata）
---

## 模型元数据

API 是*自描述的*，因为它提供了关于任何给定端点上可用的各种字段的元数据。外部应用程序（例如 [Python 接口](../api/python/index.md)）可以内省 API，以确定有关模型字段的信息。

!!! tip "API 表单"
    InvenTree Web 界面中实现的各种表单大量使用了此元数据功能。

### 请求元数据

要请求有关特定 API 端点的元数据，只需对 API URL 执行 `OPTIONS` 方法请求。

例如，要查看用于创建新的 [零件类别](../part/index.md#part-category) 的可用元数据，对 `/api/part/category/` 的 `OPTIONS` 请求会产生：

{{ image("api/api_category_options.png", "零件类别选项") }}

您可以在这里看到可用于此 API 端点的各种字段的详细列表。

## 元数据信息

`OPTIONS` 端点提供以下信息：

| 条目 | 描述 |
| --- | --- |
| name | API 端点的人类可读名称 |
| description | 端点的描述性细节，从 Python 文档字符串中提取 |
| actions | 包含可用的 HTTP 操作和字段信息（见下文） |

提供了每个字段的可用属性的特定详细信息：

{{ image("api/api_metadata_fields.png", "元数据字段") }}

### 字段类型

支持的字段类型有：

| 字段类型 | 描述 |
| --- | --- |
| string | 文本数据 |
| boolean | true / false 值 |
| integer | 整数 |
| float | 浮点数 |
| related field | 数据库中外键关系的主键值 |

### 字段属性

每个命名字段提供有关可用属性的信息：

| 属性 | 描述 |
| --- | --- |
| type | 定义 [字段类型](#字段类型) |
| default | 此字段的默认值。如果没有提供值，将假定使用此值 |
| required | 布尔值，表示是否必须提供此字段 |
| read_only | 布尔值，表示此字段是否可写 |
| label | 此字段的人类可读描述性标签。 |
| help_text | 此字段的长格式描述符。 |
| min_value | 允许的最小值（对于数字字段） |
| max_value | 允许的最大值（对于数字字段） |
| max_length | 允许的最大长度（对于文本字段） |
| model | 数据库模型的名称，如果此字段表示外键关系 |
| api_url | 相关模型的 API URL，如果此字段表示外键关系 |
| filters | 字段的 API 过滤器，如果此字段表示外键关系 |

!!! tip "字段名称"
    字段名称是用于定义字段本身的*键*

!!! info "可用属性"
    某些属性可能不适用于特定字段

## 翻译

字段 *label* 和 *help text* 值使用 [社区贡献的翻译](https://crowdin.com/project/inventree) 进行本地化。所需的区域设置信息是从 API 请求本身确定的，这意味着自动提供翻译后的值。

例如，相同的表单（在 Web 界面中）通过相同的 API 请求提供，区域设置信息“动态”确定：

{{ image("api/api_english.png", "API 表单（英文）") }}
{{ image("api/api_german.png", "API 表单（德文）") }}
