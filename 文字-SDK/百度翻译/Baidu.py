# -*- coding: utf-8 -*-

# This code shows an example of ocr translation from Simplified-Chinese to English.
# This code runs on Python 2.7.x and Python 3.x.
# ```
#   python ocr_translate.py <image>
# ```
# You may install `requests` to run this code: pip install requests
# Please refer to `https://api.fanyi.baidu.com/doc/26` for complete api document

import requests
import random
import json
import os
import sys
from hashlib import md5

# if len(sys.argv) != 2:
#     print("usage: python {} <image>".format(sys.argv[0]))
#     exit(-1)
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# image = get_file_content('./img/tes.jpg')

# file_name = sys.argv[1]
file_name = './img/2.jpg'

endpoint = 'http://api.fanyi.baidu.com'
path = '/api/trans/sdk/picture'
url = endpoint + path

from_lang = 'auto'
to_lang = 'zh'

# Set your own appid/appkey.
app_id = '20210824000926272'
app_key = 'PnMbaUZ5Y_yjxpQHMdVH'

# cuid & mac
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
response = requests.post(url, params=payload, files=image).content.decode('utf-8')
data = json.loads(response)['data']['content']
# print(data)
for i in data:
    if('发单号' in i['src']):
        print(i['src'])

# Show response
# print(type (json.dumps(response))
