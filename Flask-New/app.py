import pymysql
from flask import Flask, render_template, request, jsonify

from error import success,fail


app = Flask(__name__)

# 连接数据库
db = pymysql.connect(host="localhost", user="root", password="137928", database="db", port=3306)
cursor = db.cursor(cursor=pymysql.cursors.DictCursor)  # 游标


@app.route('/api/getList', methods=['POST', 'GET'])
def getInfoList():
    # 拿到请求参数

    sql = "select * from info LIMIT 0,100"
    cursor.execute(sql)  # 执行SQL语句
    # # 获取所有记录列表
    res = cursor.fetchall()
    return success(res,'请求成功')

@app.route('/api/get/details', methods=['POST', 'GET'])
def getInfoDetails():
    # 拿到请求参数
    id =request.json.get('id')
    sql = f"select * from info where id = '{id}'"
    cursor.execute(sql)  # 执行SQL语句
    # # 获取所有记录列表
    res = cursor.fetchall()[0]
    return success(res, '请求成功')


@app.route('/api/goods/search', methods=['POST', 'GET'])
def getInfoSearch():
    # 拿到请求参数
    title = request.get_json()['title']['title']
    # search =request.json.get('search')
    print(title)
    sql = f"select * from info where title like '%{title}%'"
    print(sql)
    cursor.execute(sql)  # 执行SQL语句
    # # 获取所有记录列表
    res = cursor.fetchall()

    return success(res,'请求成功')


if __name__ == '__main__':
    app.run(debug=True)
