# _*_ coding: utf-8 _*_
# @Time : 2022/5/19 19:11
# @FileName : 公众号定时任务.py

# 连接数据库
import json
from datetime import datetime, timedelta
import pymysql
import requests

db = pymysql.connect(host="127.0.0.1", user="BJCX", password="YpM8X7pF4wXCTZ7t", database="BJCX", port=3306)
cursor = db.cursor(cursor=pymysql.cursors.DictCursor)

limitConfig = {
    1: ["1", "6"],
    2: ["2", "7"],
    3: ["3", "8"],
    4: ["4", "9"],
    5: ["5", "0"],
    6: ["不限行"],
    7: ["不限行"],
}


def isLimit(CAR_NUMBER, NOTICE_TIME):
    carLast = CAR_NUMBER[-1]
    isXian = carLast in limitConfig[xq + 1]
    return isXian and NOTICE_TIME == 1


def sendMsg(OPEN_ID, CAR_NUMBER, REASON):
    url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=' + access_token
    param = {
        "touser": OPEN_ID,
        "template_id": "QWcqPsYlMUwNpZUF3Ru1W1XkK0MHN_cWU6RhEemtVNM",
        "miniprogram": {
            "appid": "wx05f392bd9573cbf6",
            "pagepath": "/pages/index/index"
        },
        "data": {
            "first": {
                "value": '您的爱车【{}】明天在【成都】限行,请合理安排出行方式,避免罚款!'.format(CAR_NUMBER)
            },
            "keyword1": {
                "value": CAR_NUMBER,
                "color": "#FF0101"
            },
            "keyword2": {
                "value": REASON
            },
            "remark": {
                "value": "宝!每天快乐开车鸭~~~",
                "color": '#007BF9'
            }
        }
    }
    response = requests.post(url, json=param)
    result = json.loads(response.text)
    print('发送模板结果----------->>>>', result, '---------------------------------->>>>', OPEN_ID)


if __name__ == '__main__':
    getTokenUrl = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx6f877428ac5ee3f2&secret=5be7b51e5f4e96b6dcb7b8fcacb79ada'
    response = requests.get(getTokenUrl)
    access_token = json.loads(response.text)['access_token']
    print('获取token----------->', access_token)
    xq = datetime.today().isoweekday()  # 星期几
    sql = f"SELECT * FROM CAR WHERE DELETE_TIME IS NULL"
    cursor.execute(sql)
    res = cursor.fetchall()
    REASON = datetime.now().strftime('%Y-%m-%d') + '成都限行' + ",".join(limitConfig[xq + 1])  # 限行原因
    a = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    print(a)
    # for i in res:
    #     isSend = isLimit(i['CAR_NUMBER'], i['NOTICE_TIME'])
    #     if isSend:
    #         sendMsg(i['OPEN_ID'], i['CAR_NUMBER'], REASON)
