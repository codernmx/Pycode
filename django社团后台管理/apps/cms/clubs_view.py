#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2019/3/2  0:21
# @Author: 余浪人
# @email: yulangren520@gmail.com

from flask import render_template, request,jsonify
from flask_login import login_required
from apps.cms import cms_bp
from apps.forms.massForm import EditMassForm, MassForm, ActivityForm
from apps.models.massModel import MassModel, db, ActivityModel
from apps.lib.delete_data import delete, deletes
from apps.lib.edit_data import edit_data
from apps.lib.error import errors


# 添加社团
@cms_bp.route('/clubs_add', endpoint='clubs_add', methods=['GET', 'POST'])
@login_required
def clubs_add():
    form = MassForm(request.form)
    if request.method == 'POST':
        if form.validate():
            model = MassModel()
            model.set_attrs(form.data)
            db.session.add(model)
            db.session.commit()
            return jsonify({"status": 0})
        return jsonify({"status": 1, "message": errors(form)})
    return render_template('clubs.html', form=form, title='添加')


# 社团列表/删除列表
@cms_bp.route('/clubs_list', endpoint='clubs_list', methods=['GET', 'DELETE'])
@login_required
def clubs_list():
    if request.method == 'DELETE':
        uid_s = request.form.get('data_s')
        if uid_s:   # 批量删除
            return deletes(MassModel, db, list(uid_s.split(',')))
        uid = request.form.get('uid')
        return delete(MassModel, db, uid)
    data_list = MassModel.query.filter(MassModel.status == 1)
    return render_template('clubs_list.html', data_list=data_list)


# 编辑社团
@cms_bp.route('/clubs_edit', endpoint='clubs_edit', methods=['GET', "POST"])
@login_required
def clubs_edit():
    uid = request.args.get('uid')
    data = edit_data(MassModel, db, EditMassForm, uid)
    if data == 'ok':
        return jsonify({"status": 0})
    return render_template('clubs.html', form=data, title='更新')


# 社团活动添加
@cms_bp.route('/activity_add', endpoint='activity_add', methods=['GET', "POST"])
@login_required
def activity_add():
    form = ActivityForm(request.form)
    if request.method == 'POST':
        if form.validate():
            model = ActivityModel()
            model.set_attrs(form.data)
            db.session.add(model)
            db.session.commit()
            return jsonify({"status": 0})
        else:
            return jsonify({"status": 1, "message": errors(form)})
    return render_template('activity.html', form=form, title='添加')


# 社团活动列表
@cms_bp.route('/activity_list', endpoint='activity_list', methods=['GET', 'DELETE'])
@login_required
def activity_list():
    if request.method == 'DELETE':
        uid_s = request.form.get('data_s')
        if uid_s:
            return deletes(ActivityModel, db, list(uid_s.split(',')))
        uid = request.form.get('uid')
        return delete(ActivityModel, db, uid)
    data_list = ActivityModel.query.filter(ActivityModel.status == 1)
    return render_template('activity_list.html', data_list=data_list)


# 社团活动修改
@cms_bp.route('/activity_edit', endpoint='activity_edit', methods=['GET', 'POST'])
@login_required
def activity_edit():
    uid = request.args.get('uid')
    data = edit_data(ActivityModel, db, ActivityForm, uid)
    if data == 'ok':
        return jsonify({"status": 0})
    return render_template('activity.html', form=data, title='更新')
