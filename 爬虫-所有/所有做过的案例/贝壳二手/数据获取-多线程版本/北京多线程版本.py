import time
import requests
from bs4 import BeautifulSoup
import pandas as pd
import threading

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34',
    "Cookie": 'lianjia_uuid=4642ac1c-3194-4244-adbf-42ef4174f915; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217d73ee63dca8e-0c3fc706043a43-5919135e-921600-17d73ee63ddae9%22%2C%22%24device_id%22%3A%2217d73ee63dca8e-0c3fc706043a43-5919135e-921600-17d73ee63ddae9%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; f-token=Ft8DBLiLeRMcRFrGwTZwpTvpMM1jgpPCJhThVPbyNrG2QAj5B8MAVwiamwvKK0zQeVffsB9GHEL4EjO0gY9Yw2QtUlIf6M3P2OWNP9k0XVafb7wSufEeya2/VTvxUlk7nVbgACewqR6vbBcQ; cy_ip=106.84.23.164; lianjia_ssid=765dbc91-c004-46fb-922a-39f2691473f3; select_city=110000; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1638327548,1638333666,1638520242; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1638520383; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiMTc0OTU2MTA1YWI5MjRkOWNiMzNmZWZkZjQxNjk0Y2U5NDhjZjBjOTZlODgzZTdlY2JlZDI3NjgwYTFlOTAwYjE0NDk4YWY5YzU3NWZlNmZlZDhkNjRjNDM0MzljMGFjNDhlNWQ3ZTBlZDgxZGRiNTc0ZDMyYzAyNjgwNmZkMzE0ZDQ2ZDcyZjE5NGFmYTE4NjMzZDI0ZmE0YjEyZmY2ODhjMzU2MmQ2YWQ3MGU4MmFmZjhmM2E5ODVhMzhlOWQ4NTdkOGQxZTkyZjU0NjNkZWViZTBhOTY5MjQ5MWQ0ZTdlZTExZjljNDRkOGRjMTg0ZTdmMGJlMjk3MWE2NmRiNTFjZTk3YTg0ZGQ3MWJhYzNkOTQ3ZWRiMjAzM2ZiMDk3NDZjOGIxMjEyZmEyZDU2N2I0ZDUzZThhNjEyYTRkYTIwMjE0OTQ4OTgwNTk5M2Y3ODhmNWY1NzQzODgwYzNjNlwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCJjNWQ3ODZkMFwifSIsInIiOiJodHRwczovL2JqLmtlLmNvbS9lcnNob3VmYW5nL2Zlbmd0YWkvcGcyLyIsIm9zIjoid2ViIiwidiI6IjAuMSJ9'
}

allInfo = []

lock = threading.Lock()


def getDetail(singurl):
    print('正在获取-------------->>>>>>>', singurl)
    req = requests.get(singurl, headers=headers).content.decode('utf-8')
    sou = BeautifulSoup(req, "lxml")
    huxing = sou.select(".houseInfo > .room > .mainInfo")[0].string
    louceng = sou.select(".houseInfo > .room > .subInfo")[0].string
    mianji = sou.select(".houseInfo > .area > .mainInfo")[0].string
    zhuangxiuqingkuang = sou.select(".houseInfo > .type > .subInfo")[0].string
    jiage = sou.select(".price > .total")[0].string
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
    with lock:
        singleInfo = [huxing, louceng, mianji, zhuangxiuqingkuang, jiage, xiaoqu, quyu, fangwuchaoxiang, peibeidianti,
                      guapaishijianStr, fangwuyongtu]
        df = pd.read_csv('北京一百页数据.csv', encoding='utf-8')
        df.loc[len(df)] = singleInfo  # 其中loc[]中需要加入的是插入地方dataframe的索引，默认是整数型
        df.columns = ['户型', '楼层', '面积', '装修情况', '价格', '小区', '区域', '房屋朝向', '配置电梯', '挂牌时间', '房屋用途']
        df.to_csv('北京一百页数据.csv', index=False, encoding='utf_8_sig')


def multi_thread(allUrl):
    print("开始")
    threads = []
    for url in allUrl:
        threads.append(
            threading.Thread(target=getDetail, args=(url,))
        )
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("结束")


if __name__ == "__main__":
    start = time.time()
    for j in range(6, 7):
        print('当前获取页码------------', j)
        url = 'https://bj.ke.com/ershoufang/fengtai/pg' + str(j) + '/'
        res = requests.get(url, headers=headers).content.decode('utf-8')
        print(res)
        soup = BeautifulSoup(res, "lxml")
        allUrlUrlLinkInfo = soup.select(".img.VIEWDATA.CLICKDATA.maidian-detail")
        allUrl = []
        for i in allUrlUrlLinkInfo:
            url = i['href']
            allUrl.append(url)
        multi_thread(allUrl)
    end = time.time()
    print("总共耗时:", end - start, "seconds")
