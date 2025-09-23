# 进入开发者容器
docker exec -it inventree_devcontainer-inventree-1 bash

# 进入目录
cd /home/inventree

# 进入环境
source /home/inventree/dev/venv/bin/activate

# invoke命令
## 导入演示数据并创建一个超级用户，用户名: admin，密码: inventree
invoke dev.setup-test --dev
### 创建超级管理员用户
invoke superuser
### 通过命令行重置密码
cd src/backend/InvenTree
python ./manage.py changepassword <username>

## 启动后端服务（Django）
invoke dev.server

## 启动前端服务（Vite/React）
invoke int.frontend-install # 仅需执行一次，安装前端依赖
invoke dev.frontend-server   # 启动前端开发服务器

## 迁移文件
invoke migrate
