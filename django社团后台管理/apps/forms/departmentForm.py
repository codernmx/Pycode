#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2019/3/4  15:09
# @Author: 余浪人
# @email: yulangren520@gmail.com

from wtforms import Form,StringField,validators
from apps.models.departemtModel import DepartmentModel


class DepartmentForm(Form):
    department = StringField(label='系别',validators=[validators.Length(3,-1,'输入不合法')],render_kw={"class": "layui-input", "style": "width: 50%","placeholder":"请输入系别","lay-verify": "required"})

    def validate_department(self, _):
        cou = DepartmentModel.query.filter(DepartmentModel.department == self.department.data).count()
        if cou:
            raise validators.ValidationError(f"{self.department.data}_已存在!")
