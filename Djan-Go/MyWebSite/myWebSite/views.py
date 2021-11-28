from django.http import HttpResponse, JsonResponse,HttpResponseBadRequest
from django.shortcuts import render


import pymysql
import json
import requests
import random
import hashlib
from hashlib import md5

config = {
    "appcode": '',
    'appid': '',
    'appkey': '',
    'ak': '',  # 百度ip的key值
}


# 给我的手机发送通知
def noticeLiu(request, apiName):
    # ip = request.META['REMOTE_ADDR']
    # ip = request.META['HTTP_X_FORWARDED_FOR']
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        ip = request.META.get("HTTP_X_FORWARDED_FOR")  # 经过nginx代理获取ip
    else:
        ip = request.META.get("REMOTE_ADDR")  # 没有通过代理获取ip
    try:
        # 请求百度查ip地址
        ipUrl = 'https://api.map.baidu.com/location/ip?ak=%s&ip=%s&coor=bd09ll' % (config['ak'], ip)
        response = requests.get(ipUrl)
        data = json.loads(response.text)
        address = data['content']['address']
        url = 'https://api.day.app/ETH6H7jpx6yLfwUKzMUqzV/有用户调用了 %s ip为 %s 地址 %s' % (apiName, ip, address)
        response = requests.get(url)
        return response
    except BaseException as error:
        return error


def index(request):
    noticeLiu(request, '访问主页')
    return render(request, '404.html')
    # 连接database
    # conn = pymysql.connect(host='127.0.0.1',
    #                        user='TEST',
    #                        password='5b48602315',
    #                        database='TEST',
    #                        charset='utf8')
    # # 得到一个可以执行SQL语句的光标对象
    # # cursor = conn.cursor()
    # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # # 定义要执行的SQL语句
    # sql = f'select * from test'
    # # 执行SQL语句
    # cursor.execute(sql)
    # data = cursor.fetchall()
    # # print(data)
    # # 关闭光标对象
    #
    # # 关闭数据库连接
    # # conn.close()
    # a = []
    # cursor.close()
    # return JsonResponse({
    #     "success": True,
    #     "code": 200,
    #     "data": data,
    #     'a': a
    # })
# 翻译接口
def translate(request):
    noticeLiu(request, '翻译文字')
    body = request.body.decode('utf-8')
    try:
        data = json.loads(body)
        from_lang = data['from_lang']
        to_lang = data['to_lang']
        query = data['query']
        # from_lang = request.POST.get('from_lang')
        # to_lang = request.POST.get('to_lang')
        # query = request.POST.get('query')

        appid = config['appid']
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
        return JsonResponse({'data': result})
    except BaseException as error:
        # return JsonResponse({'error': error,'msg':'请求参数错误','success':False})
        return HttpResponseBadRequest()



# 翻译图片
def translateFile(request):
    noticeLiu(request, '翻译图片')
    file = request.FILES.get('file')
    from_lang = request.POST.get('from_lang')
    to_lang = request.POST.get('to_lang')
    fileData = file.read()
    endpoint = 'http://api.fanyi.baidu.com'
    path = '/api/trans/sdk/picture'
    url = endpoint + path
    app_id = config['appid']
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
    return JsonResponse({'data': result})


# 文档转pdf换取token
def getChangePdfToken(request):
    noticeLiu(request, '文档转pdf换取token')
    file = request.FILES.get('file')
    type = request.POST.get('type')
    fileData = file.read()
    host = 'https://pdf2doc.ali.duhuitech.com'
    path = '/v1/convert'
    data = {
        'type': type
    }
    url = host + path
    headers = {
        'Authorization': 'APPCODE ' + config['appcode'],
    }
    files = {'file': fileData}
    response = requests.post(url, files=files, headers=headers, data=data)
    data = json.loads(response.text)
    return JsonResponse({'data': data, 'success': True, 'code': 200})


# token换取文件地址
def tokenGetFileUrl(request):
    noticeLiu(request, 'token换取文件地址')
    body = request.body.decode('utf-8')
    try:
        data = json.loads(body)
        token = data['token']
        baseUrl = 'https://apitx.duhuitech.com/q?token='
        url = baseUrl + token
        response = requests.get(url)
        data = json.loads(response.text)
        return JsonResponse({'data': data, 'success': True, 'code': 200})
    except BaseException as error:
        # return JsonResponse({'error': error,'msg':'请求参数错误','success':False})
        return HttpResponseBadRequest()


# Office文档/苹果iWorks/Sketch/多张图片/网页网址转换为PDF  换取token
def getPdfChangeToken(request):
    noticeLiu(request, '文件转pdf')
    file = request.FILES.get('file')
    fileName = file.name
    type = fileName.split('.', 1)[1]
    fileData = file.read()
    host = 'https://ali.duhuitech.com'
    path = '/v1/convert_post'
    data = {
        'type': type
    }
    url = host + path
    headers = {
        'Authorization': 'APPCODE ' + config['appcode'],
    }
    files = {'file': fileData}
    response = requests.post(url, files=files, headers=headers, data=data)
    data = json.loads(response.text)
    return JsonResponse({'data': data, 'success': True, 'code': 200})
