#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2019/3/1  14:23
# @Author: 余浪人
# @email: yulangren520@gmail.com

from flask_sqlalchemy import SQLAlchemy
from apps.lib.pwd_verify import set_password
from apps.lib.public import get_uuid_16,get_date
db = SQLAlchemy()


# 基础数据模型
class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, comment='ID')
    uuid = db.Column(db.String(16), unique=True, default=get_uuid_16, comment='UUID')
    create_time = db.Column(db.Date, default=get_date(), comment='创建时间')
    update_time = db.Column(db.Date, default=get_date(), comment='更新时间')
    status = db.Column(db.Integer, default=1, comment='状态|-1:停用  0:删除  1:启用')

    def set_attrs(self, form_data):
        for k, v in form_data.items():
            if hasattr(self, k) and k != 'id':
                if v == '' or v == None:
                    pass
                elif k != 'password':
                    if k == 'username':
                        setattr(self, k, v.strip())
                    else:
                        setattr(self, k, v)
                else:  # 对密码进行加密
                    setattr(self, k, set_password(v.strip()))

    def __getitem__(self, item):
        if hasattr(self, item):
            return getattr(self, item)


from apps.models import member_model,massModel,departemtModel
