from web import app
import pymysql
from flask import render_template
from python.model.ProvinceNum import ProvinceNum
from python.model.CityNum import CityNum

def get_conn():
    conn = pymysql.connect(host="localhost",
                           user="root",
                           password="root",
                           database="stat",charset='utf8',)
    return conn

@app.route('/distribute_area')
def distribute_area():
    conn = get_conn()
    cursor = conn.cursor()
    sql1 = '''
            select DISTINCT c1.city,c1.confirmedCount
            from confirmedstat c1
            inner join confirmedstat c2
            on LEFT(c1.city,2) = left(c2.province,2)
            where c1.city <> '河北区' and  c1.city <> '吉林市'
        '''
    print(sql1)
    cursor.execute(sql1)
    results1 = cursor.fetchall()
    
    sql2 = '''
    select DISTINCT CONCAT(c1.city,'市'),c1.confirmedCount
    from confirmedstat c1
    '''
    cursor.execute(sql2)
    results2 = cursor.fetchall()

    sql3 = '''
       select DISTINCT c1.city,c1.confirmedCount
       from confirmedstat c1
       '''
    cursor.execute(sql3)
    results3 = cursor.fetchall()

    china = []
    for result in results1:
        pn = ProvinceNum(result[0], result[1])
        #jsonob = json.dumps(pn, default=ProvinceNum.pn2dict, ensure_ascii=False)
        china.append(pn.__dict__)
    print(china)

    a = []
    for result in results2:
        cn = CityNum(result[0], result[1])
        #jsonob = json.dumps(cn, default=CityNum.cn2dict, ensure_ascii=False)
        a.append(cn.__dict__)
    for result in results3:
        cn = CityNum(result[0], result[1])
        #jsonob = json.dumps(cn, default=CityNum.cn2dict, ensure_ascii=False)
        a.append(cn.__dict__)
    print(a)

    #china = [{'area': '湖北省','China_confirm_sum':'122'},{'area': '安徽省','China_confirm_sum':'122'}] # fake user
    #a = [{'concat': '孝感市', 'confirm': '122'},{'concat': '黄冈市', 'confirm': '122'}]  # fake user
    return render_template("distribute_area.html",china=china,a=a)