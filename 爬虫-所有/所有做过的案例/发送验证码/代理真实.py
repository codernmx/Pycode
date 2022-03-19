#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
import json
import random
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.30',
    "Accept-Encoding": "Gzip",
}


def createPhone():
    prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139",
               "147", "150", "151", "152", "153", "155", "156", "157", "158", "159",
               "186", "187", "188", "189", "172", "176", "185"]
    four = "".join(random.choice("0123456789") for i in range(4))
    phone = random.choice(prelist) + four + four
    return phone


# proxy_ip = requests.get(api_url).json()['data']['proxy_list']
# proxy_ip = [
#     'http://221.226.94.218:110/'
# ]
# https://www.kuaidaili.com/ops/
# 用户名密码认证(私密代理/独享代理)
username = "2507128400@qq.com"
password = "aa123456"

proxies = {
    # "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {'user': username, 'pwd': password,
    #                                                 'proxy': random.choice(proxy_ip)},
    # "https": "https://%(user)s:%(pwd)s@%(proxy)s/" % {'user': username, 'pwd': password,
    #                                                   'proxy': random.choice(proxy_ip)}

    'http': '221.226.94.218:110'
}


def sendCode(number):
    url = 'https://www.aliboxx.com/sunlight/client/anno/sendMobileVerifyCode'
    data = {"type": 0, "mobile": number, "GR": "86"}
    res = requests.post(url, json=data, proxies=proxies).content.decode('utf-8')
    data = json.loads(res)['body']['status']
    with io.open('记录.txt', 'a+', encoding='utf-8') as f:
        f.write(number + data + '\n')  # 添加‘\n’用于换行
        f.close()  # 关闭文件
    print(data)


if __name__ == '__main__':
    for i in range(0, 10):
        number = createPhone()
        sendCode(number)
