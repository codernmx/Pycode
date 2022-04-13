#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2019/3/4  21:57
# @Author: 余浪人
# @email: yulangren520@gmail.com

import re

def errors(form):
    return re.findall("\['(.*?)'\]",str(form.errors))[0]