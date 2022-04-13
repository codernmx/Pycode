#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2019/3/4  10:55
# @Author: 余浪人
# @email: yulangren520@gmail.com

from apps.models import db, BaseModel


class DepartmentModel(BaseModel):
    department = db.Column(db.String(64), unique=True, comment='系别')

    def __repr__(self):
        return f'当前系别: {self.department}'

    def keys(self):
        return 'department'
