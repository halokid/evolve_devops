#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pymysql

class Mysql(object):
  def __init__(self):
    self.config = {
      'host': "192.168.1.129",
      'port': 33061,
      'user': "root",
      'password': 'mysql-pw',
      'database': "evolve_devops",
      'charset': 'utf8',
      'cursorclass': pymysql.cursors.DictCursor,
      # 'cursorclass': pymysql.cursors.Cursor,
    }

  def getCursor(self):
    conn = pymysql.connect(**self.config)
    cursor = conn.cursor()
    return conn, cursor
