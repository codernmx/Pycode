import time
import xlwt
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import random

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34',
    "Cookie": 'BMAP_SECKEY=e7ccd76a71cca7384bc9d56993ddbed2e19bbff4744b85e39bb3d65be30e7613e76ae0b8689ae7f5bb14207898aef6950e69432a9314fa542a239fa64bfb5b45c6756257100384c9ac96001718aee8b563ecb4cf51b20fd1d89340e346c424d7f581fee99e8b3d10c7850fdac2264ca53d889a5481a24001d2f197632e25799a6c05f974f6fae9a280661438ff3c7f6ae9a05b252f4980c2a3cdda2895ca4e0eb895baf077e870b3ae71f6d8dfebcd06e220298771a772df2ae28eb78978cdc1b56ebb91662d35473805d2a5f8d24f8ce48c1de720da238e81ec009878f54ddd71bfb22203d7878c45ecfd7c61f1ae17; lianjia_uuid=741ff607-861b-42c2-a026-b46bc4e68618; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217d667be0445cf-07b62fd5b47cca-5919135e-1327104-17d667be045c18%22%2C%22%24device_id%22%3A%2217d667be0445cf-07b62fd5b47cca-5919135e-1327104-17d667be045c18%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; lianjia_ssid=c54dd85b-2d84-4b41-ad90-18dac13b0571; select_city=310000; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1638795363; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1638795478; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiZDA1NDFhNjNlZWQzOWE5NTgwMzVjNGYwMWE4ZDNkOTM5ZGJlNWFjODdkNWQzYzczYmRiYTMzMDY0YjI4N2JhZDY2NmExMzQ4OTRlOWU5ZTVjNjcxZWI3YWExY2YwMjRhMzA5ZDQ4NDZiYjNkNzg5M2M4NWUyYTY0OGM0MDVlYmRkOTY1ZTlhOTdhYmIwYWU2YTMxMmJjOGRjZjI2ZGJjZDgwYjEyNjJhZWMwMDc3YTAwZmIwZWFjODUzZmU5YWM5YTE1YjVkOGUzNWMyMTc3YmRiZjkwMDcxMjY2ZjAyNzk1NzdiMjAwZDc2M2YwNWYwMDQzOWNiZTAxZDM1ZGZlNzhjY2EyY2NhMjg1ODBmZmNmZjk3NDIwNDVlOTg4MGIwODFlMzljOGE1MDVjOTVhYjZiNGE5Y2Q3NTBhYzlkOWJjODY1MzMwYmJkYmZlZTA2NWE4OTc5YWNiYzUyYjYwNlwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCI0YmU5M2RlNlwifSIsInIiOiJodHRwczovL3NoLmtlLmNvbS9lcnNob3VmYW5nL3B1ZG9uZy9wZzIvIiwib3MiOiJ3ZWIiLCJ2IjoiMC4xIn0='
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
    isHuxing = False
    for i in chaoxiang:
        if '房屋朝向' in str(i) and (not isChao):
            fangwuchaoxiang = i.contents[1].string
            isChao = True
        if '配备电梯' in str(i) and (not isPei):
            peibeidianti = i.contents[1].string
            isPei = True
        if '户型结构' in str(i) and (not isHuxing):
            huxingjiegou = i.contents[1].string
            isHuxing = True
    if not isChao:
        fangwuchaoxiang = ''
    if not isPei:
        peibeidianti = ''
    if not isHuxing:
        huxingjiegou = ''

    guapaishijian = sou.select(".transaction ul>li")
    isGua = False
    isYong = False
    isChan = False
    isNian = False
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
        if '房屋年限' in str(i) and (not isNian):
            fangwunianxian = i.contents[1].string
            isNian = True

    if not isGua:
        guapaishijianStr = ''
    if not isYong:
        fangwuyongtu = ''
    if not isChan:
        chaquanleix = ''
    if not isNian:
        fangwunianxian = ''

    return  [danjia,xiaoqu,jiage,huxing,mianji,fangwuchaoxiang,jianzhushijian,fangwunianxian,huxingjiegou,zhuangxiuqingkuang]

# 一个地区最多获取一百页
for j in range(1, 100):
    print('当前获取页码------------',j)
    #需要改下边 每个分区 不一样
    url = 'https://sh.ke.com/ershoufang/chongming/pg' + str(j) + '/'
    res = requests.get(url, headers=headers).content.decode('utf-8')
    # print(res)
    soup = BeautifulSoup(res, "lxml")
    allUrl = soup.select(".img.VIEWDATA.CLICKDATA.maidian-detail")
    allInfo = []
    for i in allUrl:
        url = i['href']
        singleInfo = getDetail(url)
        # 存储
        df = pd.read_csv('获取一百页.csv', encoding='utf-8')
        df.loc[len(df)] = singleInfo  # 其中loc[]中需要加入的是插入地方dataframe的索引，默认是整数型
        df.columns = ['单价','小区','总价', '户型', '面积', '房屋朝向', '建成年代', '房产年限', '户型结构', '装修情况']
        df.to_csv('获取一百页.csv', index=False, encoding='utf_8_sig')
    time.sleep(random.randint(1, 10))
