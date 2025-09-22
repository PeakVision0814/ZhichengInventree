---
标题：Devcontainer
---

## Devcontainer

[Devcontainers](https://code.visualstudio.com/docs/devcontainers/containers) 是进入 InvenTree 开发的最简单方式。你可以在 vscode 中在你的机器上运行它们，或者使用 github codespaces。

### 在 vscode 中设置

#### 前提条件

在继续之前，你需要确保已经安装了以下工具。

- 需要 [git](https://git-scm.com/downloads) 来克隆仓库
- 需要 [docker](https://www.docker.com/products/docker-desktop/) 来运行 devcontainer
- 需要 [vscode](https://code.visualstudio.com/Download) 来编辑和调试代码

#### Docker 容器

InvenTree devcontainer 设置会安装以下 docker 容器：

| 容器 | 描述 |
|---|---|
| inventree | InvenTree 主机服务器 |
| db | InvenTree 数据库 (postgresql) |
| redis | 用于缓存的 Redis 服务器 |

#### 设置/安装

1. 克隆仓库（如果你想提交更改，请 fork 它并在下一步中使用你的 fork 的 url）
   ```bash
   git clone https://github.com/inventree/InvenTree.git
   ```
2. 打开 vscode，导航到扩展侧边栏，搜索 `ms-vscode-remote.remote-containers`。点击安装。
3. 通过点击 `文件 > 打开文件夹` 打开从上面克隆的文件夹。
4. vscode 现在应该会问你是否想在 devcontainer 中重新打开这个文件夹。点击 `在容器中重新打开`。这可能需要几分钟时间，直到镜像被下载、构建并设置好所有依赖项。
5. 通过点击顶部菜单中的 `终端 > 新终端` 打开一个新的终端。
6. 现在，你终端中的最后一行应该在行首显示文本 `(venv)`
7. 完成！你现在应该有一个正常运行的 InvenTree 开发安装

### 在 Codespaces 中设置

使用你的浏览器打开 [inventree/InvenTree](https://github.com/inventree/InvenTree)，点击 `Code`，选择 `codespaces` 标签，然后点击在当前分支上创建 codespace。这可能需要几分钟时间，直到你的 inventree 开发环境设置完成。

!!! warning "关闭终端"
    出现的显示 `Welcome to codespaces` 的终端没有使用虚拟环境。关闭它并使用一个新的终端，该终端将自动连接到 venv 以使用命令。

### 运行任务

任务可以帮助你执行脚本。你可以通过打开命令面板（<kbd>CMD</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd>）并搜索 `运行任务` 来运行它们。然后选择所需的任务。

#### 设置演示数据集

如果你需要一些演示测试数据，请运行 `dev.setup-test` 任务。这将导入一个密码为 `inventree` 的 `admin` 用户。有关此数据集包含的更多信息，请参阅 [inventree/demo-dataset](../demo.md)。

#### 设置超级用户

如果你只需要一个超级用户，请运行 `superuser` 任务。它应该会提示你输入凭据。

#### 运行后台worker

如果你需要使用后台worker处理你的队列，请运行 `worker` 任务。这是一个前台任务，将在终端中执行。

### 运行 InvenTree

你可以只运行 InvenTree，也可以使用集成的调试器进行调试。转到 `运行和调试` 侧面板，确保已选择 `InvenTree Server`。点击左侧的播放按钮。

!!! tip "使用第三方调试"
    有时你还需要调试一些第三方软件包。只需选择 `InvenTree Server - 3rd party`

你现在可以设置断点，如果命中该点，vscode 将自动暂停执行。你可以看到该上下文中所有可用的变量，并使用底部的调试器控制台评估一些代码。使用播放或步进按钮继续执行。

!!! info "React 前端开发"

React 前端需要额外的步骤才能运行。请参阅 [Web UI / React](./react-frontend.md)

### 插件开发

插件开发最简单的方法是使用 InvenTree devcontainer。只需将你的插件仓库也挂载到 devcontainer 工作区中，并将其安装为 pip 可编辑包。

1. 要将你的插件 repo 挂载到工作区中，请将其添加到你的 `.devcontainer/devcontainer.json` 文件中。（确保你没有提交它）
   ```json
   "mounts": [
     "source=/path/to/your/local/inventree-plugin,target=/workspaces/inventree-plugin,type=bind,consistency=cached"
   ],
   ```
2. 通过点击 `文件 > 将文件夹添加到工作区…` 将 `/workspaces/inventree-plugin` 添加到你的 vscode 工作区文件夹。
3. 通过在 venv 中执行以下命令，将你的插件安装为 pip 可编辑安装。
   ```bash
   pip install -e /workspaces/inventree-plugin
   ```
4. 通过将以下文件添加到你的插件 repo `.vscode/settings.json`，将 InvenTree 核心代码添加到 Pylance IntelliSense 路径（你的路径可能因你的设置而异）：
   ```json
   {
     "python.analysis.extraPaths": ["/workspaces/InvenTree/InvenTree"]
   }
   ```

你的插件现在应该能够从 InvenTree 设置中激活。你还可以使用断点进行调试。

### 故障排除

#### 你的 ssh 密钥在 devcontainer 中不可用，但已加载到 macOS 上的活动 `ssh-agent`

确保你在 macOS 上为 vscode 启用了完全磁盘访问权限，否则你的 ssh 密钥在容器内不可用（参考：[自动将 SSH 密钥添加到 ssh-agent [评论]](https://github.com/microsoft/vscode-remote-release/issues/4024#issuecomment-831671081)）。

#### 你无法在 devcontainer 中使用你的 gpg 密钥来签署 macOS 上的提交

确保你已正确安装和设置 `gnupg` 和 `pinentry-mac`。阅读这篇 [medium 文章](https://medium.com/@jma/setup-gpg-for-git-on-macos-4ad69e8d3733) 以获取有关如何正确设置它的更多信息。

#### 数据库、媒体文件等存储在哪里？

备份、媒体/静态文件、venv、plugin.txt、secret_key.txt ... 存储在 `dev` 文件夹中。如果你想从一个干净的设置开始，你可以删除该文件夹，但请注意，这将删除你已经在 InvenTree 中设置的所有内容。

数据库数据存储在 `dev-db` 目录中。这由 `postgres` docker 容器管理。

### 性能改进

如果你在 Windows 中运行 devcontainer，你可能会遇到一些性能问题 - 尤其是在文件系统操作方面。

为了显著提高性能，应将源代码安装到 **WSL 2** 文件系统中（而不是在你的“Windows”文件系统中）。这将大大提高文件访问性能，并使 devcontainer 对文件系统更改的响应速度更快。

你还可以参考 [提高磁盘性能指南](https://code.visualstudio.com/remote/advancedcontainers/improve-performance) 以获取更多信息。

### Redis 缓存

devcontainer 设置提供了一个 [redis](https://redis.io/) 容器，可用于管理全局缓存。默认情况下，这是启用的，但可以通过调整 [docker compose 文件]({{ sourcefile('.devcontainer/docker-compose.yml') }}) 中的环境变量轻松禁用它。

### 前端测试

默认情况下，未安装运行前端测试（通过 playwright）所需的软件包。有关在 devcontainer 环境中安装这些软件包的说明，请参阅 [安装说明](./react-frontend.md#install-playwright)。
