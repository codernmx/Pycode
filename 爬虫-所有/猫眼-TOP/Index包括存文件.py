import time
import xlwt
import requests
from bs4 import BeautifulSoup
import random
import pandas as pd

headers = {
    "Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    "Accept-Encoding": 'gzip, deflate, br',
    "Accept-Language": 'zh-CN,zh;q=0.9',
    "Cache-Control": 'max-age=0',
    "Connection": 'keep-alive',
    "Cookie": '__mta=48482713.1635159163254.1635159163254.1635159163254.1; __mta=48482713.1635159163254.1635159163254.1636109843763.2; _lxsdk_cuid=17cb714c0e0c8-033e82611b0dc3-3a67410c-144000-17cb714c0e1c8; uuid_n_v=v1; uuid=9674BC503BCD11ECB4F8514365831FE83313CBD44FCA442B9EBF16166F870D9A; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk=9674BC503BCD11ECB4F8514365831FE83313CBD44FCA442B9EBF16166F870D9A; _csrf=c0897c2fe8b12a6664d889f6c2bb4883c27ead5915e9e87f1ccc14fa38c974ad; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1635159163,1635261061,1635851473,1636109833; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1636109844; _lxsdk_s=17cefbed57e-1bc-1b3-505%7C%7C4',
    "Host": 'www.maoyan.com',
    # sec-ch-ua: "Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92",
    "sec-ch-ua-mobile": '?0',
    "Sec-Fetch-Dest": 'document',
    "Sec-Fetch-Mode": 'navigate',
    "Sec-Fetch-Site": 'none',
    "Sec-Fetch-User": '?1',
    "Upgrade-Insecure-Requests": '1',
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
}

url_list = []  # 所有单个url
for iii in range(0, 1):
    url = 'https://maoyan.com/board/4?offset=' + str(iii) + '0'
    response = requests.get(url, headers=headers).content.decode('utf-8')
    print(response)
    soup = BeautifulSoup(response, "lxml")
    # url
    listUrl = soup.select('.image-link')
    for i in listUrl:
        url_list.append('https://maoyan.com' + str(i['href']))
# 	time.sleep(random.randint(20, 50))
print(url_list)

all_info = []
for singUrl in url_list:
    print(singUrl)
    response = requests.get(singUrl, headers=headers).content.decode('utf-8')
    print(response)
    soup = BeautifulSoup(response, "lxml")
    # 名字
    name = soup.select('.celeInfo-right .name')[0].string
    name = name.replace(' ', '')

    # 演员
    yyList = soup.select('.celebrity-group .celebrity-list .celebrity .info .name')
    yyStr = ''
    for i in yyList:
        yyStr += i.string
    yyStr = yyStr.replace('\n', '')
    yyStr = yyStr.replace(' ', '')
    # 导演
    dy = soup.select('.mod-content .celebrity-group .celebrity-list .info .name')[0].string

    # 类型
    lxList = soup.select('.celeInfo-right .movie-brief-container .text-link')
    lxStr = ''
    for i in lxList:
        lxStr += i.string
    lxStr = lxStr.replace(' ', '')
    # 上架时间
    sjsj = soup.select('.celeInfo-right .movie-brief-container .ellipsis')
    sjsjStr = sjsj[len(sjsj) - 1].string
    sjsjStr = sjsjStr.replace(' ', '')
    all_info.append([name, yyStr, dy, lxStr, sjsjStr])
    time.sleep(random.randint(20, 50))
print(all_info)


# 存表格
df = pd.DataFrame(all_info) #将获取到的所有数据生成表格
# 设置下边表格的字段
df.columns = ['名称', '演员', '导演', '类型','上架时间']
df.to_csv('测试.csv',encoding='utf_8_sig')
