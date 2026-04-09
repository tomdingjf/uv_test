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
uv init -p 项目名称

安装新的模块
直接用uv add模块，就可以创建虚拟环境，也能添加uv.lock
uv add requests

查看安装的库
uv pip list

导出requirements配置
uv pip freeze > requirements.txt

安装配置
uv sync

"""

"""
添加远程仓库地址，命名为 origin
    git remote add origin git@github-personal:tomdingjf/uv_test.git
将本地仓库与 GitHub 上的 uv_test 仓库关联
    git branch -M main
将当前分支重命名为 main
    -M 表示强制重命名
将本地 main 分支推送到远程 origin 仓库
    git push -u origin main
    -u 参数会建立本地分支与远程分支的跟踪关系，以后只需 git push 即可

"""

