#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2019/3/1  13:26
# @Author: 余浪人
# @email: yulangren520@gmail.com

from flask_migrate import Migrate, MigrateCommand
from apps import create_app
from flask_script import Manager
from apps.models import db

cms_app = create_app('apps.setting.DevelopmentConfig')
manager = Manager(app=cms_app)
# 绑定数据迁移
migrate = Migrate(app=cms_app, db=db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
