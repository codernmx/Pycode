import pymysql.cursors
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'SimHei'

plt.figure(dpi = 600)
#连接数据库
conn = pymysql.connect(
    host = '127.0.0.1',
    user = 'root',
    passwd = '137928', #数据库密码
    db = 'douban_novels',
    charset = 'utf8mb4'
    )
cursor = conn.cursor()


#生成dataframe：图书信息与高分图书信息
sql_select = 'select * from douban_novels.novels'
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

dic = {'TITLE' : title, 'AUTHOR' : author,\
       'RATING' : rating, 'PUBLISHER' : publisher}

d = pd.DataFrame(dic) #生成dataframe：图书信息
d_high_rating = d[d['RATING'] >= 8.5] #生成dataframe：高分图书信息

#得到图书各类信息的描绘信息
print('\n' + '1000本小说评分统计信息', end = '\n')
d_des = d.describe()
d_des.to_csv('1000本小说评分统计信息.csv')
print(d_des)

print('\n' + '1000本小说作者统计信息', end = '\n')
d_aut_des = d['AUTHOR'].describe()
d_aut_des.to_csv('1000本小说作者统计信息.csv')
print(d_aut_des)

print('\n' + '1000本小说出版社统计信息', end = '\n')
d_pls_des = d['PUBLISHER'].describe()
d_pls_des.to_csv('1000本小说出版社统计信息.csv')
print(d_pls_des)

#图书评分箱线图
rating_box = d.plot.box(title="1000本小说评分箱线图")
plt.grid(linestyle="--", alpha=0.3)
plt.savefig('1000本小说评分箱线图.png')
plt.show()

#将图书信息进行分类统计，统计1000本小说中出现最多的10个出版社的出现次数
pls_group = d_high_rating.groupby('PUBLISHER')
pls_group = pls_group.size().reset_index(name='counts')
pls_group = pls_group.set_index('PUBLISHER')
pls_group = pls_group.sort_values('counts', ascending = False)
pls_group = pls_group[0 : 10]
pls_bar = pls_group.plot.bar()
plt.title('1000本小说中出现最多的10个出版社的出现次数')
plt.xlabel('出现次数')
plt.ylabel('出版社')
pls_bar.legend_.remove()
plt.savefig('1000本小说中出现最多的10个出版社的出现次数.png', bbox_inches = 'tight')
plt.show()

#将高分图书信息进行分类统计，统计1000本小说中，8.5分以上的小说出现最多的10个出版社的出现次数
pls_group = d.groupby('PUBLISHER')
pls_group = pls_group.size().reset_index(name='counts')
pls_group = pls_group.set_index('PUBLISHER')
pls_group = pls_group.sort_values('counts', ascending = False)
pls_group = pls_group[0 : 10]
pls_bar = pls_group.plot.bar()
plt.title('1000本小说中，8.5分以上的小说出现最多的10个出版社的出现次数')
plt.xlabel('出现次数')
plt.ylabel('出版社')
pls_bar.legend_.remove()
plt.savefig('1000本小说中，8.5分以上的小说出现最多的10个出版社的出现次数.png', bbox_inches = 'tight')
plt.show()

#生成datframe：图书标签与高分图书标签
sql_select = '''select * from douban_novels.novels, douban_novels.novel_tags
                where douban_novels.novels.NO = douban_novels.novel_tags.BOOKNO;'''
cursor.execute(sql_select)
title = []
author = []
rating = []
publisher = []
tag = []
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
    tag.append(book[6])

dic = {'TITLE' : title, 'AUTHOR' : author,\
       'RATING' : rating, 'PUBLISHER' : publisher, 'TAG' : tag}
d = pd.DataFrame(dic) #生成datframe：图书标签
d_high_rating = d[d['RATING'] >= 8.5] #生成datframe：高分图书标签

#得到图书标签的描绘信息
print('\n' + '1000本小说标签统计信息', end = '\n')
d_tags_des = d['TAG'].describe()
d_tags_des.to_csv('1000本小说标签统计信息.csv')
print(d_tags_des)

#将图书标签进行分类统计，统计1000本小说中出现最多的10个标签的出现次数
tags_group = d.groupby('TAG')
tags_group = tags_group.size().reset_index(name='counts')
tags_group = tags_group.sort_values('counts', ascending = False)
tags_group = tags_group.set_index('TAG')
tags_top10 = tags_group[0 : 10]
tags_top10_bar = tags_top10.plot.bar()
plt.title('1000本小说中出现最多的10个标签的出现次数')
plt.xlabel('出现次数')
plt.ylabel('标签')
tags_top10_bar.legend_.remove()
plt.savefig('1000本小说中出现最多的10个标签的出现次数.png', bbox_inches = 'tight')
plt.show()

#将高分图书标签进行分类统计,统计1000本小说中，8.5分以上的小说出现最多的10个标签的出现次数
tags_group = d_high_rating.groupby('TAG')
tags_group = tags_group.size().reset_index(name='counts')
tags_group = tags_group.sort_values('counts', ascending = False)
tags_group = tags_group.set_index('TAG')
tags_top10 = tags_group[0 : 10]
tags_top10_bar = tags_top10.plot.bar()
plt.title('1000本小说中，8.5分以上的小说出现最多的10个标签的出现次数')
plt.xlabel('出现次数')
plt.ylabel('标签')
tags_top10_bar.legend_.remove()
plt.savefig('1000本小说中，8.5分以上的小说出现最多的10个标签的出现次数.png', bbox_inches = 'tight')
plt.show()

cursor.close()
conn.close()
