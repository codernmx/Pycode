# @Time : 2021/11/22 22:21
# @SoftWare : PyCharm
# -*- coding: utf-8 -*-
import requests
import random
import json
import os
import sys
from hashlib import md5
import pandas as pd

app_id = ''
app_key = ''
dir = "C:\\Users\\Myxk\\Desktop\\ApiPythonSDK\\img"  # 设置工作路径


# 新建列表，存放文件名（可以忽略，但是为了做的过程能心里有数，先放上）


def getAllFile():
    allPath = []
    for root, dirs, files in os.walk(dir):
        for file in files:
            singlePath = os.path.join(root, file)
            allPath.append(singlePath)
    # 打印文件名
    return allPath


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


def get_md5(string, encoding='utf-8'):
    return md5(string.encode(encoding)).hexdigest()


def get_file_md5(file_name):
    with open(file_name, 'rb') as f:
        data = f.read()
        return md5(data).hexdigest()


# file_name = './img/4.jpg'


def getNumber(file_name):
    url = 'http://api.fanyi.baidu.com/api/trans/sdk/picture'
    salt = random.randint(32768, 65536)
    sign = get_md5(app_id + get_file_md5(file_name) +
                   str(salt) + 'APICUID' + 'mac' + app_key)
    payload = {'from': 'auto', 'to': 'zh', 'appid': app_id,
               'salt': salt, 'sign': sign, 'cuid': 'APICUID', 'mac': 'mac'}
    image = {'image': (os.path.basename(file_name), open(
        file_name, 'rb'), "multipart/form-data")}
    response = requests.post(
        url, params=payload, files=image).content.decode('utf-8')
    try:
        data = json.loads(response)['data']['content']
        # sumSrc = json.loads(response)['data']['sumSrc']
    except:
        return response
    # sumSrc = json.loads(response)['data']['sumSrc']
    print(data)
    for i in data:
        if('发单号' in i['src']):
            cutStr = i['src'].split('发单号')
            finalStr = cutStr[len(cutStr)-1].replace(':', '')
            finalStr = finalStr.replace('：', '')
            finalStr = finalStr.replace(' ', '')
            finalStr = finalStr.replace('发单号', '')
            return finalStr
        elif('发貨单号' in i['src']):
            cutStr = i['src'].split('发貨单号')
            finalStr = cutStr[len(cutStr)-1].replace(':', '')
            finalStr = finalStr.replace('：', '')
            finalStr = finalStr.replace(' ', '')
            finalStr = finalStr.replace('发貨单号', '')
            return finalStr
        elif '发旋单号' in i['src'] :
            cutStr = i['src'].split(':')
            finalStr = cutStr[len(cutStr) - 1].replace(':', '')
            finalStr = finalStr.replace('：', '')
            finalStr = finalStr.replace(' ', '')
            finalStr = finalStr.replace('发旋单号', '')
            return finalStr


if __name__ == '__main__':
    # years = "2001"
    allPath = getAllFile()
    print(len(allPath), '总文件个数')
    allInfo = []
    for i in allPath:
        print(i)
        number = getNumber(i)
        allInfo.append([i, number])
        print('-------------------------------------------------->>>>>>>>', number)
    df = pd.DataFrame(allInfo)
    df.columns = ['图片名称', '单号']
    df.to_csv('data.csv', encoding='utf_8_sig')
