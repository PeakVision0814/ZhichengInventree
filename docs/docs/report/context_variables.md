---
title: 上下文变量（Context Variables）
---

## 上下文变量

上下文变量在渲染时提供给每个模板。可用的上下文变量取决于正在渲染模板的模型类型。

### 全局上下文

除了特定于模型的上下文变量之外，以下全局上下文变量可用于所有模板：

{{ report_context("base", "global") }}

::: report.models.ReportTemplateBase.base_context
    options:
        show_source: True

### 报告上下文

除了[全局上下文](#global-context)之外，所有*报告*模板都可以访问以下上下文变量：

{{ report_context("base", "report") }}

使用 `merge` 上下文变量时，所选项目在 `instances` 列表中可用。{{ templatefile("report/inventree_stock_report_merge.html") }} 展示了一个完整的例子。要访问单个项目属性，您可以循环遍历 `instances` 或通过索引访问它们，例如 `instance.0.name`。

下面是一个示例模板，该模板为某些选定的零件生成单个报告。每个零件占据表格中的一行

```html
{% raw %}
<h2>所选零件的合并报告</h2>
<table>
  <tr>
    <th>名称</th>
    <th>描述</th>
  </tr>
  {% for part in instances %}
    <tr>
      <td>{{ part.name }}</td>
      <td>{{ part.description }}</td>
    </tr>
  {% endfor %}
</table>
{% endraw %}
```

请注意，自定义插件也可能会向报告上下文中添加其他上下文变量。

::: report.models.ReportTemplate.get_context
    options:
        show_source: True

### 标签上下文

除了[全局上下文](#global-context)之外，所有*标签*模板都可以访问以下上下文变量：

{{ report_context("base", "label") }}

请注意，自定义插件也可能会向标签上下文中添加其他上下文变量。

::: report.models.LabelTemplate.get_context
    options:
        show_source: True

## 模板类型

模板（无论是用于生成[报告](./report.md)还是[标签](./labels.md)）都是针对特定的“模型”类型进行渲染的。支持以下模型类型，并且可以针对它们渲染模板：

| 模型类型 | 描述 |
| --- | --- |
| company | Company 实例 |
| [build](#build-order) | [Build Order](../manufacturing/build.md) 实例 |
| [buildline](#build-line) | [Build Order Line Item](../manufacturing/build.md) 实例 |
| [salesorder](#sales-order) | [Sales Order](../sales/sales_order.md) 实例 |
| [returnorder](#return-order) | [Return Order](../sales/return_order.md) 实例 |
| [purchaseorder](#purchase-order) | [Purchase Order](../purchasing/purchase_order.md) 实例 |
| [stockitem](#stock-item) | [StockItem](../stock/index.md#stock-item) 实例 |
| [stocklocation](#stock-location) | [StockLocation](../stock/index.md#stock-location) 实例 |
| [part](#part) | [Part](../part/index.md) 实例 |

### 公司

针对 Company 实例打印报告或标签时，可以使用以下上下文变量：

{{ report_context("models", "company") }}

::: company.models.Company.report_context
    options:
        show_source: True

### 制造订单

针对 [Build Order](../manufacturing/build.md) 对象打印报告或标签时，可以使用以下上下文变量：

{{ report_context("models", "build") }}

::: build.models.Build.report_context
    options:
        show_source: True

### 制造订单行

针对 [BuildOrderLineItem](../manufacturing/build.md) 对象打印报告或标签时，可以使用以下上下文变量：

{{ report_context("models", "buildline") }}

::: build.models.BuildLine.report_context
    options:
        show_source: True

### 销售订单

针对 [SalesOrder](../sales/sales_order.md) 对象打印报告或标签时，可以使用以下上下文变量：

{{ report_context("models", "salesorder") }}

::: order.models.Order.report_context
    options:
        show_source: True

### 销售订单发货

当针对 [SalesOrderShipment](../sales/sales_order.md#sales-order-shipments) 对象打印报告或标签时，可以使用以下上下文变量：

{{ report_context("models", "salesordershipment") }}

::: order.models.SalesOrderShipment.report_context
    options:
        show_source: True

### 退货订单

针对 [ReturnOrder](../sales/return_order.md) 对象打印报告或标签时，可以使用以下上下文变量：

{{ report_context("models", "returnorder") }}

### 采购订单

针对 [PurchaseOrder](../purchasing/purchase_order.md) 对象打印报告或标签时，可以使用以下上下文变量：

{{ report_context("models", "purchaseorder") }}

### 库存项目

针对 [StockItem](../stock/index.md#stock-item) 对象打印报告或标签时，可以使用以下上下文变量：

{{ report_context("models", "stockitem") }}

::: stock.models.StockItem.report_context
    options:
        show_source: True

### 库存位置

针对 [StockLocation](../stock/index.md#stock-location) 对象打印报告或标签时，可以使用以下上下文变量：

{{ report_context("models", "stocklocation") }}

::: stock.models.StockLocation.report_context
    options:
        show_source: True

### 零件

针对 [Part](../part/index.md) 对象打印报告或标签时，可以使用以下上下文变量：

{{ report_context("models", "part") }}

::: part.models.Part.report_context
    options:
        show_source: True

## 模型变量

除了直接提供给每个模板的上下文变量之外，每种模型类型都有许多可以通过模板访问的属性和方法。

对于每种模型类型，下面列出了最常用的属性的子集。 有关属性和方法的完整列表，请参阅特定模型类型的源代码。

### 零件

#### 零件

每个零件对象都可以访问有关该零件的大量上下文变量。 从模板中访问 `Part` 对象时，将提供以下上下文变量。

| 变量 | 描述 |
|----------|-------------|
| name | 此零件的简称 |
| full_name | 此零件的全名（如果 IPN 不为空，则包括 IPN；如果 variant 不为空，则包括 variant） |
| variant | 此零件的可选变体号 - 对于零件名称必须是唯一的 |
| category | 此零件所属的 [PartCategory](#part-category) 对象 |
| description | 零件的较长形式描述 |
| keywords | 用于改进零件搜索结果的可选关键字 |
| IPN | 内部零件号（可选） |
| revision | 零件修订版 |
| is_template | 如果为 True，则此零件是“模板”零件 |
| link | 链接到包含有关此零件的更多信息的外部页面（例如，内部 Wiki） |
| image | 此零件的图像 |
| default_location | 正常存储该项目的默认 [StockLocation](#stock-location) 对象（可以为空） |
| default_supplier | 应用于采购和库存此零件的默认 [SupplierPart](#supplierpart) |
| default_expiry | 此零件的任何 StockItem 实例的默认到期时间 |
| minimum_stock | 要保持库存的最小首选数量 |
| units | 此零件的计量单位（默认为“pcs”） |
| salable | 此零件可以出售给客户吗？ |
| assembly | 可以从其他零件构建此零件吗？ |
| component | 可以使用此零件来制造其他零件吗？ |
| purchaseable | 可以从供应商处购买此零件吗？ |
| trackable | 可跟踪零件可以分配唯一的序列号等 |
| active | 此零件是否处于活动状态？ 零件已停用，而不是已删除 |
| virtual | 此零件是“虚拟”的吗？ 例如，软件产品或类似产品 |
| notes | 此零件的附加备注字段 |
| creation_date | 将此零件添加到数据库的日期 |
| creation_user | 将此零件添加到数据库的用户 |
| responsible | 负责此零件的用户（可选） |
| starred | 零件是否已加星标 |
| disabled | 零件是否已禁用 |
| total_stock | 库存总量 |
| quantity_being_built | 正在构建的数量 |
| required_build_order_quantity | 制造订单所需的数量 |
| allocated_build_order_quantity | 为制造订单分配的数量 |
| build_order_allocations | 查询集，其中包含该零件的所有制造订单分配 |
| required_sales_order_quantity | 销售订单所需的数量 |
| allocated_sales_order_quantity | 为销售订单分配的数量 |
| available | 零件是否可用 |
| on_order | 订购中的数量 |
| required | 制造订单和销售订单所需的总数量 |
| allocated | 为制造订单和销售订单分配的总数量 |

#### 零件类别

| 变量 | 描述 |
|----------|-------------|
| name | 此类别的名称 |
| parent | 父类别 |
| default_location | 此类别或子类别中零件的默认 [StockLocation](#stock-location) 对象 |
| default_keywords | 在此类别中创建的零件的默认关键字 |

### 库存

#### 库存项目

| 变量 | 描述 |
|----------|-------------|
| parent | 链接到从中创建此 StockItem 的另一个 [StockItem](#stock-item) |
| uid | 包含唯一 ID 的字段，该 ID 映射到第三方标识符（例如，条形码） |
| part | 链接到此 [StockItem](#stock-item) 是其实例的主抽象 [Part](#part) |
| supplier_part | 链接到特定的 [SupplierPart](#supplierpart)（可选） |
| location | 此 [StockItem](#stock-item) 所在的 [StockLocation](#stock-location) |
| quantity | 库存单位的数量 |
| batch | 此 [StockItem](#stock-item) 的批号 |
| serial | 此 [StockItem](#stock-item) 的唯一序列号 |
| link | 链接到外部资源的可选 URL |
| updated | 上次更新此库存项目的日期（自动） |
| expiry_date | [StockItem](#stock-item) 的到期日期（可选） |
| stocktake_date | 此项目的上次库存盘点的日期 |
| stocktake_user | 执行最近库存盘点的用户 |
| review_needed | 如果 [StockItem](#stock-item) 需要审核，则标记 |
| delete_on_deplete | 如果为 True，则当库存水平降至零时，将删除 [StockItem](#stock-item) |
| status | 此 [StockItem](#stock-item) 的状态（参考：InvenTree.status_codes.StockStatus） |
| status_label | 状态的文本表示形式，例如“OK” |
| notes | 额外备注字段 |
| build | 链接到制造（如果此库存项目是从制造创建的） |
| is_building | 布尔字段，指示此库存项目当前是否正在制造（或是否“在生产中”） |
| purchase_order | 链接到 [PurchaseOrder](#purchase-order)（如果此库存项目是从 PurchaseOrder 创建的） |
| infinite | 如果为 True，则永远不会耗尽此 [StockItem](#stock-item) |
| sales_order | 链接到 [SalesOrder](#sales-order) 对象（如果 StockItem 已分配给 SalesOrder） |
| purchase_price | 此 [StockItem](#stock-item) 的单位购买价格 - 这是购买时的单价（如果此项目是从外部供应商处购买的） |
| packaging | StockItem 的包装方式的描述（例如，“卷轴”、“散装”、“磁带”等） |

#### 库存位置

| 变量 | 描述 |
|----------|-------------|
| barcode | 简短的有效负载数据（例如，对于标签）。 示例：`{"stocklocation": 826}`，其中 826 是主键|
| description | 位置的描述 |
| icon | 图标的名称（如果已设置），例如 fas fa-warehouse |
| item_count | 仅返回此位置中库存项目的数量 |
| name | 位置的名称。 这只是此位置的名称，而不是路径 |
| owner | 位置的所有者（如果有）。 只能在管理界面中分配所有者 |
| parent | 父位置。 如果它已经是最高位置，则返回 None |
| path | 包含从最高父级开始的层次结构的位置的查询集 |
| pathstring | 包含以斜杠分隔的路径的所有名称的字符串，例如 A/B/C |
| structural | 如果位置是结构性的，则为 True |

### 供应商

#### 公司

| 变量 | 描述 |
|----------|-------------|
| name | 公司名称 |
| description | 较长形式的描述 |
| website | 公司网站的 URL |
| primary_address | 标记为主要地址的 [Address](#address) 对象 |
| address | 主要地址的字符串格式 |
| contact | 联系人姓名 |
| phone | 联系人电话号码 |
| email | 联系人电子邮件地址 |
| link | 指向公司的第二个 URL（实际上只能在管理界面中访问） |
| notes | 关于公司的额外备注（实际上只能在管理界面中访问） |
| is_customer | 布尔值，该公司是否是客户 |
| is_supplier | 布尔值，该公司是否是供应商 |
| is_manufacturer | 布尔值，该公司是否是制造商 |
| currency_code | 公司的默认货币 |
| parts | 查询集，其中包含公司提供的所有零件 |

#### 地址

| 变量 | 描述 |
|----------|-------------|
| line1 | 邮政地址的第一行 |
| line2 | 邮政地址的第二行 |
| postal_code | 城市的邮政编码 |
| postal_city | 城市名称 |
| country | 国家名称 |

#### 联系方式

| 变量 | 描述 |
|----------|-------------|
| company | 联系人所属的公司对象 |
| name | 联系人的名字和姓氏 |
| phone | 电话号码 |
| email | 电子邮件地址 |
| role | 联系人的角色 |

#### 供应商零件

| 变量 | 描述 |
|----------|-------------|
| part | 链接到主零件（过时） |
| source_item | 链接到此 [SupplierPart](#supplierpart) 实例的采购 [StockItem](#stock-item) |
| supplier | 供应此零件的 [Company](#company) |
| SKU | 库存单位（供应商零件号） |
| link | 链接到此供应商零件的外部网站 |
| description | 描述性备注字段 |
| note | 较长形式的备注字段 |
| base_cost | 添加到订单的独立于数量的基本费用，例如“卷绕费” |
| multiple | 提供零件的倍数 |
| lead_time | 供应商交货时间 |
| packaging | 提供零件的包装，例如“卷轴” |
| pretty_name | IPN、供应商名称、供应商 SKU 和（如果不是 null）制造商字符串用 `|` 连接。 例如，`P00037 | Company | 000021` |
| unit_pricing | 一件产品的价格。 |
| price_breaks | 按正确的顺序返回关联的价格折扣 |
| has_price_breaks | 此 [SupplierPart](#supplierpart) 是否有价格折扣 |
| manufacturer_string | 为此 [SupplierPart](#supplierpart) 格式化 MPN 字符串。 连接制造商名称和零件号。 |

### 用户

| 变量 | 描述 |
|----------|-------------|
| username | 用户的用户名 |
| fist_name | 用户的名字 |
| last_name | 用户的姓氏 |
| email | 用户的电子邮件地址 |
| pk | 用户的主键 |
