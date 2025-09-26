---
title: 通知混合(Notification Mixin)
---

## 通知混合

`NotificationMixin` 类为插件提供了在系统中发生特定事件时向用户发送通知的能力。

任何由 InvenTree 核心系统生成的通知都可以通过实现此混合类的自定义插件发送给用户。

### 发送通知

`send_notification` 方法用于向用户发送通知：

::: plugin.base.integration.NotificationMixin.NotificationMixin.send_notification
    options:
      show_bases: False
      show_root_heading: False
      show_root_toc_entry: False
      summary: False
      members: []
      extra:
        show_sources: True

### 过滤目标

如果需要，插件可以实现 `filter_targets` 方法来过滤将接收通知的用户列表。这允许根据特定标准对通知哪些用户进行更精细的控制。

::: plugin.base.integration.NotificationMixin.NotificationMixin.filter_targets
    options:
      show_bases: False
      show_root_heading: False
      show_root_toc_entry: False
      summary: False
      members: []
      extra:
        show_sources: True

## 内置通知

以下内置通知插件可用：

- [UI 通知](../builtin/ui_notification.md)
- [电子邮件通知](../builtin/email_notification.md)
- [Slack 通知](../builtin/slack_notification.md)
v
