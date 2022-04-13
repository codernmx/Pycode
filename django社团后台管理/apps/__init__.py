#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2019/3/1  13:26
# @Author: 余浪人
# @email: yulangren520@gmail.com

from flask import Flask


# 注册蓝图
def register_bp(app: Flask):
    from apps.cms import cms_bp
    app.register_blueprint(cms_bp)


# 注册数据库
def register_db(app: Flask):
    from apps.models import db
    db.init_app(app)


# 注册login服务
def register_login(app: Flask):
    app.secret_key = 'hello_9527'
    from apps.lib.login_sys import login_manager
    login_manager.login_view = '/admin'
    login_manager.login_message = u"请登陆!"
    login_manager.session_protection = 'strong'
    login_manager.init_app(app)


# 注册应用
def create_app(config: str):
    app = Flask(__name__)
    app.config.from_object(config)
    register_bp(app=app)
    register_db(app=app)
    register_login(app=app)
    return app
