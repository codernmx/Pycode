# -*- coding: utf-8 -*-
import requests
import random
import json
import os
import sys
from hashlib import md5
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
file_name = './img/4.jpg'
endpoint = 'http://api.fanyi.baidu.com'
path = '/api/trans/sdk/picture'
url = endpoint + path
from_lang = 'auto'
to_lang = 'zh'

# Set your own appid/appkey.
app_id = ''
app_key = ''
cuid = 'APICUID'
mac = 'mac'
# Generate salt and sign
def get_md5(string, encoding='utf-8'):
    return md5(string.encode(encoding)).hexdigest()
def get_file_md5(file_name):
    with open(file_name, 'rb') as f:
        data = f.read()
        return md5(data).hexdigest()
salt = random.randint(32768, 65536)
sign = get_md5(app_id + get_file_md5(file_name) +
               str(salt) + cuid + mac + app_key)
# Build request
payload = {'from': from_lang, 'to': to_lang, 'appid': app_id,
           'salt': salt, 'sign': sign, 'cuid': cuid, 'mac': mac}
image = {'image': (os.path.basename(file_name), open(
    file_name, 'rb'), "multipart/form-data")}
# Send request
response = requests.post(
    url, params=payload, files=image).content.decode('utf-8')
data = json.loads(response)['data']['content']
sumSrc = json.loads(response)['data']['sumSrc']
# print(sumSrc,'\n\n\n\n\n\n\n\n')
for i in data:
    if('发单号' in i['src']) or ('发貨单号' in i['src']):
        cutStr = i['src'].split('发貨单号') or i['src'].split('发单号')
        finalStr = cutStr[len(cutStr)-1].replace(':', '')
        finalStr = finalStr.replace('：', '')
        finalStr = finalStr.replace(' ', '')
        print(finalStr)