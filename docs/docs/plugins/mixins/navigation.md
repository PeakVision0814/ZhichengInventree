---
title: 导航混合(Navigation Mixin)
---

## 导航混合

使用类常量 `NAVIGATION` 定义一个链接数组，这些链接应添加到 InvenTrees 导航标题中。
该数组必须至少包含一个字典，其中至少为每个元素定义一个名称和一个链接。链接必须格式化为 URL 模式名称查找——不能直接链接到外部站点。可选的图标必须是对图标的类引用。

``` python
class MyNavigationPlugin(NavigationMixin, InvenTreePlugin):

    NAME = "NavigationPlugin"

    NAVIGATION = [
        {'name': 'SampleIntegration', 'link': 'plugin:sample:hi', 'icon': 'ti ti-box'},
    ]

    NAVIGATION_TAB_NAME = "示例导航"
    NAVIGATION_TAB_ICON = 'ti ti-plus-circle'
```

可选的类常量 `NAVIGATION_TAB_NAME` 和 `NAVIGATION_TAB_ICON` 可用于更改父导航节点的名称和图标。
