#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2019/3/1  22:31
# @Author: 余浪人
# @email: yulangren520@gmail.com

from wtforms import Form, StringField, validators, PasswordField, SelectField, RadioField
from apps.models.massModel import MassModel
from apps.models.departemtModel import DepartmentModel
from apps.models.member_model import SysMemberModel, ClubsMemberModel


class SysMemberForm(Form):
    username = StringField(
        label=u'登录名', validators=[validators.DataRequired(message='登录名不可为空')],
        render_kw={"class": "layui-input", "placeholder": "请输入登录名", "lay-verify": "required|username"})
    nikename = StringField(label=u'用户名', validators=[
        validators.Length(
            min=2, message='名字长度不足'), validators.Length(max=16, message='名字过长')],
                           render_kw={"class": "layui-input", "placeholder": "请输入用户名名", "lay-verify": "nikename"})
    password = PasswordField(
        label=u'密码', validators=[validators.Length(min=6, message='密码至少6位')],
        render_kw={"class": "layui-input", "placeholder": "请输入密码", "lay-verify": "required|pass"})
    password2 = PasswordField(
        label=u'确认密码', validators=[validators.EqualTo('password', '两次密码不一致!')],
        render_kw={"class": "layui-input", "placeholder": "请重复密码", "lay-verify": "required|password2"})

    def validate_username(self, _):
        cou = SysMemberModel.query.filter(SysMemberModel.username == self.username.data).count()
        if cou:
            raise validators.ValidationError("登录名已存在!")


class ClubsMemberForm(Form):
    clubs = SelectField(
        label=u'所属社团', render_kw={"class": "layui-input", "lay-verify": "required"}, coerce=int)
    department = SelectField(
        label=u'所属系别', render_kw={"class": "layui-input", "lay-verify": "required"}, coerce=int)
    student_num = StringField(
        label=u'学号', validators=[validators.DataRequired('不可为空')],
        render_kw={"class": "layui-input", "style": "width: 50%", "placeholder": "请输入学号"})
    name = StringField(
        label=u'姓名', validators=[validators.DataRequired('不可为空'), validators.Length(2, 16, '长度不合法')],
        render_kw={"class": "layui-input", "style": "width: 50%", "placeholder": "请输入姓名"})
    phone = StringField(
        label=u'电话', validators=[
            validators.DataRequired('不可为空'),
            validators.Regexp(r'^((13[0-9])|(14[5,7])|(15[0-3,5-9])|(17[0,3,5-8])|(18['r'0-9])|166|198|199)\d{8}$',
                              message="请输入正确的电话号码")],
        render_kw={"class": "layui-input", "style": "width: 50%", "placeholder": "请输入电话"})
    sex = RadioField(label=u'性别', choices=[(0, "男"), (1, "女")], coerce=int)
    class_grade = StringField(
        label=u'班级', validators=[validators.DataRequired('不可为空'), validators.Length(3, 50, '班级不合法')],
        render_kw={"class": "layui-input", "style": "width: 50%", "placeholder": "请输入班级"})

    def __init__(self, *args, **kwargs):
        super(ClubsMemberForm, self).__init__(*args, **kwargs)
        self.clubs.choices = [(r.id, r.massName) for r in MassModel.query.all()]  # 初始化所属社团
        self.department.choices = [(r.id, r.department) for r in DepartmentModel.query.all()]  # 初始化所属系别

    def validate_student_num(self, _):
        cou = ClubsMemberModel.query.filter(ClubsMemberModel.student_num == self.student_num.data).count()
        if cou:
            raise validators.ValidationError(f"{self.student_num.data}_学号已存在!")

    def validate_phone(self, _):
        cou = ClubsMemberModel.query.filter(ClubsMemberModel.phone == self.phone.data).count()
        if cou:
            raise validators.ValidationError(f"{self.phone.data}_手机号已存在!")


class OrdinarySysMemberForm(SysMemberForm):
    limited = SelectField(label='权限', choices=[(1, '普通管理员'), (0, '超级管理员')],
        render_kw={"class": "layui-input", "lay-verify": "required"}, coerce=int)
