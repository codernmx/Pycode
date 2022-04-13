#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2019/3/3  15:39
# @Author: 余浪人
# @email: yulangren520@gmail.com
from flask import jsonify
from apps.lib.public import check_obj


# 删除一个
def delete(model, db, uid):
    obj = model.query.filter_by(id=uid, status=1).first()
    if not check_obj(obj) and uid:
        db.session.delete(obj)
        db.session.commit()
        return jsonify({"status": 0})
    return jsonify({"status": 1})


# 批量删除
def deletes(model, db, uid_s: list):
    try:
        for uid in uid_s:
            obj = model.query.filter_by(id=uid, status=1).first()
            if not check_obj(obj) and uid:
                db.session.delete(obj)
        db.session.commit()
        return jsonify({"status": 0})
    except:
        return jsonify({"status": 1})
