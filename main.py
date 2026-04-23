# -*- coding: utf-8 -*-
# @Time: 2026/4/6 11:36
# @Author: TomDing

"""
创建虚拟环境
    python -m venv .venv

激活虚拟环境
    source .venv/bin/activate

编辑配置文件
    edit pyproject.toml

同步配置
    pip install -e .
"""
from flask import flash
import requests
from lxml import etree
"""

用uv开始新的项目
uv init -p project_name
3.12为python版本，此文件夹需要符合python规范，不能有空格
uv init -p 3.12
也可以先建文件夹，同理，文件夹也需要符合python规范
uv init -p 3.12 --name my_project

查看可用的python版本
uv python list --only-downloads


安装新的模块
直接用uv add模块，就可以创建虚拟环境，也能添加uv.lock
uv add requests

查看安装的库
uv pip list

导出requirements配置
uv pip freeze > requirements.txt

安装配置
uv sync

添加远程仓库地址，命名为 origin
    git remote add origin git@github-personal:tomdingjf/uv_test.git
将本地仓库与 GitHub 上的 uv_test 仓库关联
    git branch -M main
将当前分支重命名为 main
    -M 表示强制重命名
将本地 main 分支推送到远程 origin 仓库
    git push -u origin main
    -u 参数会建立本地分支与远程分支的跟踪关系，以后只需 git push 即可


# 安装最新版本
uv python install

# 安装特定大版本
uv python install 3.12

# 安装精确版本
uv python install 3.12.3

# 同时安装多个版本
uv python install 3.10 3.11 3.12
"""

