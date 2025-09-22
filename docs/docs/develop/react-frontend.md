---
title: React 前端开发
---

## 设置

以下文档详细介绍了如何设置和运行 InvenTree 前端用户界面的开发安装。 假定您正在使用 [InvenTree devcontainer 设置](./devcontainer.md)。

!!! warning "本指南假定您已经有一个正在运行的 devcontainer"

!!! info "所有这些步骤都在 Visual Studio Code 中执行"

!!! note "Devcontainer"
    [devcontainer](./devcontainer.md) 设置已经包括所有必需的软件包，并准备好运行前端服务器。

### 安装软件包

首先，确保安装了所有必需的前端软件包：

```bash
invoke int.frontend-install
```

## 服务器进程

开发环境需要运行两个服务器进程 - 后端服务器和前端服务器。

### 后端服务器

在启动前端服务器之前，请确保后端服务器正在运行。 后端服务器负责提供前端将连接到的 API 端点。

```bash
invoke dev.server
```

这将在前台启动后端服务器，并占用运行它的终端窗口。

### 前端服务器

现在后端服务器正在运行，您可以启动前端服务器。 前端服务器负责提供基于 React 的用户界面，并为构建和测试前端代码提供开发环境。

在一个*单独的终端窗口*中，运行以下命令来启动前端服务器：

```bash
invoke dev.frontend-server
```

当前端服务器运行时，它将在 https://localhost:5173/ 上可用

## 实时重新加载

对前端代码所做的任何更改都会自动触发前端服务器的实时重新加载。 这意味着您可以更改代码，并在浏览器中立即看到结果，而无需手动刷新页面。

## 调试

您可以将 vscode 调试器附加到前端服务器以调试前端代码。 在前端服务器运行的情况下，打开 vscode 中的“运行和调试”视图，然后从下拉列表中选择“InvenTree Frontend - Vite”。 单击播放按钮开始调试。 这会将调试器附加到正在运行的 vite 服务器，并允许您在前端代码中放置断点。

!!! info "后端服务器"
    要调试前端代码，后端服务器必须正在运行（在单独的进程中）。 请注意，您不能在同一个 vscode 实例中调试后端服务器和前端服务器。

## 测试

前端代码库使用 [Playwright](https://playwright.dev/) 进行测试。 有大量涵盖前端代码库的测试，这些测试作为 CI 管道的一部分自动运行。

### 安装 Playwright

要安装运行测试所需的软件包，您可以使用以下命令：

```bash
cd src/frontend
sudo npx playwright install-deps
npx playwright install
```

### 运行测试

要在本地交互式编辑器中运行测试，您可以使用以下命令：

```bash
cd src/frontend
npx playwright test --ui
```

这将首先启动后端服务器（位于 http://localhost:8000），然后针对前端服务器（位于 http://localhost:5173）运行测试。 将打开一个交互式浏览器窗口，您可以单独或作为一组运行测试。

### 查看报告

playwright 测试作为项目 CI 管道的一部分自动运行，结果存储为可下载的报告。 报告文件可以使用 playwright “重播”，以查看测试运行的结果，并仔细检查任何失败的测试。

要查看报告，您可以在下载报告并从 zip 文件中解压缩后使用以下命令：

```bash
npx playwright show-report path/to/report
```

### 未找到测试

如果在测试启动序列中出现任何问题，playwright UI 将显示消息“未找到测试”。 在这种情况下，发生了一个错误，可能是启动了 InvenTree 服务器进程（该进程在后台运行）。

要调试这种情况并确定需要解决的错误，请运行以下命令：

```bash
npx playwright test --debug
```

这会将任何错误输出到控制台，使您能够在继续之前解决问题。 在所有可能性下，您的 InvenTree 安装需要更新，只需运行 `invoke update` 即可让您继续。

## 提示和技巧

### WSL

在 Windows 上，任何 Docker 交互都通过 WSL 运行。 自然地，所有容器和 devcontainer 都通过 WSL 运行。
前端服务器的默认配置设置文件轮询以启用热重载。
这本身就是一个巨大的性能损失。 如果您运行的是较旧的系统，它可能足以阻止任何东西在容器中运行。

如果您在运行前端服务器时遇到问题，请查看您的 Docker Desktop 应用程序。
如果您经常看到容器几乎使用了所有可用的 CPU 容量，则需要关闭文件轮询。

!!! warning "关闭文件轮询需要您在每次文件更改时重新启动前端服务器进程"

前往以下路径：`src/frontend/vite.config.ts` 并更改：

```const IS_IN_WSL = platform().includes('WSL') || release().includes('WSL');```

至

```const IS_IN_WSL = false;```

!!! tip "确保不要将此更改提交到 Git！"

!!! warning "此更改将要求您为在前端代码中所做的每次更改都重新启动前端服务器"

### 注意事项

运行前端开发服务器时，某些功能可能无法完全按预期工作！ 请花时间了解运行前端开发服务器时的数据流，以及它如何与后端服务器交互！

#### SSO 登录

通过 SSO 登录到前端开发服务器时，重定向 URL 可能无法正确重定向。
