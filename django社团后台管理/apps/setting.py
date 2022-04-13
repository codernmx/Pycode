#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time: 2019/3/1  13:27
# @Author: 余浪人
# @email: yulangren520@gmail.com

import datetime


# ******* 配置项目路径 *******#
def get_database_uri():
    import os
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return 'sqlite:///{}/mass_system.db'.format(base_dir)


# ******* 配置Redis *******#
def get_redis():
    from redis import Redis
    r = Redis(host='127.0.0.1', port=6379, db=0, password=None, socket_connect_timeout=10)
    return r


class Config:
    # ******* 配置数据库 *******#
    # SQLALCHEMY_DATABASE_URI = "mysql+cymysql://root:248369@localhost:3306/mass_system"     # Mysql 数据库
    SQLALCHEMY_DATABASE_URI = get_database_uri()  # sqlite 数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # ******* 配置session *******#
    SESSION_TYPE = "redis"
    SESSION_REDIS = get_redis()
    SESSION_USE_SIGNER = True  # 发送到浏览器上session的cookie值进行加密
    SESSION_KEY_PREFIX = "elm"  # 保存到session中的值的前缀
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(seconds=1 * (60 * 60))  # 设置session过期时间


# 开发环境
class DevelopmentConfig(Config):
    DEBUG = True

# 生产环境
class ProductionConfig(Config):
    pass
