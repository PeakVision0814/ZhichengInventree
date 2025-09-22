---
标题：架构（Architecture）
---

## 典型部署

InvenTree 是一个经典的 Django 应用程序，支持 WSGI 接口标准。下图显示了 InvenTree 的典型和推荐部署架构。

``` mermaid
flowchart LR
    Request --- RP[1: 反向代理]
    RP --- Gunicorn[5: Gunicorn]
    subgraph image:inventree/inventree
    Gunicorn --- Django[6: Django 服务器进程]
    end
    Django --- Database@{ shape: cyl, label: "SQL 数据库" }
    Django --- Redis
    Worker[7: Q2 Worker] ---  Redis@{ shape: cyl, label: "9: Redis 缓存" }
      Database -- 8: 数据库保存任务 ---> Worker

    subgraph caddy
    RP --- file[2: 文件服务器]
end

    file --- s[3: 静态文件]
    file --- m[媒体文件]
    RP-. 4: API 认证请求 .-> Gunicorn
```

1. 反向代理（例如 Caddy、Nginx、Apache）接收请求。
2. 静态或媒体文件的请求可以直接由反向代理提供，也可以转发到专用文件服务器
3. 静态或媒体文件可以通过不同的文件服务器提供（例如，将静态文件放置在 CDN 中）
4. 媒体文件需要向 Django 服务器发出 API 身份验证请求，以确保用户有权访问该文件
5. API 或前端请求从反向代理转发到 Gunicorn，Gunicorn 是一个 WSGI 服务器，用于处理服务器 Django 进程。
6. Gunicorn 进程是 Django 应用程序的松散耦合实例——主要提供 REST API，因为前端只需要几个完整的 django 调用（参见下面的 [前端架构](#frontend-architecture)）。
7. 正确配置的 InvenTree 实例还将运行后台工作进程（Q2 Worker），负责处理长时间运行的任务，例如发送通知、生成报告或计算昂贵的更新。Q2 用作任务处理库，它运行多个松散耦合的工作进程。
8. 数据库保存任务并由工作进程查询。这实现了相对持久的任务处理，因为可以重启底层服务器，从而最大程度地减少任务丢失。
9. InvenTree 的各种组件可以受益于 Redis 或协议兼容的缓存，该缓存用于存储经常访问的数据，例如用户会话、API 令牌、全局或插件设置或其他瞬态数据。这有助于提高性能并减少数据库的负载。

## 代码架构

本节介绍 InvenTree 代码库的各种架构方面以及系统中的机制和生命周期。

使用 InvenTree 不需要了解这些方面，但对于想要为项目做出贡献或了解如何在系统中使用插件或通过修补自定义功能来扩展系统的开发人员来说，这很有帮助。

### 存储库布局和关注点分离

所有计划在服务器上执行的代码都位于 `src/` 目录中。 contrib 中的某些代码可能需要部署或维护实例。
一个例外是 `tasks.py` 文件，其中包含可以从命令行运行的各种维护任务的定义。此文件位于存储库的根目录中，以简化说明。

代码样式通常仅适用于 `src/` 目录中的代码。

### 后端架构

InvenTree 的后端是一个 Django 应用程序。它的结构通常遵循 Django 的约定，但也包括一些自定义和扩展，以支持 InvenTree 的特定需求。
与 Django 标准最显着的偏差是：
- 操作 django 应用程序机制以启用[插件系统](#plugin-system)
- 使用自定义角色映射系统使权限更易于访问

后端的目的是：
- API 优先，具有 RESTful API，该 API 由前端使用，也可以由其他应用程序使用。
- 模块化，不同组件和应用程序之间具有清晰的关注点分离。
- 通过透明的测试覆盖率进行合理的测试
- 遵循 Django 和普遍接受的安全约定

### 前端架构

InvenTree 的前端主要是一个单页应用程序 (SPA)，使用 React, mantine 和 yarn/vite 用于捆绑。

#### 提供前端
它是静态预构建的，并由 Django 应用程序作为静态文件捆绑包提供。无需 node 可执行文件或捆绑技术即可在生产环境中运行前端。但是，可以将前端的开发服务器与后端的开发或生产实例一起使用。

前端和后端不需要由同一服务器或在同一域上提供服务，只需要 API 版本匹配即可。

#### 耦合到后端

前端在应用程序的生命周期内不会耦合，但可以通过 `INVENTREE_SETTINGS` 全局变量（由 `spa_settings` 标记呈现）来启动。

这些设置可以配置基本 URL、可用后端、环境详细信息等。

为了方便起见，前端的 html 结构通过性能优化的模板运行。仅完成了非常有限的渲染量，以保持响应时间和安全线程的表面较低。
