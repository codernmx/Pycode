import json
import requests
import uuid
from pymysql import *

def myUuid():
    return str(uuid.uuid4()).replace('-', '')
info = []

key = 'xxxxxxxxxxxxxxx'

# 高德地图接口文档地址
# https://lbs.amap.com/api/webservice/guide/api/district

def getAll(data, par=None):
    for i in data:
        i['id'] = myUuid()
        if par:
            i['parent'] = par
        id = i['id']
        if len(i['citycode']) >0:
            i['citycode'] =i['citycode']
        else:
            i['citycode'] = None
        citycode = i['citycode']
        adcode = i['adcode']
        name = i['name']
        center = i['center']
        level = i['level']
        info.append((id, citycode, adcode, name, center, level,par))
        if len(i['districts']) > 0:
            getAll(i['districts'], i['adcode'])

def getInfo():
    url = 'https://restapi.amap.com/v3/config/district?subdistrict=3&key='.format(key)
    try:
        response = requests.get(url)
        data = json.loads(response.text)
        lev1 = data['districts'][0]['districts']
        getAll(lev1)
    except Exception as error:
        print(error, '取值报错~~，注意看key是否正确')


if __name__ == '__main__':
    getInfo()

    # 存储数据
    conn = connect(host='127.0.0.1', port=3306, user='root', password='root', database='bjcx', charset='utf8')
    cursor = conn.cursor()  # 获取光标
    cursor.executemany(
        '''insert into area_code (id,citycode,adcode,name,center,level,parent) values(%s,%s,%s,%s,%s,%s,%s)''', info)
    conn.commit()