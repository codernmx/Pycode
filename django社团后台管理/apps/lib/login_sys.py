#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2019/3/1  19:26
# @Author: 余浪人
# @email: yulangren520@gmail.com

from flask_login import LoginManager
from apps.models.member_model import SysMemberModel

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return SysMemberModel.query.filter_by(id=int(user_id)).first()