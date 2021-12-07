import datetime
import json

import pandas as pd
import requests
url = 'https://prod-chn-gcp-common-api.workjam.com/api/v4/companies/1549136564541/locations/1560474627780369/shifts/7180e703-5d85-40fa-91e3-b2c7db5e3c96'
headers = {
    "accept": 'application/json, text/plain, */*',
    "accept-encoding": 'gzip, deflate, br',
    "accept-language": 'en',
    "cache-control": 'no-cache',
    "origin": 'https://app.workjam.com',
    "pragma": 'no-cache',
    "referer": 'https://app.workjam.com/',
    # sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96",
    "sec-ch-ua-mobile": '?0',
    "sec-ch-ua-platform": "macOS",
    "sec-fetch-dest": 'empty',
    "sec-fetch-mode": 'cors',
    "sec-fetch-site": 'same-site',
    "user-agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36',
    "x-correlation-id": '6A6CB13F-D675-4817-92E4-5B2368B28E24',
    "x-token": 'eyJraWQiOiJXT1JLSkFNLUFQSS1HQVRFV0FZLUtFWS1JRCIsInR5cCI6IkpXVCIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiIxNjI5MzMxMzIzMTU5NTQ0IiwiZmlyc3ROYW1lIjoiQ3lhbiIsImxhc3ROYW1lIjoiV2FuZyIsImlzV0pBZG1pbiI6ZmFsc2UsImlzcyI6ImFwaS1jb3JlIiwiZGF0YWNlbnRlcklkIjoiZ2NwLXVzYS0yLWNvbW1vbiIsImV4cCI6MTY0Mzk1NzU0OCwiaWF0IjoxNjM4NzczNDg4LCJpc1hUb2tlbiI6dHJ1ZX0.qY3wXTzPekc0eBFGJ0EG4IPPx7OKqqCTlE7w6gPIFtzOsnjDV78T0oqlTxI68-nbQXAe6hQTzHhIEQZsiH-lbRcca68LyYhFN-daHRgzlstT4ChfEWkjSfNmnaGMF2ZoifBxyR1jKZZ8puSmC3K3XBcnXSnBrqjXtFYlVLfuNDwNgzWvgNxdgXj6ZDmqcQUbzlyQDzvPqjxTPsWUqc-JUNOpNGb-03rWTolhb5ienN1d7WiSr8r76wW_uPqnRKpBX64b1jZnujxaVL8Vf9e2ilGMzmJZSmhajH-J8vXmC-ciWj9eOZZxBb0G4FQ84pyQ8fK1tvu4R0lFvQfCrIO-qw',
}
res = requests.get(url, headers=headers).content.decode('utf-8')
data = json.loads(res)['segments']
allInfo = []
for i in data:
    startDateTime = i['startDateTime']
    #格式化一下时间
    #格式化一下时间
    #格式化一下时间
    #格式化一下时间
    endDateTime = i['endDateTime']
    position = i['position']
    allInfo.append([startDateTime,endDateTime,position])
    # print('position------------------->>>>>',i['position'])
print(data)

df = pd.DataFrame(allInfo)
df.columns = ['startDateTime', 'endDateTime', 'position']
df.to_csv('表格.csv', encoding='utf_8_sig')
