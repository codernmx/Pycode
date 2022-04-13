#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2019/3/1  14:34
# @Author: 余浪人
# @email: yulangren520@gmail.com

from werkzeug.security import generate_password_hash, check_password_hash


# 哈希加盐的密码方式
def set_password(password):
    return generate_password_hash(password=password, method='pbkdf2:sha256', salt_length=32)


# 哈希验证密码的方式
def check_password(set_password, password):
    return check_password_hash(pwhash=set_password, password=password)  # 验证成功返回True
