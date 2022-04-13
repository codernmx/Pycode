#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2019/3/1  18:34
# @Author: 余浪人
# @email: yulangren520@gmail.com


from apps.models import db, BaseModel
from flask_login import UserMixin
from apps.models.massModel import MassModel
from apps.models.departemtModel import DepartmentModel


# 系统管理员
class SysMemberModel(BaseModel, UserMixin):
    username = db.Column(db.String(16),unique=True, comment='登录名')
    nikename = db.Column(db.String(32), comment='用户名')
    password = db.Column(db.String(128), comment='密码')
    limited = db.Column(db.Integer, default=1, comment='权限 超:0 普:1')

    def __repr__(self):
        return f'<当前用户:{self.username}>'

    def keys(self):
        return 'username', 'nikename', 'limited'


# 社团会员
class ClubsMemberModel(BaseModel):
    clubs = db.Column(db.Integer, db.ForeignKey(MassModel.id), comment='所属社团')
    department = db.Column(db.Integer, db.ForeignKey(DepartmentModel.id), comment='所属系别')
    student_num = db.Column(db.String(16),unique=True, comment='学号')
    name = db.Column(db.String(16), comment='名字')
    phone = db.Column(db.String(12), comment='电话')
    sex = db.Column(db.Integer, comment='性别')
    class_grade = db.Column(db.String(32), comment='班级')
    depart = db.relationship('DepartmentModel', backref='club')
    massModel = db.relationship('MassModel', backref='clubsmembermodel')

    def __repr__(self):
        return f'<当前社团会员: {self.name}>'

    def keys(self):
        return 'clubs', 'department', 'student_num', 'name', 'phone', 'sex', 'class_grade'
