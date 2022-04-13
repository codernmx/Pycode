#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2019/3/2  0:05
# @Author: 余浪人
# @email: yulangren520@gmail.com

from wtforms import Form, StringField, validators, DateField, TextAreaField, SelectField
from apps.models.massModel import MassModel


class MassForm(Form):
    massName = StringField(
        label='社团名称', validators=[validators.DataRequired('社团不可为空'), validators.Length(3, 32, '社团名称长度不合法')],
        render_kw={"class": "layui-input", "placeholder": "请输入社团名称", "lay-verify": "required"}
    )
    mass_principal_name = StringField(
        label='社团负责人', validators=[
            validators.DataRequired('负责人不可为空'), validators.Length(2, 10, '负责人名字长度不合法')],
        render_kw={"class": "layui-input", "placeholder": "请输入负责人", "lay-verify": "required"}
    )
    mass_introduce = TextAreaField(
        label='社团简介', validators=[validators.DataRequired('不可为空')],
        render_kw={"class": "layui-textarea", "placeholder": "请输入社团简介", "lay-verify": "required",
                   "style": "min-height: 200px;"}
    )

    def validate_massName(self, _):
        cou = MassModel.query.filter(MassModel.massName == self.massName.data).count()
        if cou:
            raise validators.ValidationError(f"{self.massName.data}_已存在!")



class EditMassForm(MassForm):
    create_time = StringField(
        label='成立时间', render_kw={"class": "layui-input", "style": "width: 150px", "disabled": "disabled"}
    )


class ActivityForm(Form):
    clubs_name = SelectField(label='所属社团', validators=[validators.DataRequired('不可为空')], coerce=int)
    activity_title = StringField(
        label='活动标题', validators=[validators.DataRequired('标题不可为空'), validators.Length(3, -1, '标题长度不合法')],
        render_kw={"class": "layui-input", "placeholder": "请输入活动名称", "lay-verify": "required"})
    activity_address = StringField(
        label='活动地点', validators=[validators.DataRequired('地点不可为空')],
        render_kw={"class": "layui-input", "style": "width: 50%", "placeholder": "请输入活动地点"}
    )
    activity_principal = StringField(
        label='活动负责人', validators=[validators.DataRequired('负责人不可为空')],
        render_kw={"class": "layui-input", "style": "width: 150px", "placeholder": "请输入负责人"}
    )

    activity_content = TextAreaField(
        label='活动内容', validators=[validators.DataRequired('内容不可为空')], render_kw={
            "class": "layui-textarea", "placeholder": "请输入活动内容", "style": "min-height: 200px;"})

    activity_date = DateField(
        label='活动时间', validators=[validators.DataRequired('日期不可空')],
        render_kw={"class": "layui-input", "style": "width: 150px", "placeholder": "请选择日期"}
    )

    def __init__(self, *args, **kwargs):
        super(ActivityForm, self).__init__(*args, **kwargs)
        self.clubs_name.choices = [(r.id, r.massName) for r in MassModel.query.all()]  # 初始化所属社团
