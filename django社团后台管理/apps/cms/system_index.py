#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2019/3/1  13:59
# @Author: 余浪人
# @email: yulangren520@gmail.com
from flask_login import login_user, logout_user, login_required, current_user
from apps.cms import cms_bp
from flask import render_template, request, redirect, url_for
from apps.models.member_model import db, SysMemberModel
from apps.lib.pwd_verify import check_password_hash
from apps.forms.memberForm import SysMemberForm
from apps.models.massModel import MassModel,ActivityModel
from apps.models.member_model import ClubsMemberModel
from apps.models.departemtModel import DepartmentModel


# 系统首页
@cms_bp.route('/sys_index', endpoint='sys_index', methods=['GET'])
@login_required
def index():
    return render_template('index.html')


# 系统落地页
@cms_bp.route('/welcome', endpoint='welcome', methods=['GET'])
@login_required
def index():
    clubs_num = len(MassModel.query.all())
    member_num =len(SysMemberModel.query.all())
    activity_num = len(ActivityModel.query.all())
    clubsMember_num = len(ClubsMemberModel.query.all())
    department_num = len(DepartmentModel.query.all())
    return render_template('welcome.html',clubs=[clubs_num,member_num,activity_num,clubsMember_num,department_num])


# 用户登录
@cms_bp.route('/', methods=['GET', 'POST']) # 添加默认地址
@cms_bp.route('/admin', endpoint='login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username').strip()
        password = request.form.get('password')
        sm = SysMemberModel.query.filter_by(status=1, username=username).first()
        if sm.username == username and check_password_hash(sm.password, password):
            login_user(sm)  # 登录成功
            return redirect(url_for(endpoint='cms_bp.sys_index'))
        else:
            return render_template('login.html', error='账号或密码错误!', data=username)
    elif not SysMemberModel.query.filter_by(id=1).first():
        sm = SysMemberModel()  # 超级管理员初始化
        data = {"username": "admin", "password": "admin", "limited": 0, "nikename": "超级管理员"}
        sm.set_attrs(data)
        db.session.add(sm)
        db.session.commit()
    return render_template('login.html')


# 退出系统
@cms_bp.route('/logout', endpoint='logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for(endpoint='cms_bp.login'))


# 修改密码
@cms_bp.route('/edit_pwd', endpoint='edit_pwd',methods=['GET','POST'])
@login_required
def edit_password():
    form = SysMemberForm(request.form)
    user_id = current_user.id
    sysMember = SysMemberModel.query.filter_by(id=user_id).first()
    if request.method=='POST':
        if form.validate():
            sysMember.set_attrs(form.data)
            db.session.commit()
            return redirect(url_for(endpoint='cms_bp.logout'))
    else:
        form=SysMemberForm(data=dict(sysMember))
    return render_template('edit_password.html',form=form)

