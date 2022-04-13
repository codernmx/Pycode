from web import app
from flask import request
from python.model.InfectedPerson import InfectedPerson
import pymysql


def get_conn():
    conn = pymysql.connect(host="localhost",
                           user="root",
                           password="root",
                           database="stat",charset='utf8',)
    return conn

@app.route('/selectallInfo',methods=['POST'])
def selectallInfo():
    page = request.form.get("page")
    limit = request.form.get("limit")
    conn = get_conn()
    cursor = conn.cursor()
    sql1 = "select * from confirmedstat"
    cursor.execute(sql1)
    results1 = cursor.fetchall()
    print(len(results1))

    sql2 = "select * from confirmedstat limit %s,%s "
    limit = int(limit)
    page = int(page)
    start = (page-1)*limit
    print(type(start))
    print(type(limit))

    cursor.execute(sql2,(start,limit))
    results2 = cursor.fetchall()
    print(len((results2)))

    resultList = []
    res = {}

    for result in results2:
        ifper = InfectedPerson(result[0],result[1],result[2],result[3],result[4],result[5],result[6])
        #jsonob = json.dumps(user,default=InfectedPerson.infp2dict,ensure_ascii=False)
        resultList.append(ifper.__dict__)
    print(resultList)
    res['data'] = resultList
    res['code'] = 0
    res['msg'] = ''
    res['count'] = len(results1)
    print(res)
    print(len(results2))
    return res

@app.route('/selectAreaByOption',methods=['POST'])
def selectAreaByOption():
    conn = get_conn()
    cursor = conn.cursor()
    province = request.form.get("key[province]")
    city = request.form.get("key[city]")
    sql = '''
    select * from confirmedstat
    where province = %s and city = %s
    '''
    cursor.execute(sql, (province, city))
    results = cursor.fetchall()
    resultList = []
    res = {}
    for result in results:
        user = InfectedPerson(result[0],result[1],result[2],result[3],result[4],result[5],result[6])
        #jsonob = json.dumps(user,default=InfectedPerson.infp2dict,ensure_ascii=False)
        resultList.append(user.__dict__)
    print(resultList)
    res['data'] = resultList
    res['code'] = 0
    res['msg'] = ''
    res['count'] = len(resultList)
    print(res)
    print(len(resultList))
    return res






