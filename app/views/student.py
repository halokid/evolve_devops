#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Blueprint

user = Blueprint('student', __name__)


@user.route('/students')
def users():
  return 'students'


