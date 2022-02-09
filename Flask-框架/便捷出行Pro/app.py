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
    "appid": 'wx285a242d191f9226',
    "secret": '9a2df59bab8c6b744cf699749d5d6263',
    'appidFanyi': '20210824000926272',
    'appkey': 'PnMbaUZ5Y_yjxpQHMdVH',
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


def notice(nickName=None, thing=None):
    try:
        ip = request.remote_addr
        # 请求百度查ip地址
        ipUrl = 'https://api.map.baidu.com/location/ip?ak=%s&ip=%s&coor=bd09ll' % (config['ak'], ip)
        response = requests.get(ipUrl)
        data = json.loads(response.text)
        address = data['content']['address']
        #添加到log表中

        sql = f"insert into LOG (IP,ADDRESS) values ('{ip}','{address}')"
        try:
            cursor.execute(sql)
        except:
            cursor = coon()
            cursor.execute(sql)

        # 手机发送通知
        url = 'https://api.day.app/ETH6H7jpx6yLfwUKzMUqzV/便捷出行Pro/%s %s' % (nickName, thing)
        requests.get(url)
    except:
        # 手机发送通知
        url = 'https://api.day.app/ETH6H7jpx6yLfwUKzMUqzV/便捷出行Pro/%s' % ('报错了额~~')
        requests.get(url)


@app.route('/', methods=['POST', 'GET'])
def index():
    return success("便捷出行Pro", '请求成功')


# 用户登录
@app.route('/api/login', methods=['POST'])
def getUserInfo():
    code = request.get_json().get('code')

    avatarUrl = request.get_json().get('avatarUrl')
    nickName = request.get_json().get('nickName')
    notice(nickName, '首次登录')

    url = 'https://api.weixin.qq.com/sns/jscode2session?appid={}&secret={}&js_code={}&grant_type=authorization_code'.format(
        config['appid'], config['secret'], code)
    response = requests.post(url).content.decode('utf-8')
    data = json.loads(response)
    print(data['openid'])
    openid = data['openid']

    sql = f"SELECT id,avatarUrl,nickName FROM m_user WHERE openid = '{openid}'"
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
    notice(openid, '二次登录')

    sql = f"SELECT * FROM m_user WHERE openid = '{openid}'"
    try:
        cursor.execute(sql)
    except:
        cursor = coon()
        cursor.execute(sql)
    res = cursor.fetchall()
    return success(res, '请求成功')


@app.route('/api/fanyi/baidu/translate/word', methods=['POST', 'GET'])
# 翻译接口
def translate():
    notice('文字')
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
    notice('图片')
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
