#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import render_template
from app import create_app

app = create_app()
if __name__ == "__main__":
  app.run("0.0.0.0", 8080, debug=True)




