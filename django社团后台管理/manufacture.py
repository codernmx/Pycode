#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2019/3/5  18:59
# @Author: 余浪人
# @email: yulangren520@gmail.com


from apps import create_app
from apps.models import db

cms_app = create_app('apps.setting.ProductionConfig')

if __name__ == '__main__':
    with cms_app.app_context():
        db.create_all()
    cms_app.run(host="0.0.0.0", port=80)
