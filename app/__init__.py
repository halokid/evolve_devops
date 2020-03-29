#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()#实例化SQLAlchemy


from .views.student import student

#创建app
def create_app():
  app = Flask(__name__)
  # 设置配置文件
  app.config.from_object('config')

  # 注册蓝图
  app.register_blueprint(student)

  # 2. 注册 Flask-SQLAlchemy
  # 这个对象在其他地方想要使用
  # SQLAlchemy(app)
  db.init_app(app)

  return app



