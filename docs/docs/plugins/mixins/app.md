---
title: App Mixin
---

## AppMixin

如果将此 mixin 添加到插件，则插件类定义的目录将被添加到 InvenTree 服务器配置中的 `INSTALLED_APPS` 列表中。

!!! warning "危险区域"
    只有在您了解 Django 的 [应用系统]({% include "django.html" %}/ref/applications) 的情况下才使用此 mixin。 具有此 mixin 的插件会深入集成到 InvenTree 中，并且可能导致难以重现或长时间运行的错误。 在发布之前，请使用 Django 的内置测试功能，以确保您的代码不会在 InvenTree 中导致不需要的行为。
