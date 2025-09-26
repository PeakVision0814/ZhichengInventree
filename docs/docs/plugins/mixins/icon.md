---
title: 图标包 Mixin（Icon Pack Mixin）
---

## IconPackMixin

IconPackMixin 类提供了基本功能，允许插件公开自定义图标包，这些图标包可在 InvenTree UI 中使用。这对于提供自定义制作的图标包尤其有用，该图标包包含用于不同位置类型的图标，例如不同尺寸和样式的抽屉、包、ESD 袋等，这些图标在标准 tabler 图标库中不可用。

### 示例插件

以下示例演示了如何使用 `IconPackMixin` 类来添加自定义图标包：

::: plugin.samples.icons.icon_sample.SampleIconPlugin
    options:
        show_bases: False
        show_root_heading: False
        show_root_toc_entry: False
        show_source: True
        members: []
