<div align="center">
  <img src="assets/images/logo/inventree.png" alt="InvenTree logo" width="200" height="auto" />
  <h1>InvenTree</h1>
  <p>开源库存管理系统</p>

<!-- Badges -->
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/license/MIT)![GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/inventree/inventree)
![CI](https://github.com/inventree/inventree/actions/workflows/qc_checks.yaml/badge.svg)
[![Documentation Status](https://readthedocs.org/projects/inventree/badge/?version=latest)](https://inventree.readthedocs.io/en/latest/?badge=latest)
![Docker Build](https://github.com/inventree/inventree/actions/workflows/docker.yaml/badge.svg)
[![Netlify Status](https://api.netlify.com/api/v1/badges/9bbb2101-0a4d-41e7-ad56-b63fb6053094/deploy-status)](https://app.netlify.com/sites/inventree/deploys)
[![Performance Testing](https://dev.azure.com/InvenTree/InvenTree%20test%20statistics/_apis/build/status%2Fmatmair.InvenTree?branchName=testing)](https://dev.azure.com/InvenTree/InvenTree%20test%20statistics/_build/latest?definitionId=3&branchName=testing)

[![OpenSSF Best Practices](https://bestpractices.coreinfrastructure.org/projects/7179/badge)](https://bestpractices.coreinfrastructure.org/projects/7179)
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/inventree/InvenTree/badge)](https://securityscorecards.dev/viewer/?uri=github.com/inventree/InvenTree)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=inventree_InvenTree&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=inventree_InvenTree)

[![codecov](https://codecov.io/gh/inventree/InvenTree/graph/badge.svg?token=9DZRGUUV7B)](https://codecov.io/gh/inventree/InvenTree)
[![Crowdin](https://badges.crowdin.net/inventree/localized.svg)](https://crowdin.com/project/inventree)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/inventree/inventree)
[![Docker Pulls](https://img.shields.io/docker/pulls/inventree/inventree)](https://hub.docker.com/r/inventree/inventree)

[![GitHub Org's stars](https://img.shields.io/github/stars/inventree?style=social)](https://github.com/inventree/)
[![Twitter Follow](https://img.shields.io/twitter/follow/inventreedb?style=social)](https://twitter.com/inventreedb)
[![Subreddit subscribers](https://img.shields.io/reddit/subreddit-subscribers/inventree?style=social)](https://www.reddit.com/r/InvenTree/)
[![Mastdon](https://img.shields.io/badge/dynamic/json?label=Mastodon&query=followers_count&url=https%3A%2F%2Fchaos.social%2Fapi%2Fv1%2Faccounts%2Flookup%3Facct=InvenTree&logo=mastodon&style=social)](https://chaos.social/@InvenTree)

<h4>
    <a href="https://demo.inventree.org/">查看演示</a>
  <span> · </span>
    <a href="https://docs.inventree.org/en/latest/">文档</a>
  <span> · </span>
    <a href="https://github.com/inventree/InvenTree/issues/new?template=bug_report.md&title=[BUG]">报告Bug</a>
  <span> · </span>
    <a href="https://github.com/inventree/InvenTree/issues/new?template=feature_request.md&title=[FR]">请求功能</a>
  </h4>
</div>

<!-- About the Project -->
## :star2: 关于本项目

InvenTree 是一个开源库存管理系统，提供强大的底层库存控制和零件追踪功能。InvenTree 系统的核心是一个 Python/Django 数据库后端，它提供一个管理界面（基于 Web）和一个 REST API，用于与外部接口和应用程序交互。强大的插件系统为自定义应用程序和扩展提供支持。

查看[我们的网站](https://inventree.org)了解更多详情。

<!-- Roadmap -->
### :compass: 路线图

想看看我们正在做什么吗？查看[路线图标签](https://github.com/inventree/InvenTree/issues?q=is%3Aopen+is%3Aissue+label%3Aroadmap)和[horizon 里程碑](https://github.com/inventree/InvenTree/milestone/42)。

<!-- Integration -->
### :hammer_and_wrench: 集成

InvenTree 设计为**可扩展的**，并为与外部应用程序**集成**或添加自定义插件提供多种选项：

* [InvenTree API](https://docs.inventree.org/en/latest/api/)
* [Python 模块](https://docs.inventree.org/en/latest/api/python/)
* [插件接口](https://docs.inventree.org/en/latest/plugins/)
* [第三方工具](https://docs.inventree.org/en/latest/plugins/integrate/)

<!-- TechStack -->
### :space_invader: 技术栈

<details>
  <summary>服务器</summary>
  <ul>
    <li><a href="https://www.python.org/">Python</a></li>
    <li><a href="https://www.djangoproject.com/">Django</a></li>
    <li><a href="https://www.django-rest-framework.org/">DRF</a></li>
    <li><a href="https://django-q.readthedocs.io/">Django Q</a></li>
    <li><a href="https://docs.allauth.org/">Django-Allauth</a></li>
  </ul>
</details>

<details>
<summary>数据库</summary>
  <ul>
    <li><a href="https://www.postgresql.org/">PostgreSQL</a></li>
    <li><a href="https://www.mysql.com/">MySQL</a></li>
    <li><a href="https://www.sqlite.org/">SQLite</a></li>
    <li><a href="https://redis.io/">Redis</a></li>
  </ul>
</details>

<details>
  <summary>客户端</summary>
  <ul>
    <li><a href="https://react.dev/">React</a></li>
    <li><a href="https://lingui.dev/">Lingui</a></li>
    <li><a href="https://reactrouter.com/">React Router</a></li>
    <li><a href="https://tanstack.com/query/">TanStack Query</a></li>
    <li><a href="https://github.com/pmndrs/zustand">Zustand</a></li>
    <li><a href="https://mantine.dev/">Mantine</a></li>
    <li><a href="https://icflorescu.github.io/mantine-datatable/">Mantine Data Table</a></li>
    <li><a href="https://codemirror.net/">CodeMirror</a></li>
  </ul>
</details>

<details>
<summary>DevOps</summary>
  <ul>
    <li><a href="https://hub.docker.com/r/inventree/inventree">Docker</a></li>
    <li><a href="https://crowdin.com/project/inventree">Crowdin</a></li>
    <li><a href="https://app.codecov.io/gh/inventree/InvenTree">Codecov</a></li>
    <li><a href="https://sonarcloud.io/project/overview?id=inventree_InvenTree">SonarCloud</a></li>
    <li><a href="https://packager.io/gh/inventree/InvenTree">Packager.io</a></li>
  </ul>
</details>

<!-- Getting Started -->
## :toolbox: 部署 / 开始使用

有多种部署 InvenTree 的选项。

<div align="center"><h4>
    <a href="https://docs.inventree.org/en/latest/start/docker/">Docker</a>
    <span> · </span>
    <a href="https://inventree.org/digitalocean"><img src="https://www.deploytodo.com/do-btn-blue-ghost.svg" alt="Deploy to DO" width="auto" height="40" /></a>
    <span> · </span>
    <a href="https://docs.inventree.org/en/latest/start/install/">裸机</a>
</h4></div>

单行安装 - 阅读[文档](https://docs.inventree.org/en/latest/start/installer/)，了解支持的发行版以及有关该函数的详细信息：
```bash
wget -qO install.sh https://get.inventree.org && bash install.sh
```

参考[入门指南](https://docs.inventree.org/en/latest/start/install/)以获取完整的安装和设置说明。

<!-- Mobile App -->
## :iphone: 移动应用

InvenTree 由一个[配套移动应用](https://docs.inventree.org/app/)提供支持，该应用允许用户访问库存控制信息和功能。

<div align="center"><h4>
    <a href="https://play.google.com/store/apps/details?id=inventree.inventree_app">Android Play 商店</a>
     <span> · </span>
    <a href="https://apps.apple.com/au/app/inventree/id1581731101#?platform=iphone">Apple App Store</a>
</h4></div>

<!-- Security -->
## :lock: 行为准则 & 安全策略

InvenTree 项目团队致力于为所有用户提供安全和友好的环境。请阅读我们的 [行为准则](CODE_OF_CONDUCT.md) 了解更多信息。

InvenTree 遵循行业安全最佳实践。我们的安全策略包含[在此仓库中](SECURITY.md)。我们在[我们的文档站点](https://docs.inventree.org/en/latest/security/)上提供专门的安全页面。

<!-- Contributing -->
## :wave: 贡献

欢迎并鼓励贡献。请帮助使这个项目变得更好！参考[贡献页面](https://docs.inventree.org/en/latest/develop/contributing/)。

<!-- Translation -->
## :scroll: 翻译

InvenTree Web 应用程序的母语翻译是[通过 Crowdin 由社区贡献的](https://crowdin.com/project/inventree)。**欢迎并鼓励贡献**。

<!-- Sponsor -->
## :money_with_wings: 赞助

如果您使用 InvenTree 并发现它很有用，请考虑[赞助该项目](https://github.com/sponsors/inventree)。

<!-- Acknowledgments -->
## :gem: 致谢

我们要感谢 [PartKeepr](https://github.com/partkeepr/PartKeepr) 作为一个有价值的前身和灵感来源。
在您的实例的许可信息对话框中查找已使用的第三方库的完整列表。

## :heart: 支持

<p>本项目由以下赞助商支持：</p>

<p align="center">
<a href="https://github.com/MartinLoeper"><img src="https://github.com/MartinLoeper.png" width="60px" alt="Martin Löper" /></a>
<a href="https://github.com/lippoliv"><img src="https://github.com/lippoliv.png" width="60px" alt="Oliver Lippert" /></a>
<a href="https://github.com/lfg-seth"><img src="https://github.com/lfg-seth.png" width="60px" alt="Seth Smith" /></a>
<a href="https://github.com/snorkrat"><img src="https://github.com/snorkrat.png" width="60px" alt="" /></a>
<a href="https://github.com/spacequest-ltd"><img src="https://github.com/spacequest-ltd.png" width="60px" alt="SpaceQuest Ltd" /></a>
<a href="https://github.com/appwrite"><img src="https://github.com/appwrite.png" width="60px" alt="Appwrite" /></a>
<a href="https://github.com/PricelessToolkit"><img src="https://github.com/PricelessToolkit.png" width="60px" alt="" /></a>
<a href="https://github.com/cabottech"><img src="https://github.com/cabottech.png" width="60px" alt="Cabot Technologies" /></a>
<a href="https://github.com/markus-k"><img src="https://github.com/markus-k.png" width="60px" alt="Markus Kasten" /></a>
<a href="https://github.com/jefffhaynes"><img src="https://github.com/jefffhaynes.png" width="60px" alt="Jeff Haynes" /></a>
<a href="https://github.com/dnviti"><img src="https://github.com/dnviti.png" width="60px" alt="Daniele Viti" /></a>
<a href="https://github.com/Islendur"><img src="https://github.com/Islendur.png" width="60px" alt="Islendur" /></a>
<a href="https://github.com/Gibeon-NL"><img src="https://github.com/Gibeon-NL.png" width="60px" alt="Gibeon-NL" /></a>
<a href="https://github.com/Motrac-Research-Engineering"><img src="https://github.com/Motrac-Research-Engineering.png" width="60px" alt="Motrac Research" /></a>
<a href="https://github.com/trytuna"><img src="https://github.com/trytuna.png" width="60px" alt="Timo Scrappe" /></a>
<a href="https://github.com/ATLAS2246"><img src="https://github.com/ATLAS2246.png" width="60px" alt="ATLAS2246" /></a>
<a href="https://github.com/Kedarius"><img src="https://github.com/Kedarius.png" width="60px" alt="Radek Hladik" /></a>

</p>

<p>拥有的持续资源由以下提供：</p>

<p align="center">
  <a href="https://depot.dev?utm_source=inventree"><img src="https://depot.dev/badges/built-with-depot.svg" alt="Built with Depot" /></a>
  <a href="https://inventree.org/digitalocean">
    <img src="https://opensource.nyc3.cdn.digitaloceanspaces.com/attribution/assets/SVG/DO_Logo_horizontal_blue.svg" width="201px" alt="Servers by Digital Ocean">
  </a>
  <a href="https://www.netlify.com"> <img src="https://www.netlify.com/v3/img/components/netlify-color-bg.svg" alt="Deploys by Netlify" /> </a>
  <a href="https://crowdin.com"> <img src="https://crowdin.com/images/crowdin-logo.svg" alt="Translation by Crowdin" /> </a> <br>
</p>


<!-- License -->
## :warning: 许可证

在 [MIT](https://choosealicense.com/licenses/mit/) 许可证下分发。有关更多信息，请参见 [LICENSE.txt](https://github.com/inventree/InvenTree/blob/master/LICENSE)。
