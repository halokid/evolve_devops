传统项目演进到devops的教学项目
====================================



•**项目介绍**

- 一个班级学生信息展示项目

- 包含了学生信息的增删改查等功能





•**技术栈**

- Python 3.6 开发， 主要用到Flask等模块，由python本身提供HTTP服务

- Mysql做数据库， 进行数据储存

- HTML + CSS 做前端页面， 作为静态页面由flask来引用

- 前端动态数据由python从mysql获取， 渲染到前端页面

- 前端做数据数据的动态更新交互，python做数据处理


•**项目运行**
```shell
cd evolve_devops
python main.py

# 访问 http://127.0.0.1:8080/
➜  evolve_devops git:(master) ✗  python main.py
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!

# app.run("0.0.0.0", 8080, debug=True)
# 当 debug=True 的时候，python代码的修改是立即生效的，不用重启项目
```

