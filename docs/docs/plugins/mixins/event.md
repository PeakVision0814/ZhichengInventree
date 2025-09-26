---
title: 事件混入（Event Mixin）
---

## EventMixin

`EventMixin` 类使插件能够响应某些触发的事件。

当发生某个（服务器端）事件时，后台工作程序会将事件信息传递给任何继承自 `EventMixin` 基类的插件。

!!! tip "启用事件集成"
    必须首先启用*启用事件集成*选项，以允许插件响应事件。

{{ image("plugin/enable_events.png", "启用事件集成") }}

## 事件

事件使用字符串标识符传递，例如 `build.completed`

传递给接收函数的参数（和关键字参数）完全取决于事件的类型。

!!! info "阅读代码"
    实现对特定事件的响应需要对 InvenTree 代码库有一定了解，特别是与接收到的该事件相关的代码。虽然此处记录了*可用*事件，但要实现对特定事件的响应，您需要阅读代码以了解传递给事件处理程序的数据。

## 通用事件

在某些数据库操作上会生成许多*通用*事件。 每当在数据库中创建、更新或删除数据库对象时，都会生成相应的事件。

#### 对象已创建

当在数据库中创建一个新对象时，会生成一个事件，其事件名称如下：`<app>_<model>.created`，其中 `<model>` 是模型类的名称（例如 `part`、`stockitem` 等）。

该事件使用以下关键字参数调用：

- `model`：已创建对象的模型类
- `id`：已创建对象的主键

**示例：**

创建一个新的 `Part` 对象，其主键为 `123`，从而导致生成以下事件：

```python
trigger_event('part_part.created', model='part', id=123)
```

### 对象已更新

当在数据库中更新一个对象时，会生成一个事件，其事件名称如下：`<app>_<model>.saved`，其中 `<model>` 是模型类的名称（例如 `part`、`stockitem` 等）。

该事件使用以下关键字参数调用：

- `model`：已更新对象的模型类
- `id`：已更新对象的主键

**示例：**

更新一个主键为 `123` 的 `Part` 对象，从而导致生成以下事件：

```python
trigger_event('part_part.saved', model='part', id=123)
```

### 对象已删除

当从数据库中删除一个对象时，会生成一个事件，其事件名称如下：`<app>_<model>.deleted`，其中 `<model>` 是模型类的名称（例如 `part`、`stockitem` 等）。

该事件使用以下关键字参数调用：

- `model`：已删除对象的模型类
- `id`：已删除对象的主键（如果可用）

**示例：**

删除一个主键为 `123` 的 `Part` 对象，从而导致生成以下事件：

```python
trigger_event('part_part.deleted', model='part', id=123)
```

!!! warning "对象已删除"
    请注意，该事件是在从数据库中删除对象 *后* 触发的，因此该对象本身不再可用。

## 特定事件

除了上面列出的*通用*事件外，还有许多其他事件由 InvenTree 代码库中的*特定*操作触发。

可用事件在下面列出的枚举中提供。 请注意，虽然此处记录了事件的名称，但传递给事件处理程序的具体参数将取决于触发的特定事件。

### 构建事件

::: build.events.BuildEvents
    options:
        show_bases: False
        show_root_heading: False
        show_root_toc_entry: False
        show_source: True
        members: []

### 零件事件

::: part.events.PartEvents
    options:
        show_bases: False
        show_root_heading: False
        show_root_toc_entry: False
        show_source: True
        members: []

### 库存事件

::: stock.events.StockEvents
    options:
        show_bases: False
        show_root_heading: False
        show_root_toc_entry: False
        show_source: True
        members: []

### 采购订单事件

::: order.events.PurchaseOrderEvents
    options:
        show_bases: False
        show_root_heading: False
        show_root_toc_entry: False
        show_source: True
        members: []

### 销售订单事件

::: order.events.SalesOrderEvents
    options:
        show_bases: False
        show_root_heading: False
        show_root_toc_entry: False
        show_source: True
        members: []

### 退货订单事件

::: order.events.ReturnOrderEvents
    options:
        show_bases: False
        show_root_heading: False
        show_root_toc_entry: False
        show_source: True
        members: []

### 插件事件

::: plugin.events.PluginEvents
    options:
        show_bases: False
        show_root_heading: False
        show_root_toc_entry: False
        show_source: True
        members: []

## 示例

### 示例插件 - 所有事件

实现类必须至少提供一个 `process_event` 函数：

::: plugin.samples.event.event_sample.EventPluginSample
    options:
        show_bases: False
        show_root_heading: False
        show_root_toc_entry: False
        show_source: True
        members: []

### 示例插件 - 特定事件

如果你只想处理一些特定的事件，你也可以实现 `wants_process_event` 函数来决定是否要处理这个事件。这个函数会被同步执行，所以要注意它应该包含简单的逻辑。

总的来说，这个函数可以大大减少后台工作程序的负担，因为需要处理的事件较少。

::: plugin.samples.event.filtered_event_sample.FilteredEventPluginSample
    options:
        show_bases: False
        show_root_heading: False
        show_root_toc_entry: False
        show_source: True
        members: []
