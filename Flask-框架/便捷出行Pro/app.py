import random

import pymysql, json, requests
from flask import Flask, request, jsonify
import hashlib
from hashlib import md5
from error import success, fail

app = Flask(__name__)
config = {
    "appid": 'wx285a242d191f9226',
    "secret": '9a2df59bab8c6b744cf699749d5d6263',
    'appidFanyi': '20210824000926272',
    'appkey': 'PnMbaUZ5Y_yjxpQHMdVH',

}


# 便捷出行

# sql = f"delete from info where id = '{id}'"  删除
# sql = f"select * from info where title like '%{title}%'"  搜索
# 连接数据库
def coon():
    # db = pymysql.connect(host="localhost", user="root", password="137928", database="BJCX", port=3306)
    db = pymysql.connect(host="49.232.153.152", user="BJCX", password="YpM8X7pF4wXCTZ7t", database="BJCX", port=3306)
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    return cursor


cursor = coon()


@app.route('/', methods=['POST', 'GET'])
def index():
    return success("便捷出行Pro", '请求成功')


# 用户登录
@app.route('/api/login', methods=['POST'])
def getUserInfo():
    code = request.get_json().get('code')

    avatarUrl = request.get_json().get('avatarUrl')
    nickName = request.get_json().get('nickName')

    # 手机发送通知
    notUrl = 'https://api.day.app/ETH6H7jpx6yLfwUKzMUqzV/小小恋情/%s登录了小程序' % (nickName)
    r = requests.get(notUrl)

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
        return success(res[0], '请求成功')


# code查询用户信息
@app.route('/api/get/user/info', methods=['POST'])
def login():
    code = request.get_json().get('code')
    url = 'https://api.weixin.qq.com/sns/jscode2session?appid={}&secret={}&js_code={}&grant_type=authorization_code'.format(
        config['appid'], config['secret'], code)
    response = requests.post(url).content.decode('utf-8')
    data = json.loads(response)
    print(data['openid'])
    openid = data['openid']

    sql = f"SELECT * FROM m_user WHERE openid = '{openid}'"
    # sql = f"SELECT * FROM USER WHERE USER = '{user}' AND PASSWORD ='{password}' "
    try:
        cursor.execute(sql)
    except:
        cursor = coon()
        cursor.execute(sql)
    res = cursor.fetchall()
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


@app.route('/api/fanyi/baidu/translate/word', methods=['POST', 'GET'])
# 翻译接口
def translate():
    # request.get_data()
    from_lang = request.get_json().get('from_lang')
    to_lang = request.get_json().get('to_lang')
    query = request.get_json().get('query')
    try:
        appid = config['appidFanyi']
        appkey = config['appkey']
        endpoint = 'http://api.fanyi.baidu.com'
        path = '/api/trans/vip/translate'
        url = endpoint + path

        def make_md5(s, encoding='utf-8'):
            return md5(s.encode(encoding)).hexdigest()

        salt = random.randint(32768, 65536)
        sign = make_md5(appid + query + str(salt) + appkey)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        payload = {
            'appid': appid,
            'q': query,
            'from': from_lang,
            'to': to_lang,
            'salt': salt,
            'sign': sign
        }
        r = requests.post(url, params=payload, headers=headers)
        result = r.json()
        # return JsonResponse({'data': result})
        return success({'data': result}, '请求成功')
    except BaseException as error:
        # return JsonResponse({'error': error,'msg':'请求参数错误','success':False})
        # return HttpResponseBadRequest()
        return fail("失败", '错误')


@app.route('/api/fanyi/baidu/translate/img', methods=['POST', 'GET'])
# 翻译图片
def translateFile():
    # file = request.FILES.get('file')
    file = request.files.get('file')
    data = request.form.to_dict()   #获取文件携带的参数
    from_lang = data['from_lang']
    to_lang = data['to_lang']
    fileData = file.read()
    endpoint = 'http://api.fanyi.baidu.com'
    path = '/api/trans/sdk/picture'
    url = endpoint + path
    app_id = config['appidFanyi']
    app_key = config['appkey']
    cuid = 'APICUID'
    mac = 'mac'

    def get_md5(string, encoding='utf-8'):
        return md5(string.encode(encoding)).hexdigest()

    def get_file_md5(file_name):
        data = file_name
        return hashlib.md5(data).hexdigest()

    salt = random.randint(32768, 65536)
    sign = get_md5(app_id + get_file_md5(fileData) + str(salt) + cuid + mac +
                   app_key)
    payload = {
        'from': from_lang,
        'to': to_lang,
        'appid': app_id,
        'salt': salt,
        'sign': sign,
        'cuid': cuid,
        'mac': mac
    }
    response = requests.post(url, params=payload, files={'image': fileData})
    result = response.json()
    return success(result, '请求成功')


if __name__ == '__main__':
    app.run(debug=True, port=5002)
