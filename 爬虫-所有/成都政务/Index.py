import random
import time
import requests
import json
import re
from bs4 import BeautifulSoup
import math


headers = {
    "Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    "Accept-Encoding": 'gzip, deflate',
    "Accept-Language": 'zh-CN,zh;q=0.9',
    "Cache-Control": 'max-age=0',
    "Connection": 'keep-alive',
    "Cookie": 'JSESSIONID=C5F7C424F0783FE6FE2FF04575669428',
    "Host": '12345.chengdu.gov.cn',
    "Referer": 'http://12345.chengdu.gov.cn/moreTelByClass?TelType=1161',
    "Upgrade-Insecure-Requests": '1',
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}

infoList = []
url = 'http://12345.chengdu.gov.cn/moreTelByClass?TelType=1155'
response = requests.get(url, headers=headers).content.decode('utf-8')
soup = BeautifulSoup(response, "lxml")
list_a = soup.select('.listL > div > a')
# 这是每一个来电分类的链接
number = 0
for i in list_a:
    dictInfo = {}
    url = 'http://12345.chengdu.gov.cn/' + i['href']  # 每一个大分类的链接
    print('当前主分类url--->>>>>>', url)
    TelType = i['href'].split('=')[len(i['href'].split('=')) - 1]  # 获取TelType
    tel_cat = i.contents[0].text  # 分类
    dictInfo['tel_cat'] = tel_cat
    # 请求分类的第一个网页
    response = requests.get(url, headers=headers).content.decode('utf-8')
    # print(response)
    soup = BeautifulSoup(response, "lxml")
    pageCount = 0  # 初始化pageCount
    x = re.findall(re.compile("(.*?);"), str(soup))
    for a in x:
        if ('var iRecCount =' in a):
            pageCount = math.ceil(int(a.split('=')[-1]) / 15)  # 算出总页数
    print('当前分类总页数------>>', pageCount)

    # for遍历
    for iii in range(0, pageCount):
        url = 'http://12345.chengdu.gov.cn/moreTelByClass?page=' + str(iii)
        data = {
            "TelType": TelType,
            "pageID": iii
        }
        res = requests.post(url, headers=headers, data=data).content.decode('utf-8')
        soupP = BeautifulSoup(res, "lxml")
        list_b = soupP.select('.left5 > UL > LI > A')  # 每一页数据的列表
        for jjj in range(0, len(list_b)):
            print(jjj)
            singlepageUlr = 'http://12345.chengdu.gov.cn/' + list_b[jjj]['href']  # 单个页面详情
            for i in list_b[jjj].contents:
                if 'listTit7' in str(i):
                    dictInfo['tel_title'] = i.string
                if 'WIDTH: 80px; OVERFLOW: hidden; WHITE-SPACE: nowrap; TEXT-OVERFLOW: ellipsis;' in str(
                    i) and 'listTit2' in str(i):
                    dictInfo['handle_depart'] = i.string  # 办理单位
                if 'WIDTH: 80px; OVERFLOW: hidden; WHITE-SPACE: nowrap; TEXT-OVERFLOW: ellipsis;' in str(
                    i) and 'listTit8' in str(i):
                    dictInfo['status'] = i.string  # 状态
                if 'style="WIDTH: 90px;"' in str(i) and 'listTit2' in str(i):
                    dictInfo['type'] = i.string  # 类别
                if 'style="WIDTH: 60px"' in str(i) and 'listTit8' in str(i):
                    dictInfo['pageviews'] = i.string  # 访问量
            # 页面取完数据获取详情里边的数据

            print('每个详细信息url---------->>>>>', singlepageUlr)
            dictInfo['url'] = singlepageUlr
            resDetail = requests.get(singlepageUlr, headers=headers, data=data).content.decode('utf-8')
            soupD = BeautifulSoup(resDetail, "lxml")
            list_c = soupD.select('.rightside1 > TABLE > TBODY > tr')  # 每一页数据的列表
            print(len(list_c),'——————————————————————————>>>>>>>')
            # 取时间
            for i in list_c[2].contents:
                if 'class="td2 f12pxgrey"' in str(i):
                    dictInfo['tel_date'] = i.string
            # 来电内容
            for i in list_c[3].contents:
                if 'f12pxgrey' in str(i):
                    # print(i.string)
                    dictInfo['tel_cont'] = i.string
            # 结果
            for i in list_c[-1].contents:
                if 'f12pxgrey' in str(i):
                    dictInfo['handle_result'] = i.string.replace(' ', '')
            # 处理部门
            result = ''
            for i in list_c[5:-2]:
                for k in i.contents:
                    result += k.string.replace('\n', '')
            dictInfo['proc_departs'] = result
            time.sleep(random.randint(0,5))
            infoList.append(dictInfo)
            number += 1
            dictInfo = {}
            dictInfo['tel_cat'] = tel_cat
            # print(infoList)
            # 测试----如果大于200 存一个
            print('当前----------->>>>', number)
            if (len(infoList) > 10):
                with open('测试.json', 'w', encoding='utf-8') as f:
                    json.dump(infoList, f, ensure_ascii=False)
        # time.sleep(random.randint(5, 20))
    # time.sleep(random.randint(5, 20))
