import json

import pymysql
import requests
from flask import Flask, request, jsonify
import hashlib

from error import success, fail

app = Flask(__name__)
config = {
    "appid": 'wxd9839f9c40077615',
    "secret": 'b4309c70ba68d54137bebeb408ccf5de',

}


# 连接数据库
def coon():
    db = pymysql.connect(host="localhost", user="root", password="137928", database="xcx_school", port=3306)
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    return cursor


cursor = coon()


@app.route('/', methods=['POST', 'GET'])
def index():
    return success("", '请求成功')
    # 1、 获取携带的 signature、timestamp、nonce、echostr
    # signature = request.args.get("signature", "")
    # timestamp = request.args.get("timestamp", "")
    # nonce = request.args.get("nonce", "")
    # echostr = request.args.get("echostr", "")
    # print(signature, timestamp, nonce, echostr)

    # token="codernmx"

    # # 2、 进行字典排序
    # data = [token, timestamp, nonce]
    # data.sort()

    # # 3、三个参数拼接成一个字符串并进行sha1加密
    # temp = ''.join(data)
    # sha1 = hashlib.sha1(temp.encode('utf-8'))
    # hashcode = sha1.hexdigest()
    # print(hashcode)

    # # 4、对比获取到的signature与根据上面token生成的hashcode，如果一致，则返回echostr，对接成功
    # if hashcode == signature:
    #     return echostr
    # else:
    #     return "error"


# 用户登录
@app.route('/api/login', methods=['POST'])
def login():
    code = request.get_json().get('code')

    avatarUrl = request.get_json().get('avatarUrl')
    nickName = request.get_json().get('nickName')
    url = 'https://api.weixin.qq.com/sns/jscode2session?appid={}&secret={}&js_code={}&grant_type=authorization_code'.format(
        config['appid'], config['secret'], code)
    response = requests.post(url).content.decode('utf-8')
    data = json.loads(response)
    print(data['openid'])
    openid = data['openid']

    sql = f"SELECT id,avatarUrl,nickName FROM m_user WHERE openid = '{openid}'"
    # sql = f"SELECT * FROM USER WHERE USER = '{user}' AND PASSWORD ='{password}' "
    try:
        cursor.execute(sql)
    except:
        cursor = coon()
        cursor.execute(sql)
    res = cursor.fetchall()
    if len(res) == 0:
        sql = f"insert into m_user (openid,avatarUrl,nickName) values ('{openid}','{avatarUrl}','{nickName}')"
        cursor.execute(sql)
        sql = f"SELECT id,avatarUrl,nickName FROM m_user WHERE openid = '{openid}'"
        cursor.execute(sql)
        res = cursor.fetchall()
        return success(res, '请求成功')
    else:
        return success(res, '请求成功')


@app.route('/api/getList', methods=['POST', 'GET'])
def getInfoList():
    # 拿到请求参数
    id = request.get_json().get('id')
    m_status = request.get_json().get('m_status')

    sql = f"select * from m_info where m_type = '{id}' and m_status = '{m_status}'"
    try:
        cursor.execute(sql)
    except:
        cursor = coon()
        cursor.execute(sql)
    # # 获取所有记录列表
    res = cursor.fetchall()
    return success(res, '请求成功')


# 获取自己发布的
@app.route('/api/getList/my', methods=['POST', 'GET'])
def getInfoListMy():
    # 拿到请求参数
    id = request.get_json().get('id')

    sql = f"select * from m_info where m_user = '{id}'"
    try:
        cursor.execute(sql)
    except:
        cursor = coon()
        cursor.execute(sql)
    # # 获取所有记录列表
    res = cursor.fetchall()
    return success(res, '请求成功')


# 修改自己发布的
@app.route('/api/info/update', methods=['POST', 'GET'])
def getInfoUpdate():
    # 拿到请求参数
    id = request.get_json().get('id')
    m_status = request.get_json().get('m_status')

    sql = f"UPDATE m_info set m_status = '{m_status}' where id = '{id}'"
    print(sql)
    try:
        cursor.execute(sql)
    except:
        cursor = coon()
        cursor.execute(sql)
    # # # 获取所有记录列表
    res = cursor.fetchall()
    return success(res, '请求成功')


# 获取列表和详细信息
@app.route('/api/get/message', methods=['POST', 'GET'])
def getInfoDetails():
    # 拿到请求参数
    id = request.json.get('id')
    sql = f"select * from m_message where infoId = '{id}'"
    try:
        cursor.execute(sql)
    except:
        cursor = coon()
        cursor.execute(sql)
    # # 获取所有记录列表
    res = cursor.fetchall()

    # 订单信息
    sql = f"select * from m_info where id = '{id}'"
    cursor.execute(sql)  # 执行SQL语句
    # # 获取所有记录列表
    info = cursor.fetchall()
    return success({
        "info": info,
        "list": res
    }, '请求成功')


# 发送信息
@app.route('/api/insert/message', methods=['POST', 'GET'])
def insertMessage():
    # 拿到请求参数
    userId = request.get_json().get('userId')
    infoId = request.get_json().get('infoId')
    content = request.get_json().get('content')
    avatarUrl = request.get_json().get('avatarUrl')

    sql = f"insert into m_message (userId,infoId,content,avatarUrl) values ('{userId}','{infoId}','{content}','{avatarUrl}')"
    print(sql)
    try:
        cursor.execute(sql)
    except:
        cursor = coon()
        cursor.execute(sql)
    # # # 获取所有记录列表
    res = cursor.fetchall()
    return success(res, '请求成功')


@app.route('/api/info/insert', methods=['POST', 'GET'])
def getInfoInsert():
    # 拿到请求参数
    content = request.get_json().get('content')
    price = request.get_json().get('price')
    qqNumber = request.get_json().get('qqNumber')
    m_user = request.get_json().get('id')
    type = request.get_json().get('type')

    sql = f"insert into m_info (m_title,m_price,m_type,m_qq,m_user) values ('{content}','{price}','{type}','{qqNumber}','{m_user}')"
    print(sql)
    try:
        cursor.execute(sql)
    except:
        cursor = coon()
        cursor.execute(sql)
    # # # 获取所有记录列表
    res = cursor.fetchall()
    return success(res, '请求成功')


# # 搜索
# @app.route('/api/goods/search', methods=['POST', 'GET'])
# def getInfoSearch():
#     # 拿到请求参数
#     title = request.get_json()['search']
#
#     sql = f"select * from info where title like '%{title}%'"
#     print(sql)
#     cursor.execute(sql)  # 执行SQL语句
#     # # 获取所有记录列表
#     res = cursor.fetchall()
#
#     return success(res, '请求成功')
#     # 添加商品
#
#
# # 删除商品
# @app.route('/api/goods/del', methods=['POST', 'GET'])
# def getInfoDel():
#     # 拿到请求参数
#     id = request.get_json().get('id')
#
#     sql = f"delete from info where id = '{id}'"
#     print(sql)
#     cursor.execute(sql)  # 执行SQL语句
#     # # # 获取所有记录列表
#     res = cursor.fetchall()
#     return success(res, '请求成功')


if __name__ == '__main__':
    app.run(debug=True)
