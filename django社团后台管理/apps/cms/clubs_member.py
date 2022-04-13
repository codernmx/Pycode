#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2019/3/4  10:16
# @Author: 余浪人
# @email: yulangren520@gmail.com

from apps.cms import cms_bp
from flask_login import login_required
from flask import request, render_template, jsonify
from apps.lib.delete_data import delete, deletes
from apps.models.member_model import db, ClubsMemberModel
from apps.forms.memberForm import ClubsMemberForm
from apps.lib.edit_data import edit_data
from apps.lib.error import errors


# 添加会员
@cms_bp.route('/clubs_member_add', endpoint='clubs_member_add', methods=['GET', 'POST'])
@login_required
def clubs_member_add():
    form = ClubsMemberForm(request.form)
    if request.method == 'POST':
        if form.validate():
            clubs_member = ClubsMemberModel()
            clubs_member.set_attrs(form.data)
            db.session.add(clubs_member)
            db.session.commit()
            return jsonify({"status": 0})
        return jsonify({"status": 1, "message": errors(form)})
    return render_template('clubs_member.html', form=form, title='添加')


# 会员列表
@cms_bp.route('/clubs_member_list', endpoint='clubs_member_list', methods=['GET', 'DELETE'])
@login_required
def clubs_member_list():
    if request.method == 'DELETE':
        uid_s = request.form.get('data_s')
        if uid_s:   # 批量删除
            return deletes(ClubsMemberModel, db, list(uid_s.split(',')))
        uid = request.form.get('uid')
        return delete(ClubsMemberModel, db, uid=uid)
    data_list = ClubsMemberModel.query.all()
    return render_template('clubs_member_list.html', data_list=data_list)


# 修改会员
@cms_bp.route('/clubs_member_edit', endpoint='clubs_member_edit', methods=['GET', 'POST'])
@login_required
def clubs_member_edit():
    uid = request.args.get('uid')
    data = edit_data(ClubsMemberModel, db, ClubsMemberForm, uid)
    if data == 'ok':
        return jsonify({"status": 0})
    return render_template('clubs_member.html', form=data, title='更新')
