#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2019/3/3  21:30
# @Author: 余浪人
# @email: yulangren520@gmail.com
import uuid
import random
from datetime import datetime

# UUID
def get_uuid_16():
    data = str(uuid.uuid4())
    return ''.join(data.split('-')[:3])

# 日期时间
def get_datetime():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S ')

# 日期
def get_date():
    return datetime.now()#.strftime('%Y-%m-%d')


def gen_rnd_filename():
    filename_prefix = datetime.now().strftime('%Y%m%d%H%M%S')
    return '%s%s' % (filename_prefix, str(random.randrange(1000, 10000)))

""" 验证修改传入参数是否合法 """
from flask import abort
def check_obj(obj):
    if obj is None:
        return abort(404)