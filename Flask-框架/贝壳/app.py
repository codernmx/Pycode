import pymysql  # (需要改成ORACLE版本)
from flask import Flask, render_template, request, jsonify

from error import success, fail

app = Flask(__name__)


# 连接数据库
def coon():
    db = pymysql.connect(host="localhost", user="root", password="137928", database="beike", port=3306)
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    return cursor


cursor = coon()


# 用户登录
@app.route('/api/list', methods=['POST', 'GET'])
def getList():
    sql = f"SELECT * FROM bj_info LIMIT 0,10"
    try:
        cursor.execute(sql)
    except:
        cursor = coon()
        cursor.execute(sql)
    res = cursor.fetchall()
    return success(res, '请求成功')


if __name__ == '__main__':
    app.run(debug=True)
