#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2019/3/2  20:37
# @Author: 余浪人
# @email: yulangren520@gmail.com

from apps.models import db, BaseModel


class MassModel(BaseModel):
    massName = db.Column(db.String(64),unique=True, comment='社团名称')
    mass_principal_name = db.Column(db.String(16), comment='负责人')
    mass_introduce = db.Column(db.String(2048))

    def __repr__(self):
        return f'<社团:{self.massName}>'

    def keys(self):
        return 'massName', 'mass_principal_name', 'mass_introduce', 'create_time'


class ActivityModel(BaseModel):
    clubs_name = db.Column(db.Integer, db.ForeignKey(MassModel.id), comment='所属社团')
    activity_title = db.Column(db.String(2048), comment='活动标题')
    activity_address = db.Column(db.String(2048), comment='活动地点')
    activity_principal = db.Column(db.String(64), comment='活动负责人')
    activity_content = db.Column(db.Text, comment='活动内容')
    activity_date = db.Column(db.Date, comment='活动时间')
    massModel = db.relationship('MassModel', backref='activity_model')

    def __repr__(self):
        return f'<活动标题:{self.clubs_name}>'

    def keys(self):
        return 'clubs_name', 'activity_title', 'activity_address', 'activity_principal', 'activity_content', 'activity_date'