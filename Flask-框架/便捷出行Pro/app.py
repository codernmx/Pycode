import random

import pymysql, json, requests
from flask import Flask, request, jsonify
import hashlib
from hashlib import md5
from error import success, fail
from werkzeug.middleware.proxy_fix import ProxyFix  # nginx代理

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
config = {
    "appid": 'wx285a242d191f9226',  # 小程序appid
    "secret": '9a2df59bab8c6b744cf699749d5d6263',  # 小程序秘钥
    'appidFanyi': '20210824000926272',  # 百度翻译
    'appkey': 'PnMbaUZ5Y_yjxpQHMdVH',  # 百度翻译
    'ak': 'Z2mZbxYsOQllRq7MqFspSrYNqG9uPa20',  # 百度ip的key值

}


# 便捷出行

# sql = f"delete from info where id = '{id}'"  删除
# sql = f"select * from info where title like '%{title}%'"  搜索
# 连接数据库
def coon():
    db = pymysql.connect(host="localhost", user="root", password="137928", database="BJCX", port=3306)
    # db = pymysql.connect(host="49.232.153.152", user="BJCX", password="YpM8X7pF4wXCTZ7t", database="BJCX", port=3306)
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    return cursor


cursor = coon()


# 通知信息
def notice(nickName=None, thing=None):
    ip = request.remote_addr
    # 请求百度查ip地址
    ipUrl = 'https://api.map.baidu.com/location/ip?ak=%s&ip=%s&coor=bd09ll' % (config['ak'], ip)
    response = requests.get(ipUrl)
    data = json.loads(response.text)
    print(data)
    address = data['content']['address']

    # 添加到log表中
    sql = f"insert into LOG (IP,ADDRESS,ACTION) values ('{ip}','{address}','{thing}')"
    print(sql)
    try:
        cursor.execute(sql)
        cursor.connection.commit()  # 不提交加不进去
    except:
        cursor = coon()
        cursor.execute(sql)
        cursor.connection.commit()
    # 手机发送通知
    url = 'https://api.day.app/ETH6H7jpx6yLfwUKzMUqzV/便捷出行Pro/%s %s' % (nickName, thing)
    requests.get(url)


@app.route('/', methods=['POST', 'GET'])
def index():
    notice('', '访问主页')
    return success("便捷出行Pro", '请求成功')


# 用户登录
@app.route('/api/login', methods=['POST'])
def getUserInfo():
    code = request.get_json().get('code')

    avatarUrl = request.get_json().get('avatarUrl')
    nickName = request.get_json().get('nickName')

    url = 'https://api.weixin.qq.com/sns/jscode2session?appid={}&secret={}&js_code={}&grant_type=authorization_code'.format(
        config['appid'], config['secret'], code)
    response = requests.post(url).content.decode('utf-8')
    data = json.loads(response)
    print(data['openid'])
    openid = data['openid']

    sql = f"SELECT id,avatarUrl,nickName FROM USER WHERE openid = '{openid}'"
    try:
        cursor.execute(sql)
    except:
        cursor = coon()
        cursor.execute(sql)
    res = cursor.fetchall()
    if len(res) == 0:
        notice(nickName, '创建用户')
        sql = f"insert into USER (openid,avatarUrl,nickName) values ('{openid}','{avatarUrl}','{nickName}')"
        cursor.execute(sql)
        sql = f"SELECT id,avatarUrl,nickName FROM USER WHERE openid = '{openid}'"
        cursor.execute(sql)
        res = cursor.fetchall()
        return success(res, '请求成功')
    else:
        notice(nickName, '登录成功')
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
    notice('', '查询用户信息')

    sql = f"SELECT * FROM USER WHERE openid = '{openid}'"
    try:
        cursor.execute(sql)
    except:
        cursor = coon()
        cursor.execute(sql)
    res = cursor.fetchall()
    return success(res, '请求成功')


# 获取签到次数
@app.route('/api/get/sign/total', methods=['POST'])
def getSignTotal():
    userId = request.get_json().get('userId')
    # notice('', '查询用户信息')

    sql = f"SELECT * FROM SIGN_IN WHERE USER_ID = '{userId}'"
    try:
        cursor.execute(sql)
    except:
        cursor = coon()
        cursor.execute(sql)
    res = cursor.fetchall()
    if len(res) == 0:
        # 新增一个签到数据
        sql = f"insert into SIGN_IN (USER_ID) values ('{userId}')"
        cursor.execute(sql)
        cursor.connection.commit()
        res = cursor.fetchall()
        return success(res, '请求成功')
    else:
        return success(res, '请求成功')


# 签到板块
@app.route('/api/sign/in', methods=['POST'])
def signIn():
    notice('', '签到')
    userId = request.get_json().get('userId')

    # 修改签到天数
    sql = f"UPDATE SIGN_IN SET CONS_TOTAL = ( CASE WHEN TO_DAYS( NOW( ) ) - TO_DAYS( LAST_TIME) <= 1 THEN CONS_TOTAL + 1 WHEN TO_DAYS( NOW( ) ) - TO_DAYS( LAST_TIME) > 1 THEN 1 END) WHERE USER_ID = {userId}"
    try:
        cursor.execute(sql)
        cursor.connection.commit()
    except:
        cursor = coon()
        cursor.execute(sql)
        cursor.connection.commit()
    sql = f"SELECT * FROM SIGN_IN WHERE USER_ID = '{userId}'"
    cursor.execute(sql)
    res = cursor.fetchall()
    return success(res, '请求成功')


@app.route('/api/fanyi/baidu/translate/word', methods=['POST', 'GET'])
# 翻译接口
def translate():
    notice('', '识别文字')
    from_lang = request.get_json().get('from_lang')
    to_lang = request.get_json().get('to_lang')
    query = request.get_json().get('query')
    try:
        url = 'http://api.fanyi.baidu.com/api/trans/vip/translate'

        def make_md5(s, encoding='utf-8'):
            return md5(s.encode(encoding)).hexdigest()

        salt = random.randint(32768, 65536)
        sign = make_md5(config['appidFanyi'] + query + str(salt) + config['appkey'])
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        payload = {
            'appid': config['appidFanyi'],
            'q': query,
            'from': from_lang,
            'to': to_lang,
            'salt': salt,
            'sign': sign
        }
        r = requests.post(url, params=payload, headers=headers)
        result = r.json()
        return success({'data': result}, '请求成功')
    except BaseException as error:
        return fail("失败", '错误')


@app.route('/api/fanyi/baidu/translate/img', methods=['POST', 'GET'])
# 翻译图片
def translateFile():
    notice('', '识别图片')
    file = request.files.get('file')
    data = request.form.to_dict()  # 获取文件携带的参数
    from_lang = data['from_lang']
    to_lang = data['to_lang']
    fileData = file.read()
    url = 'http://api.fanyi.baidu.com/api/trans/sdk/picture'

    def get_md5(string, encoding='utf-8'):
        return md5(string.encode(encoding)).hexdigest()

    def get_file_md5(file_name):
        data = file_name
        return hashlib.md5(data).hexdigest()

    salt = random.randint(32768, 65536)
    sign = get_md5(config['appidFanyi'] + get_file_md5(fileData) + str(salt) + 'APICUID' + 'mac' +
                   config['appkey'])
    payload = {
        'from': from_lang,
        'to': to_lang,
        'appid': config['appidFanyi'],
        'salt': salt,
        'sign': sign,
        'cuid': 'APICUID',
        'mac': 'mac'
    }
    response = requests.post(url, params=payload, files={'image': fileData})
    result = response.json()
    return success(result, '请求成功')


if __name__ == '__main__':
    app.run(debug=True, port=5002)
