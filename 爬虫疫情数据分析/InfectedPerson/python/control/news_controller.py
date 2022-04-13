from web import app
from flask import request
from python.model.News import News
import pymysql


def get_conn():
    conn = pymysql.connect(host="localhost",
                           user="root",
                           password="root",
                           database="stat",charset='utf8',)
    return conn

@app.route('/selectallNews',methods=['POST'])
def selectallNews():
    page = request.form.get("page")
    limit = request.form.get("limit")
    conn = get_conn()
    cursor = conn.cursor()
    sql1 = "select * from pushservice"
    cursor.execute(sql1)
    results = cursor.fetchall()
    print(len(results))

    sql2 = "select * from pushservice limit %s,%s "
    limit = int(limit)
    page = int(page)
    start = (page - 1) * limit

    cursor.execute(sql2, (start, limit))
    results2 = cursor.fetchall()
    print(len((results2)))

    resultList = []
    res = {}

    for result in results2:
        new = News(result[0],result[1],result[2],result[3],result[4],result[5])
        #jsonob = json.dumps(user,default=InfectedPerson.infp2dict,ensure_ascii=False)
        resultList.append(new.__dict__)
    print(resultList)
    res['data'] = resultList
    res['code'] = 0
    res['msg'] = ''
    res['count'] = len(results)
    print(res)
    print(len(results))
    return res