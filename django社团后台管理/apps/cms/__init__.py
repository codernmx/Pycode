#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2019/3/1  13:52
# @Author: 余浪人
# @email: yulangren520@gmail.com

from flask import Blueprint

cms_bp = Blueprint('cms_bp', __name__)

from apps.cms import system_index,clubs_view,clubs_member,system_member,department_view

