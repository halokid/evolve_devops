#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Blueprint, render_template, request, redirect
from util import mysql
import time
students = Blueprint('student', __name__)

# mysql
mysqlObj = mysql.Mysql()

@students.route('/list')
def studentList():
  conn, cursor = mysqlObj.getCursor()
  sql = "select * from students"
  print(sql)
  cursor.execute(sql)
  rows = cursor.fetchall()
  print(rows)
  return render_template("index.html", rows=rows)


@students.route('/edit', methods=["GET"])
def studentEdit():
  idStr = request.args.get("id")
  conn, cursor = mysqlObj.getCursor()
  sql = "select * from students where id=" + str(idStr)
  cursor.execute(sql)
  row = cursor.fetchone()
  print(row)
  return render_template("edit.html", row=row)


@students.route('/edit-post', methods=["POST"])
def studentEditPost():
  name = request.form.get("name")
  classStr = request.form.get("class")
  age = request.form.get("age")
  idStr = request.form.get("id")
  conn, cursor = mysqlObj.getCursor()
  sql = "update students set name='" + name + "', class='" + classStr + "', age=" + str(age)\
        + " where id=" + idStr
  print(sql)
  cursor.execute(sql)
  conn.commit()
  print(conn.affected_rows())
  return redirect("/list")


@students.route('/delete')
def studentDel():
  idStr = request.args.get("id")
  sql = "delete from students where id=" + str(idStr)
  conn, cursor = mysqlObj.getCursor()
  cursor.execute(sql)
  conn.commit()
  print(conn.affected_rows())
  return render_template("del.html")










