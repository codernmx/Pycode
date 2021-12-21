import time

import pymysql
import xlwt
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import random


headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34',
    "Cookie": 'lianjia_uuid=741ff607-861b-42c2-a026-b46bc4e68618; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217d667be0445cf-07b62fd5b47cca-5919135e-1327104-17d667be045c18%22%2C%22%24device_id%22%3A%2217d667be0445cf-07b62fd5b47cca-5919135e-1327104-17d667be045c18%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%7D; lianjia_ssid=4424b121-24ed-499f-a2a6-056d765f2cc7; select_city=110000; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1638270738; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1638270763; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiZDA1NDFhNjNlZWQzOWE5NTgwMzVjNGYwMWE4ZDNkOTM5ZGJlNWFjODdkNWQzYzczYmRiYTMzMDY0YjI4N2JhZDA4OWYyMDkzOGY1MDY1ZWQyZjgwNDc2NDBiNjRmYTYwNTNmZTkzMzNmNDM3NGNjMDk4MzI0ODM1Yzc0YWIwOTMzZjkyNGM1ZmFjNGMwMWQ4ZDFkNzk1MjQ4ZGIzMjViZDE4OWU3MTk4ZTk3MWE5MTgyZTk5YjM4MGYwMjdkMjg3NzQ1M2JjNGJlZTE1MjFlNjcwY2VlMGIyNjJjODA5MjJhMjNhNjg4MGE1ZjgxNmFmMjNiODAxOGI5NTRlOTQ2ODlhYjRiMDIxMGQ0ODY0NmVjMTMxYzQwNGNkNjlkMjhiOGE3NWEzM2Q2Y2NhNmIxMmNkNWU5Y2JiMDZjZDllNjIwYmVkM2I5NjE3MTYxMGJmNjRmZGJiMGNiYTYzOGQwYlwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCJmMGUzODI3MFwifSIsInIiOiJodHRwczovL2JqLmtlLmNvbS9lcnNob3VmYW5nL3BnMi8iLCJvcyI6IndlYiIsInYiOiIwLjEifQ=='
}


def getDetail(singurl):
    print('正在获取-------------->>>>>>>', singurl)
    req = requests.get(singurl, headers=headers).content.decode('utf-8')
    sou = BeautifulSoup(req, "lxml")
    huxing = sou.select(".houseInfo > .room > .mainInfo")[0].string
    louceng = sou.select(".houseInfo > .room > .subInfo")[0].string
    mianji = sou.select(".houseInfo > .area > .mainInfo")[0].string
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
    for i in guapaishijian:
        if '挂牌时间' in str(i) and (not isGua):
            guapaishijianStr = i.contents[1].string
            isGua = True
        if '房屋用途' in str(i) and (not isYong):
            fangwuyongtu = i.contents[1].string
            isYong = True

    if not isGua:
        guapaishijianStr = ''
    if not isYong:
        fangwuyongtu = ''
    # 户型, 楼层, 面积, 装修情况, 价格, 小区, 区域, 房屋朝向, 配置电梯, 挂牌时间, 房屋用途, 单价
    return [huxing, louceng, mianji, zhuangxiuqingkuang, jiage, xiaoqu, quyu, fangwuchaoxiang, peibeidianti,
            guapaishijianStr, fangwuyongtu, danjia]


# 最多获取一百页数据
for j in range(1, 100):
    print('当前获取页码------------', j)
    url = 'https://gy.ke.com/ershoufang/guanshanhuqu/pg' + str(j) + '/'
    res = requests.get(url, headers=headers).content.decode('utf-8')
    # print(res)
    soup = BeautifulSoup(res, "lxml")
    allUrl = soup.select(".img.VIEWDATA.CLICKDATA.maidian-detail")
    allInfo = []
    for i in allUrl:
        url = i['href']
        singleInfo = getDetail(url)
        # 存储
        df = pd.read_csv('贵阳一百页数据.csv', encoding='utf-8')
        df.loc[len(df)] = singleInfo  # 其中loc[]中需要加入的是插入地方dataframe的索引，默认是整数型
        df.columns = ['户型', '楼层', '面积', '装修情况', '价格', '小区', '区域', '房屋朝向', '配置电梯', '挂牌时间', '房屋用途', '单价']
        df.to_csv('贵阳一百页数据.csv', index=False, encoding='utf_8_sig')
    time.sleep(random.randint(1, 10))
