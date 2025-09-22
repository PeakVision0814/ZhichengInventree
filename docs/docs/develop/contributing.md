---
标题：贡献指南（Contribution Guide）
---

在向 InvenTree 代码库提交你的第一个 pull request 之前，请阅读下面的贡献指南。

## 快速开始

以下命令将帮助你快速配置和运行一个开发服务器，并附带一个演示数据集供你使用：

### Devcontainer

使用我们的 [devcontainer](https://code.visualstudio.com/docs/devcontainers/containers) 在 [vscode](https://code.visualstudio.com/) 中进行设置和运行 InvenTree 开发环境是推荐的方法。

!!! success "Devcontainer 指南"
    请参考 [devcontainer 指南](./devcontainer.md) 获取更多信息！

### Docker

要使用 [docker](../start/docker.md) 设置开发环境，请运行以下指令：

```bash
git clone https://github.com/inventree/InvenTree.git && cd InvenTree
docker compose --project-directory . -f contrib/container/dev-docker-compose.yml run --rm inventree-dev-server invoke install
docker compose --project-directory . -f contrib/container/dev-docker-compose.yml run --rm inventree-dev-server invoke dev.setup-test --dev
docker compose --project-directory . -f contrib/container/dev-docker-compose.yml up -d
```

### 裸机

一个“裸机”开发环境可以按如下方式安装：

```bash
git clone https://github.com/inventree/InvenTree.git && cd InvenTree
python3 -m venv env && source env/bin/activate
pip install --upgrade --ignore-installed invoke
invoke install
invoke update
invoke dev.setup-dev --tests
```

请阅读 [InvenTree 设置文档](../start/index.md) 以获取完整的安装参考指南。

!!! note "所需软件包"
    根据你的系统，你可能需要安装其他所需的软件包。

### 设置 Devtools

运行以下命令来设置开发所需的工具。

```bash
invoke dev.setup-dev
```

*我们建议你在开始贡献之前运行此命令。 这将安装并设置 `pre-commit` 以在每次提交之前运行一些检查，并帮助减少错误。*

## 分支和版本控制

InvenTree 大致遵循 [GitLab flow](https://about.gitlab.com/topics/version-control/what-are-gitlab-flow-best-practices/) 分支风格，以允许简单管理多个标记的发布、短生命周期分支和在主干上进行开发。

名义上有 5 个活动分支：
- `master` - 主要的开发分支
- `stable` - 最新的 stable 发布
- `l10n` - 翻译分支：源到 Crowdin
- `l10_crowdin` - 翻译分支：源自 Crowdin
- `y.y.x` - 当前支持版本的发布分支 (例如 `0.5.x`)

所有其他分支都由维护者或核心团队成员定期删除。 这包括旧的发布分支。
不要将它们用作功能开发或 forks 的基础，因为没有重新调整基线的情况下，可能不会接受来自它们的补丁。

### 版本编号

InvenTree 版本编号遵循 [语义版本控制](https://semver.org/) 规范。

### 主要开发分支

InvenTree 的 "master" 分支的 HEAD 代表了当前代码开发的 "latest" 状态。

- 所有 feature 分支都合并到 master
- 所有 bug 修复都合并到 master

**禁止直接推送到 master:** 新特性必须从一个单独的分支（每个特性一个分支）作为一个 pull request 提交。

### Feature 分支

Feature 分支应该 *从* *master* 分支派生。

- 每个分支 / pull request 一个主要特性
- Feature pull request 合并回 *master* 分支。

### Stable 分支

"stable" 分支的 HEAD 代表了最新的 stable 发布代码。

- 版本化的发布合并到 "stable" 分支
- Bug 修复分支 *从* "stable" 分支创建

### Bugfix 分支

- 如果在 InvenTree 的标记发布版本中发现了一个 bug，那么应该 *从* 该标记发布创建一个 "bugfix" 或 "hotfix" 分支
- 当被批准时，该分支被合并回 *stable*，并增加一个 PATCH 号码 (例如. 0.4.1 -> 0.4.2)
- 该 bugfix *必须* 也要 cherry pick 到 *master* 分支.
- 如果使用 `backport` 标签标记，bugfix *可能* 也会从 *master* 自动向后移植到 *stable* 分支。

### 翻译分支

Crowdin 用于基于 Web 的翻译管理。 文件的处理是完全自动化的，`l10n` 和 `l10_crowdin` 分支用于管理翻译过程，不应由任何人手动触摸。

翻译过程如下：
1. 对 `master` 的提交通过 GitHub Actions 触发 CI
2. 翻译源文件被创建并自动推送到 `l10n` 分支 - 这是 Crowdin 的源分支
3. Crowdin 获取新的源文件并使它们可用于翻译
4. Crowdin 中进行的翻译在获得批准后，由 Crowdin 自动推送回 `l10_crowdin` 分支
5. `l10_crowdin` 分支由维护者定期合并回 `master`

## API 版本控制

每次 API 更改时都需要更新 [API 版本]({{ sourcefile("src/backend/InvenTree/InvenTree/api_version.py") }})。

## 环境

### 软件版本

核心软件模块的目标版本如下：

| 名称 | 最低版本 | 备注 |
|---|---|---|
| Python | {{ config.extra.min_python_version }} | 最低要求版本 |
| Invoke | {{ config.extra.min_invoke_version }} | 最低要求版本 |
| Django | {{ config.extra.django_version }} | 锁定的版本 |
| Node | 20 | 仅用于前端开发 |

任何其他软件依赖项都由项目包配置处理。

### 自动创建更新

以下工具可用于自动升级在新版本中已弃用的语法：
```bash
pip install pyupgrade
pip install django-upgrade
```

要更新代码库，请运行以下脚本。
```bash
pyupgrade `find . -name "*.py"`
django-upgrade --target-version {{ config.extra.django_version }} `find . -name "*.py"`
```

## 迁移文件

任何必需的迁移文件 **必须** 包含在提交中，否则 pull-request 将被拒绝。 如果你更改了底层数据库模式，请确保在提交 PR 之前运行 `invoke migrate` 并提交迁移文件。

*注意：一个 github action 会检查未暂存的迁移文件，如果找到任何未暂存的迁移文件，将会拒绝 PR！*

## 单元测试

任何新代码都应该被单元测试覆盖 - 如果任何新功能的代码覆盖率不足或总体代码覆盖率降低，提交的 PR 可能不会被接受。

InvenTree 代码库使用 [GitHub actions](https://github.com/features/actions) 在每次收到新的 pull request 时对代码库运行一套自动测试。 这些 actions 包括（但不限于）：

- 检查 Python 和 Javascript 代码是否符合标准样式指南
- 运行单元测试套件
- 自动构建和推送 docker 镜像
- 生成翻译文件

各种 github actions 可以在 `./github/workflows` 目录中找到

### 在本地运行测试

要在本地运行测试，请使用：

```
invoke dev.test
```

要仅运行部分测试，例如针对一个模块，请使用：
```
invoke dev.test --runtest order
```

要查看所有可用的选项：

```
invoke dev.test --help
```

#### 数据库权限问题

对于本地测试，django 会创建一个测试数据库并在测试后删除它。 如果在运行单元测试时遇到权限问题，请确保你的数据库用户具有创建新数据库的权限。

例如，在 PostgreSQL 中，运行：

```
alter user myuser createdb;
```

!!! info "Devcontainer"
    devcontainer 中提供的默认数据库容器已经设置了所需的权限

### 追踪覆盖到特定测试

有时，深入了解有多少测试覆盖特定语句以及哪些测试覆盖特定语句很有价值。coverage.py 将此信息称为上下文。 上下文由 invoke 任务测试自动捕获（启用覆盖的情况下），并且可以使用以下命令将其呈现为 HTML 报告。
```bash
coverage html -i
```

覆盖数据库也在 CI 管道中生成，并作为名为 `coverage` 的构件公开 14 天。

### 数据库查询分析

在开发过程中，分析后端代码的某些部分以查看执行了多少数据库查询可能很有用。 为此，可以使用 `count_queries` 上下文管理器来计算在特定代码块中执行的查询数。

```python
from InvenTree.helpers import count_queries

with count_queries("我的代码块"):
    # 要分析的代码块
    ...
```

开发人员可以使用它来分析特定的代码块，并且执行的查询数将打印到控制台。

## 代码风格

代码风格会在 GitHub 上作为项目 CI 管道的一部分自动检查。 这意味着任何不符合样式指南的 pull request 都会导致 CI 检查失败。

### 后端代码

后端代码 (Python) 根据 [PEP 样式指南](https://peps.python.org/pep-0008/) 进行检查。 请为每个函数和类编写文档字符串 - 我们遵循 python 的 [google doc-style](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)。

### 前端代码

前端代码 (Javascript) 使用 [eslint](https://eslint.org/) 进行检查。 虽然文档 String 对于前端代码不是强制的，但鼓励编写良好的代码文档！

### 在本地运行检查

如果你已按照设置 devtools 的步骤，则只需在将更改提交到代码时，代码风格检查就会自动执行。

### Django 模板

Django 模板通过 pre-commit 由 [djlint](https://github.com/Riverside-Healthcare/djlint) 检查。

以下规则从 [默认设置](https://djlint.com/docs/linter/) 中不适用：
```bash
D018: (Django) 内部链接应使用 { % url ... % } 模式
H006: Img 标签应具有 height 和 width 属性
H008: 属性应使用双引号引起来
H021: 应避免使用内联样式
H023: 不要使用实体引用
H025: 标签似乎是孤立的
H030: 考虑添加 meta description
H031: 考虑添加 meta keywords
T002: 应在标记中使用双引号
```

## 文档

新功能或现有功能的更新应附带用户文档。

### 稳定的链接引用

该文档框架支持添加重定向。 这用于为外部资源中的链接构建稳定的引用。

可以在 `docs/mkdocs.yml` 的 `redirect_maps` 部分中添加新的引用。 外部目标和文档页面都是可能的目标。 所有引用都在 docs CI 管道中进行 lint。

## 翻译

任何面向用户的字符串 *必须* 通过翻译引擎传递。

- InvenTree 代码是用英语编写的
- 用户可翻译的字符串以英语作为主要语言提供
- 二级语言翻译通过 [Crowdin](https://crowdin.com/project/inventree) 提供

*注意：翻译文件通过 GitHub actions 更新 - 你无需在提交 pull request 之前编译翻译文件！*

### Python 代码

对于通过 Python 代码公开的字符串，请使用以下格式：

```python
from django.utils.translation import gettext_lazy as _

user_facing_string = _('此字符串将公开给翻译引擎！')
```

### 模板字符串

HTML 和 javascript 文件通过 django 模板引擎传递。 可翻译的字符串实现如下：

```html
{ % load i18n % }

<span>{ % trans "此字符串将被翻译" % } - 此字符串不会！</span>
```

## Github 使用

### 标签

标签描述了多个区域中的问题和 PR：

| 区域 | 名称 | 描述 |
| --- | --- | --- |
| 分类标签 | | |
| | triage:not-checked | 该项目未经核心团队检查 |
| | triage:not-approved | 该项目未经维护者批准 |
| 类型标签 | | |
| | breaking | 指示破坏兼容性的重大更新或更改 |
| | bug | 标识需要解决的 bug |
| | dependency | 涉及项目依赖关系 |
| | duplicate | 另一个问题或 PR 的重复项 |
| | enhancement | 这是一个建议的增强功能，扩展了现有功能的功能 |
| | experimental | 这是一个新的 *实验性* 功能，需要手动启用 |
| | feature | 这是一个新功能，引入了新颖的功能 |
| | help wanted | 需要协助 |
| | invalid | 此问题或 PR 被认为是无效的 |
| | inactive | 表示缺乏活动 |
| | migration | 数据库迁移，需要特别注意 |
| | question | 这是一个问题 |
| | roadmap | 这是一个路线图功能，没有立即实施的计划 |
| | security | 涉及安全问题 |
| | starter | 非常适合该项目的新开发人员的问题 |
| | wontfix | 不会针对此问题或 PR 完成任何工作 |
| 功能标签 | | |
| | API | 与 API 相关 |
| | barcode | 条形码扫描和集成 |
| | build | 构建订单 |
| | importer | 数据导入和处理 |
| | order | 采购订单和销售订单 |
| | part | 零件 |
| | plugin | 插件生态系统 |
| | pricing | 定价功能 |
| | report | 报告生成 |
| | stock | 库存项目管理 |
| | user interface | 用户界面 |
| 生态系统标签 | | |
| | backport | 标记问题将被向后移植到 stable 分支作为 bug 修复 |
| | demo | 涉及 InvenTree 演示服务器或数据集 |
| | docker | Docker / docker-compose |
| | CI | CI / 单元测试生态系统 |
| | refactor | 重构现有代码 |
| | setup | 涉及 InvenTree 设置/安装过程 |
