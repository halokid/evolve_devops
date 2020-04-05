#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask

from .views.student import students

#创建app
def create_app():
  app = Flask(__name__)
  # 设置配置文件
  app.config.from_object('config')

  # 注册蓝图
  app.register_blueprint(students)

  return app



