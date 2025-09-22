---
标题：账户管理（Account Management）
---

## 用户账户

默认情况下，InvenTree 不包含任何用户账户。配置用户账户是登录 InvenTree 服务器的第一步。

### 管理员账户

你可以配置 InvenTree 在首次运行时创建一个管理员账户。该账户将拥有对 InvenTree 服务器的完整 *超级用户* 访问权限。

此账户在你首次运行 InvenTree 服务器实例时创建。此账户的用户名/密码可以在配置文件或环境变量中进行配置。

!!! info "更多信息"
    有关配置管理员账户的更多信息，请参阅 [配置文档](./config.md#administrator-account)。

### 创建超级用户

创建管理员账户的另一种方法是使用 `superuser` 命令（通过 [invoke](./invoke.md)）。这将创建一个具有指定用户名和密码的新超级用户账户。

```bash
invoke superuser
```

或者，如果你在 Docker 容器中运行 InvenTree：

```bash
docker exec -rm -it inventree-server invoke superuser
```

### 用户管理

创建管理员账户后，你可以从 InvenTree Web 界面创建和管理其他用户账户。

## 密码管理

### 通过命令行重置密码

如果密码丢失，并且其他备份选项（如电子邮件恢复）不可用，系统管理员可以从命令行重置用户账户的密码。

登录到运行 InvenTree 服务器的机器，并运行以下命令（从顶级源代码目录）：

```bash
cd src/backend/InvenTree
python ./manage.py changepassword <username>
```

系统将提示你为指定的用户账户输入新密码。
