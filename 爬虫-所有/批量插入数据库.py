# -*- coding:utf-8 -*-
import time
from pymysql import *


# 计算插入数据需要的时间
def timer(func):
    def decor(*args):
        start_time = time.time()
        func(*args)
        end_time = time.time()
        print("耗时: ", end_time - start_time)
    return decor


@timer
def addData():
    allValues = []
    for num in range(1, 20000):
        allValues.append((num,num))  # 注意要用两个括号扩起来
    conn = connect(host='127.0.0.1', port=3306, user='root', password='root', database='test', charset='utf8')
    cs = conn.cursor()  # 获取光标

    # 关键点：executemany
    cs.executemany('insert into test (id,name) values(%s,%s)', allValues)
    conn.commit()

    print('插入数据完成----------------------->')

if __name__ == '__main__':
    addData()