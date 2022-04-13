#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2019/3/4  14:02
# @Author: 余浪人
# @email: yulangren520@gmail.com

from apps.cms import cms_bp
from flask import request, render_template, jsonify
from flask_login import login_required
from apps.forms.memberForm import OrdinarySysMemberForm
from apps.models.member_model import SysMemberModel, db
from apps.lib.delete_data import delete, deletes
from apps.lib.error import errors
from apps.lib.edit_data import edit_data


# 添加普通管理
@cms_bp.route('/system_member', endpoint='system_member', methods=['GET', 'POST'])
@login_required
def system_member_add():
    form = OrdinarySysMemberForm(request.form)
    if request.method == 'POST':
        if form.validate():
            sys = SysMemberModel()
            sys.set_attrs(form.data)
            db.session.add(sys)
            db.session.commit()
            return jsonify({"status": 0})
        else:
            return jsonify({"status": 1, "message": errors(form)})
    return render_template('system_member.html', form=form,title='添加')


# 管理员列表
@cms_bp.route('/system_member_list', endpoint='system_member_list', methods=['GET', 'DELETE'])
@login_required
def system_member_list():
    if request.method == 'DELETE':
        uid_s = request.form.get('data_s')
        if uid_s:  # 批量删除
            return deletes(SysMemberModel, db, list(uid_s.split(',')))
        uid = request.form.get('uid')
        return delete(SysMemberModel, db, uid)
    data_list = SysMemberModel.query.filter(SysMemberModel.id != 1)
    return render_template('system_member_list.html', data_list=data_list)


# 修改会员
@cms_bp.route('/system_member_edit', endpoint='system_member_edit', methods=['GET', 'POST'])
@login_required
def system_member_edit():
    uid = request.args.get('uid')
    data = edit_data(SysMemberModel, db, OrdinarySysMemberForm, uid)
    if data == 'ok':
        return jsonify({"status": 0})
    return render_template('system_member.html', form=data, title='更新')
