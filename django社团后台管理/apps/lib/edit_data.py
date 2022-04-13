#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2019/3/3  16:00
# @Author: 余浪人
# @email: yulangren520@gmail.com
from flask import request, jsonify
from apps.lib.public import check_obj


def edit_data(model, db, Form, uid):
    obj = model.query.filter_by(id=uid, status=1).first()
    if not check_obj(obj):  # 验证数据
        form = Form(data=dict(obj))
        if request.method == 'POST' and uid and obj:
            form = Form(request.form)
            obj.set_attrs(form.data)
            db.session.commit()
            return 'ok'
        return form
    return jsonify({"status": 1})  # 验证不合格
