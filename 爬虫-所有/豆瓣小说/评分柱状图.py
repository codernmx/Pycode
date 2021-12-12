import pymysql.cursors
import numpy as np
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker


conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    passwd='137928',  # 数据库密码
    db='douban_novels',
    charset='utf8mb4'
)
cursor = conn.cursor()

sql_select = '''select * from douban_novels.novels'''
cursor.execute(sql_select)
title = []
author = []
rating = []
publisher = []
for book in cursor.fetchall():
    title.append(book[1])
    author.append(book[2])
    if book[3] == 0:
        rating.append(None)
    else:
        rating.append(float(book[3]))
    if book[4] == '未知':
        publisher.append(None)
    else:
        publisher.append(book[4])

dic = {'TITLE': title, 'AUTHOR': author, \
       'RATING': rating, 'PUBLISHER': publisher}
df = pd.DataFrame(dic)  # 生成datframe：

# 获取数据
df3 = df['RATING'].value_counts()[:8]
areaX = df['RATING'].value_counts().index.tolist()[:8]
areaY = []
for i in df3:
    areaY.append(i)
print(areaX)
print(areaY)


def drawLine():
    c = (
        Bar()
            .add_xaxis(areaX)
            .add_yaxis("次数", areaY)
            .set_global_opts(title_opts=opts.TitleOpts(title="评分次数柱状图"))
            .render("评分次数柱状图.html")
    )
    return c
drawLine()