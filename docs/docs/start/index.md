---
title: 设置简介（Setup Introduction）
---

## 简介

一个功能完善的 InvenTree 服务器可以用最少的设置需求进行托管。 支持多种安装方法和数据库后端，从而可以在需要时提供灵活性。

!!! info "可用于生产环境"
	InvenTree 被设计为一个可用于生产环境的应用程序，并且可以在各种环境中部署。 以下说明旨在帮助你开始进行 *生产* 环境设置。 对于开发设置，请参考 [devcontainer 设置指南](../develop/devcontainer.md)。

## 安装方法

要快速跳转到特定的安装方式，请参考以下链接：

- [**Docker**](./docker.md)
- [**软件包安装程序**](./installer.md)
- [**裸机**](./install.md)

!!! success "推荐使用 Docker"
    推荐的 InvenTree 安装方法是按照我们的 [docker 设置指南](./docker.md)。 InvenTree 提供了对 docker 和 docker compose 的开箱即用支持，这为集成到你的生产环境提供了一个简单、可靠和可复用的管道。

!!! warning "重要安全注意事项"
    我们提供了关于 InvenTree 项目在软件设计中所假定的安全态势的文档。 评估这一点是设置过程中*至关重要*的一部分，并且在将 InvenTree 部署到生产环境之前应认真阅读。 你可以在 [此处](../concepts/threat_model.md) 阅读有关 [威胁建模输入] 的更多信息。

!!! info "延伸阅读"
    有关 InvenTree 技术堆栈的更多信息，请继续阅读以下内容！

### 配置选项

与首选安装方法无关，InvenTree 提供了许多 [配置选项](./config.md)，可用于自定义服务器环境。

## 系统组件

InvenTree 软件堆栈由多个组件组成，每个组件都是功能完善的服务器环境所必需的。 你可以在 [此处](./processes.md) 阅读有关 [InvenTree 进程] 的更多信息。

## 操作系统要求

InvenTree 文档 *假设* 操作系统是基于 debian 的 Linux 操作系统。 不同的系统，有些安装步骤可能会有所不同。

!!! warning "在 Windows 上安装"
    要在 Windows 系统上安装，你应该 [安装 WSL](https://docs.microsoft.com/en-us/windows/wsl/install-win10#manual-installation-steps)，然后按照 WSL 环境中的安装步骤进行操作。

!!! success "Docker"
    通过遵循 [docker 设置指南](./docker.md)，可以简化在任何操作系统上的安装。

## Python 要求

InvenTree 至少需要 Python 版本 {{ config.extra.min_python_version}}。 如果你的系统安装了旧版本的 Python，你将需要按照你的操作系统的更新说明进行操作。

### Invoke

InvenTree 使用 [invoke](https://www.pyinvoke.org/) python 工具包来执行各种管理操作。 你可以在 [此处](./invoke.md) 阅读 [有关我们对 invoke 工具的使用] 的更多信息

### 虚拟环境

在虚拟环境中安装所需的 Python 包允许进行独立于系统范围的 Python 安装的本地安装。 虽然不是绝对必要，但是 **强烈建议** 使用虚拟环境，因为它可以防止不同的 Python 安装之间发生冲突。

你可以在 [此处](https://docs.python.org/3/tutorial/venv.html) 阅读有关 Python 虚拟环境的更多信息。

!!! info "虚拟环境"
    安装说明 *假设* 已经配置了虚拟环境

`cd` 进入 InvenTree 目录，然后使用以下命令创建一个虚拟环境：

```
python3 -m venv env
```

### 激活虚拟环境

需要激活虚拟环境以确保使用正确的 python 二进制文件和库。 InvenTree 说明 *假设* 虚拟环境始终正确激活。

要在虚拟环境中配置 InvenTree，请 ``cd`` 进入 inventree 基础目录并运行以下命令：

```
source env/bin/activate
```

或者，如果这不起作用，请尝试：

```
. env/bin/activate
```

这会将当前 shell 会话放置在虚拟环境中 - 终端应显示 ``(env)`` 前缀。

### 在虚拟环境中调用

如果你正在使用虚拟环境（你应该这样做！），你需要确保已在虚拟环境中安装了 `invoke` 包！ 如果 invoke 命令是从虚拟环境外部运行的，它们可能无法正确运行 - 并且可能非常难以调试！

若要在虚拟环境内部安装 `invoke` 包，请运行以下命令（在激活虚拟环境后）：

```
pip install --upgrade --ignore-installed invoke
```

若要检查 `invoke` 包是否已正确安装，请运行以下命令：

```
which invoke
```

这将返回虚拟环境中 `invoke` 二进制文件的路径。 如果路径 *不在* 虚拟环境中，则未正确安装 `invoke` 包！

## InvenTree 源代码

InvenTree 源代码在 [GitHub](https://github.com/inventree/inventree/) 上分发，可以使用以下命令下载最新版本（使用 Git）：

```
git clone https://github.com/inventree/inventree/
```

或者，可以将源代码下载为一个 [.zip 存档](https://github.com/inventree/InvenTree/archive/master.zip)。

!!! info "通过 Git 更新"
    建议使用 Git 下载源代码，因为它允许在发布新版本的 InvenTree 时进行简单更新。

## 调试模式

默认情况下，生产 InvenTree 安装配置为在 *禁用* [DEBUG 模式]({% include "django.html" %}/ref/settings/#std:setting-DEBUG) 的情况下运行。

以调试模式运行会提供许多方便的开发功能，但是强烈建议 *NOT* 在生产环境中以调试模式运行。 提出此建议的原因是调试模式会泄漏大量关于你安装的信息，并且可能存在安全风险。

因此，对于生产设置，你应该在 [配置选项](./config.md) 中设置 `INVENTREE_DEBUG=false`。

### 关闭调试模式

在调试模式下运行时，InvenTree Web 服务器以本机方式管理 *静态* 和 *媒体* 文件，这意味着当 *禁用* 调试模式时，必须配置代理设置来处理此情况。

!!! info "阅读更多"
    有关更多详细信息，请参阅 [代理服务器文档](./processes.md#proxy-server)
