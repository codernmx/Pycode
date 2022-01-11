import json
import math
import random
import time
import pandas as pd
import requests

name = '【罗翔】最高院对“百香果女孩”案调卷审查'
oid =968129114

ts = time.time()
ts = math.floor(ts * 1000)
allInfo = []
for page in range(0, 51):
    print('正在获取第{}页的数据'.format(page))
    params = {
        # "callback": 'jQuery172014789916927733615_' + str(ts),
        "jsonp": 'jsonp',
        "next": page,
        "type": 1,
        "oid": oid,
        "mode": 3,
        "plat": 1,
        "_": ts
    }
    url = 'https://api.bilibili.com/x/v2/reply/main'
    response = requests.get(url, params=params).content.decode('utf-8')
    # print(response)
    data = json.loads(response)['data']['replies']
    for i in data:
        # print(i['content']['message'], '---------------------->')
        # print(i['content'], '---------------------->uname')
        # print(i['content']['members'], '---------------------->sex')
        allInfo.append(i['content']['message'])
    # time.sleep(random.randint(1, 10))
df = pd.DataFrame(allInfo)
df.columns = ['评论']
df.to_csv(name + '.csv', encoding='utf_8_sig')
