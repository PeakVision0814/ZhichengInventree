---
title: 操作插件（Action Plugins）
---

## ActionMixin

可以通过将数据 POST 到 `/api/action/` 端点来调用任意“操作”。POST 请求必须包含要执行的操作的名称，并且服务器必须加载匹配的 ActionPlugin 插件。也可以通过 POST 数据将任意数据提供给操作插件：

```
POST {
    action: "MyCustomAction",
    data: {
        foo: "bar",
    }
}
```

### 示例插件

`InvenTree` 源代码中提供了一个示例操作插件，可以用作创建自定义操作插件的模板：

::: plugin.samples.integration.simpleactionplugin.SimpleActionPlugin
    options:
        show_bases: False
        show_root_heading: False
        show_root_toc_entry: False
        show_source: True
        members: []
