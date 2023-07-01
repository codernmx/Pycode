# _*_ coding: utf-8 _*_
import pymysql
import requests
from bs4 import BeautifulSoup

db = pymysql.connect(host="127.0.0.1", user="root", password="137928", database="bjcx", port=3306)
cursor = db.cursor(cursor=pymysql.cursors.DictCursor)

url = 'http://jiage.10260.com/guoneiyoujia.asp'
res = requests.get(url, headers={}).content.decode('GB2312')
soup = BeautifulSoup(res, "lxml")
allInfo = soup.select(".cpbaojia table tr")[1:32]
for i in allInfo:
    area = i.contents[1].string
    v92 = i.contents[3].string
    v95 = i.contents[5].string
    v98 = i.contents[7].string
    v0 = i.contents[9].string
    time = i.contents[11].string
    print(v92,v95,v98,v0,time)

    print(area, v92, v95, v98, v0, time, )
    # sql = f"INSERT INTO OIL (`AREA`, `V0`, `V89`, `V92`, `V95`, `V98`,`UPDATE_TIME`) VALUES ('{area}', '{v0}', '{v89}', '{v92}', '{v95}', '{v98}','{time}')" #第一次要使用插入语句，后边获取根据区域名称更新数据，名称固定的
    sql = f"UPDATE `oil` SET `v0` = '{v0}', `v92` = '{v92}', `v95` = '{v95}', `v98` = '{v98}',  `updateTime` = '{time}' WHERE `area` ='{area}'"
    # print(sql)
    try:
        cursor.execute(sql)
        print('更新数据成功--------------->', area, v92, v95, v98, v0, time)
    except:
        print('更新数据库失败！！请检查，可能网址接口更新')
