---
title: 定位混合类(Locate Mixin)
---

## 定位混合类

`LocateMixin` 类允许插件通过完全自定义的方法“定位”库存物品（或库存地点）。

例如，仓库可以这样布置：每个单独的“零件箱”都有一个视听指示器（例如，RGB LED 和蜂鸣器）。“定位”特定的库存物品会导致 LED 闪烁，蜂鸣器发出声音。

另一个例子可能是零件检索系统，其中“定位”库存物品会导致该库存物品通过传送带“交付”给用户。

可能性是无限的！

### Web 集成

{{ image("plugin/web_locate.png", "从 Web 界面定位库存物品", maxheight="400px") }}

### App 集成

如果安装并激活了定位插件，[InvenTree 移动应用程序](../../app/index.md) 会显示一个用于定位库存物品或库存位置的按钮（见下文）：

{{ image("plugin/app_locate.png", "从 App 定位库存物品", maxheight="400px") }}

### 实施

请参考 [InvenTree 源代码]({{ sourcefile("src/backend/InvenTree/plugin/samples/locate/locate_sample.py") }}) 获取一个简单的实现示例。

### 示例插件

InvenTree 代码库中提供了一个简单的例子：

::: plugin.samples.locate.locate_sample.SampleLocatePlugin
    options:
        show_bases: False
        show_root_heading: False
        show_root_toc_entry: False
        show_source: True
        members: []
