#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2019/3/4  15:05
# @Author: 余浪人
# @email: yulangren520@gmail.com


from apps.cms import cms_bp
from flask import render_template, request, jsonify
from flask_login import login_required
from apps.forms.departmentForm import DepartmentForm
from apps.models.departemtModel import DepartmentModel,db
from apps.lib.delete_data import delete, deletes
from apps.lib.error import errors


# 添加系别
@cms_bp.route('/department_add', endpoint='department_add', methods=['GET', 'POST'])
@login_required
def department_add():
    form = DepartmentForm(request.form)
    if request.method == 'POST':
        if form.validate():
            dep = DepartmentModel()
            dep.set_attrs(form.data)
            db.session.add(dep)
            db.session.commit()
            return jsonify({"status":0})
        return jsonify({"status":1,"message":errors(form)})
    return render_template('system_member.html', form=form,title='添加')


# 系别列表/ 删除系别
@cms_bp.route('/department_list',endpoint='department_list',methods=["GET",'DELETE'])
@login_required
def department_list():
    if request.method=='DELETE':
        uid_s = request.form.get('data_s')
        if uid_s:  # 批量删除
            return deletes(DepartmentModel, db, list(uid_s.split(',')))
        return delete(DepartmentModel,db,request.form.get('uid'))   # 删除
    data_list = DepartmentModel.query.all()
    return render_template('department_list.html',data_list=data_list)
