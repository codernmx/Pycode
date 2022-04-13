from web import app
from flask import request
from python.model.Province import Province
from python.model.City import City
import pymysql
import json

def get_conn():
    conn = pymysql.connect(host="localhost",
                           user="root",
                           password="root",
                           database="stat",charset='utf8',)
    return conn

#查询所有省份
@app.route('/selectallProvince')
def selectallProvince():
    conn = get_conn()
    cursor = conn.cursor()
    sql = '''
    select DISTINCT c.province from confirmedstat c
    '''
    cursor.execute(sql)
    results = cursor.fetchall()
    province = []
    for result in results:
        p = Province(result[0])
        province.append(p.__dict__)
    print(json.dumps(province, ensure_ascii=False))
    return json.dumps(province, ensure_ascii=False)

#根据选择的省份，查询某个具体城市（省-市二级联动）
@app.route('/selectallCityByProvince',methods=['POST'])
def selectallCityByProvince():
    conn = get_conn()
    cursor = conn.cursor()
    sql = '''
    select DISTINCT c.city from confirmedstat c
    where c.province = %s and LEFT(c.city,2) <> left(c.province,2)
    '''
    province = request.form.get("province")
    print("province:"+province)
    cursor.execute(sql, (province))
    results = cursor.fetchall()
    city = []
    for result in results:
        c = City(result[0])
        city.append(c.__dict__)
    print(json.dumps(city, ensure_ascii=False))
    return json.dumps(city, ensure_ascii=False)