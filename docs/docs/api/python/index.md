---
标题：Python 接口（Python Interface）
---

## Python 模块

提供了一个 [Python 模块](https://github.com/inventree/inventree-python)，用于使用 REST API 快速开发第三方脚本或应用程序。 该 python 模块处理身份验证和 API 事务，为与数据库数据交互和操作提供了一个非常清晰的界面。

### 特点

- 使用基于令牌的身份验证自动进行身份验证管理
- Pythonic 数据访问
- 本地文件上传
- 用于访问相关模型数据的强大功能

### 安装

inventree python 接口可以通过 [PIP 包管理器](https://pypi.org/project/inventree/) 轻松安装：

```
pip3 install inventree
```

!!! tip "升级"
    要升级到最新版本，请运行 `pip install --upgrade inventree`

或者，可以从 [GitHub](https://github.com/inventree/inventree-python) 下载并从源代码安装。

### 身份验证

针对 InvenTree 服务器进行身份验证很简单：

#### 基本身份验证

使用您的用户名/密码连接，如下所示：

```python
from inventree.api import InvenTreeAPI

SERVER_ADDRESS = 'http://127.0.0.1:8000'
MY_USERNAME = 'not_my_real_username'
MY_PASSWORD = 'not_my_real_password'

api = InvenTreeAPI(SERVER_ADDRESS, username=MY_USERNAME, password=MY_PASSWORD)
```

#### 令牌身份验证

或者，如果您已经拥有访问令牌：

```python
api = InvenTreeAPI(SERVER_ADDRESS, token=MY_TOKEN)
```

#### 环境变量

身份验证变量也可以使用环境变量设置：

- `INVENTREE_API_HOST`
- `INVENTREE_API_USERNAME`
- `INVENTREE_API_PASSWORD`
- `INVENTREE_API_TOKEN`

然后简单地连接，如下所示：

```python
api = InvenTreeAPI()
```

### 检索数据

一旦与 InvenTree 服务器建立连接，查询单个项目就会变得很简单。

#### 单个项目

如果已知对象的主键，则从数据库中检索它的方法如下：

```python
from inventree.part import PartCategory

category = PartCategory(api, 10)
```

#### 多个项目

可以通过使用给定类的 `list` 方法来查询数据库项目。 请注意，可以应用任意过滤器参数（如[InvenTree API](../index.md) 中所指定）来过滤返回的结果。

```python
from inventree.part import Part
from inventree.stock import StockItem

parts = Part.list(api, category=10, assembly=True)
items = StockItem.list(api, location=4, part=24)
```

上面的 `items` 变量提供了一个 `StockItem` 对象列表。

#### 按父项筛选

在基于树的模型中，可以使用 parent 关键字来筛选子项目：

```python
from inventree.part import PartCategory

child_categories = PartCategory.list(api, parent=10)
```

可以通过传递空字符串作为父过滤器来查询顶级项目：

```python
from inventree.part import PartCategory

parent_categories = PartCategory.list(api, parent='')
```

### 项目属性

可用的模型属性由内省 [API 元数据](../metadata.md) 确定。 要查看 python 界面中给定数据库模型类型的可用字段（属性），请使用 `fieldNames` 和 `fieldInfo` 方法，如下所示：

```python
from inventree.api import InvenTreeAPI
from inventree.part import Part

api = InvenTreeAPI("http://localhost:8000", username="admin", password="inventree")

fields = Part.fieldNames(api)

for field in Part.fieldNames(api):
    print(field, '->', Part.fieldInfo(field, api))
```

```
active -> {'type': 'boolean', 'required': True, 'read_only': False, 'label': 'Active', 'help_text': 'Is this part active?', 'default': True, 'max_length': None}
allocated_to_build_orders -> {'type': 'float', 'required': True, 'read_only': True, 'label': 'Allocated to build orders'}
allocated_to_sales_orders -> {'type': 'float', 'required': True, 'read_only': True, 'label': 'Allocated to sales orders'}
assembly -> {'type': 'boolean', 'required': True, 'read_only': False, 'label': 'Assembly', 'help_text': 'Can this part be built from other parts?', 'default': False, 'max_length': None}
category -> {'type': 'related field', 'required': True, 'read_only': False, 'label': 'Category', 'model': 'partcategory', 'api_url': '/api/part/category/', 'filters': {}, 'help_text': 'Part category', 'max_length': None}
component -> {'type': 'boolean', 'required': True, 'read_only': False, 'label': 'Component', 'help_text': 'Can this part be used to build other parts?', 'default': True, 'max_length': None}
default_expiry -> {'type': 'integer', 'required': True, 'read_only': False, 'label': 'Default Expiry', 'help_text': 'Expiry time (in days) for stock items of this part', 'min_value': 0, 'max_value': 2147483647, 'default': 0, 'max_length': None}
...
variant_stock -> {'type': 'float', 'required': True, 'read_only': True, 'label': 'Variant stock'}
```

### 项目方法

一旦从数据库中检索到一个对象，它的相关对象可以通过提供的辅助方法返回：

```python
part = Part(api, 25)
stock_items = part.getStockItems()
```

某些类还具有用于执行某些操作的辅助函数，例如上传文件附件或测试结果：

```python
stock_item = StockItem(api, 1001)
stock_item.uploadTestResult("Firmware", True, value="0x12345678", attachment="device_firmware.bin")
```

#### 发现方法

您可以通过[阅读源代码](https://github.com/inventree/inventree-python)或在交互式终端中使用 `dir()` 函数来确定可用的方法。

### 进一步阅读

[InvenTree Python 接口](https://github.com/inventree/inventree-python) 是开源的，并且有完善的文档。 学习的最佳方法是阅读源代码并亲自尝试！
