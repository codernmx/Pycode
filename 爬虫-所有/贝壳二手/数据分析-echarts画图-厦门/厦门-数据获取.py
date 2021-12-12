import time

import xlwt
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import random

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43',
    "Cookie": 'lianjia_uuid=71b8c20d-fd04-48d6-95ee-017fe10d83ae; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217d8ff7ddb717e-0d13b2d762ffb3-3a67410c-1327104-17d8ff7ddb8345%22%2C%22%24device_id%22%3A%2217d8ff7ddb717e-0d13b2d762ffb3-3a67410c-1327104-17d8ff7ddb8345%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; select_city=350200; lianjia_ssid=d5ed38e9-c7ae-462d-a9ab-75c0aa1da079; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1639227951; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1639227964; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiMjY4NjJlNmExMzQyMzA4YTBlMDEyMDgyZjM4NDUwYWNjNjkwNDNjY2FiYjdiMGI4OWQyNzEyOGI0YzBjZDM3ZmFjYjhkZWQ2NDdjOWJhYzRlZjkyMGJiODY5ODUyOTg0ZjY0OTI4YTU3NzEyOWJjMzIyZTAyYTUzYTJlNWY3ODIwODJkOTU4Y2ViZjM5MmQxZDZjN2YxODZmNTQzNzI2ZDdlZTE0N2Y2NmI2ZTM0ZDZjYmQ5NTYzMWY1ZWMxY2I1NTBiNDhjMDZjY2FlZDBmM2Y5NDU4YmE5N2I0MTliOTY2Mzk2YWQwNDUwZTJhYmFjMWU2ZGYxYmNmODA5NTU4MGIzNWQ0MmQxNzllMTcxYWZjYTdlMzQyN2ZkZDUwYTY4MDk4NWI1YzhhNmFkMTI3ZTM3NTJiM2YxOTM2NDlkNThcIixcImtleV9pZFwiOlwiMVwiLFwic2lnblwiOlwiMjZhOTkzYWJcIn0iLCJyIjoiaHR0cHM6Ly94bS5rZS5jb20vZXJzaG91ZmFuZy90b25nYW4vIiwib3MiOiJ3ZWIiLCJ2IjoiMC4xIn0='
}


def getDetail(singurl):
    print('正在获取-------------->>>>>>>', singurl)
    req = requests.get(singurl, headers=headers).content.decode('utf-8')
    sou = BeautifulSoup(req, "lxml")
    huxing = sou.select(".houseInfo > .room > .mainInfo")[0].string
    louceng = sou.select(".houseInfo > .room > .subInfo")[0].string
    mianji = sou.select(".houseInfo > .area > .mainInfo")[0].string
    jianzhushijian = sou.select(".houseInfo > .area > .subInfo.noHidden")[0].contents[0].string
    zhuangxiuqingkuang = sou.select(".houseInfo > .type > .subInfo")[0].string
    jiage = sou.select(".price > .total")[0].string
    danjia = sou.select(".price > .text > .unitPrice > .unitPriceValue")[0].string
    xiaoqu = sou.select(".aroundInfo > .communityName > .info.no_resblock_a")[0].string
    quyu = sou.select(".aroundInfo > .areaName > .info >a")[0].string

    chaoxiang = sou.select(".m-content  .base  ul>li")
    isChao = False
    isPei = False
    for i in chaoxiang:
        if '房屋朝向' in str(i) and (not isChao):
            fangwuchaoxiang = i.contents[1].string
            isChao = True
        if '配备电梯' in str(i) and (not isPei):
            peibeidianti = i.contents[1].string
            isPei = True
    if not isChao:
        fangwuchaoxiang = ''
    if not isPei:
        peibeidianti = ''

    guapaishijian = sou.select(".transaction ul>li")
    isGua = False
    isYong = False
    isChan = False
    for i in guapaishijian:
        if '挂牌时间' in str(i) and (not isGua):
            guapaishijianStr = i.contents[1].string
            isGua = True
        if '房屋用途' in str(i) and (not isYong):
            fangwuyongtu = i.contents[1].string
            isYong = True
        if '产权所属' in str(i) and (not isChan):
            chaquanleix = i.contents[1].string
            isChan = True

    if not isGua:
        guapaishijianStr = ''
    if not isYong:
        fangwuyongtu = ''
    if not isChan:
        chaquanleix = ''

    return [quyu, xiaoqu, jiage, huxing, mianji, danjia, fangwuchaoxiang, louceng, zhuangxiuqingkuang,
            jianzhushijian, peibeidianti,chaquanleix,guapaishijianStr]

# 一个地区最多获取一百页
for j in range(1, 66):
    print('当前获取页码------------',j)
    url = 'https://xm.ke.com/ershoufang/tongan/pg' + str(j) + '/'
    res = requests.get(url, headers=headers).content.decode('utf-8')
    # print(res)
    soup = BeautifulSoup(res, "lxml")
    allUrl = soup.select(".img.VIEWDATA.CLICKDATA.maidian-detail")
    allInfo = []
    for i in allUrl:
        url = i['href']
        singleInfo = getDetail(url)
        # 存储
        df = pd.read_csv('厦门.csv', encoding='utf-8')
        df.loc[len(df)] = singleInfo  # 其中loc[]中需要加入的是插入地方dataframe的索引，默认是整数型
        df.columns = ['区域', '小区', '总价', '房型', '面积', '单价', '朝向', '楼层位置', '装修情况', '建筑时间', '是否有电梯','产权类型','挂牌时间']
        df.to_csv('厦门.csv', index=False, encoding='utf_8_sig')
    time.sleep(random.randint(1, 10))
