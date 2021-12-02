import pymysql  # (需要改成ORACLE版本)
from flask import Flask, render_template, request, jsonify

from error import success, fail

app = Flask(__name__)

# 连接数据库
db = pymysql.connect(host="localhost", user="root", password="137928", database="db", port=3306)  # (需要改成ORACLE版本)
cursor = db.cursor(cursor=pymysql.cursors.DictCursor)  # 游标 # (需要改成ORACLE版本)

# 这里是为了避免数据库断开连接  超时自动断开  你看ORACLE 是否需要吧
while True:
    try:
        db.ping()  # (需要改成ORACLE版本 看情况)
        break
    except:
        db.ping(True)  # (需要改成ORACLE版本 看情况)


# 用户登录
@app.route('/api/login', methods=['POST'])
def login():
    user = request.get_json().get('user')
    password = request.get_json().get('password')

    sql = f"SELECT * FROM USER WHERE USER = '{user}' AND PASSWORD ='{password}' "
    cursor.execute(sql)
    res = cursor.fetchall()
    print(user, password)
    if isinstance(res, list):
        return ({
            'code': 200,
            'user': res[0]['user'],
            'id': res[0]['id'],
        })
    else:
        return ({
            'code': 201,
            'msg': "账号密码错误"
        })


# 用户注册
@app.route('/api/register', methods=['POST'])
def user_register():
    # 获参数
    user = request.get_json().get('user')
    password = request.get_json().get('password')
    print(user,password)
    sql = f"insert into user (user,password) values ('{user}', '{password}')"
    cursor.execute(sql)
    res = cursor.fetchall()
    return success(res, '请求成功')


@app.route('/api/getList', methods=['POST', 'GET'])
def getInfoList():
    # 拿到请求参数

    sql = "select * from info LIMIT 0,100"
    cursor.execute(sql)  # 执行SQL语句
    # # 获取所有记录列表
    res = cursor.fetchall()
    return success(res, '请求成功')


@app.route('/api/get/details', methods=['POST', 'GET'])
def getInfoDetails():
    # 拿到请求参数
    id = request.json.get('id')


    sql = f"select * from info where id = '{id}'"
    cursor.execute(sql)  # 执行SQL语句
    # # 获取所有记录列表
    res = cursor.fetchall()[0]
    return success(res, '请求成功')


@app.route('/api/goods/search', methods=['POST', 'GET'])
def getInfoSearch():
    # 拿到请求参数
    title = request.get_json()['search']

    sql = f"select * from info where title like '%{title}%'"
    print(sql)
    cursor.execute(sql)  # 执行SQL语句
    # # 获取所有记录列表
    res = cursor.fetchall()

    return success(res, '请求成功')
        # 添加商品


@app.route('/api/goods/insert', methods=['POST', 'GET'])
def getInfoInsert():
    # 拿到请求参数
    title = request.get_json().get('title')
    des = request.get_json().get('des')
    picture = request.get_json().get('picture')
    if not picture:
        # 给个默认图片
        picture = 'https://img.alicdn.com/bao/uploaded/TB1eTo5o1H2gK0jSZJnXXaT1FXa.png'
    price = request.get_json().get('price')



    sql = f"insert into info (title,des,picture,price) values ('{title}','{des}','{picture}','{price}')"
    print(sql)
    cursor.execute(sql)  # 执行SQL语句
    # # # 获取所有记录列表
    res = cursor.fetchall()
    return success(res, '请求成功')


# 删除商品
@app.route('/api/goods/del', methods=['POST', 'GET'])
def getInfoDel():
    # 拿到请求参数
    id = request.get_json().get('id')

    sql = f"delete from info where id = '{id}'"
    print(sql)
    cursor.execute(sql)  # 执行SQL语句
    # # # 获取所有记录列表
    res = cursor.fetchall()
    return success(res, '请求成功')


# 修改商品信息
@app.route('/api/goods/update', methods=['POST', 'GET'])
def getInfoUpdate():
    # 拿到请求参数
    title = request.get_json().get('title')
    des = request.get_json().get('des')
    picture = request.get_json().get('picture')
    price = request.get_json().get('price')
    id = request.get_json().get('id')

    sql = f"UPDATE info set title = '{title}', des = '{des}',picture='{picture}',price='{price}' where id = '{id}'"
    print(sql)
    cursor.execute(sql)  # 执行SQL语句
    # # # 获取所有记录列表
    res = cursor.fetchall()
    return success(res, '请求成功')


if __name__ == '__main__':
    app.run(debug=True)
