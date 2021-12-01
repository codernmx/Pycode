import time
import xlwt
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import random

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34',
}

url ='https://www.haodanku.com/allitem/hdk_allitem_list?p=2'
def getDetail(singurl):
    print('正在获取-------------->>>>>>>', singurl)
    req = requests.get(singurl, headers=headers).content.decode('utf-8')

    item_info = json.loads(req)['item_info']
    for i in item_info:
        itemshorttitle = i['itemshorttitle']# 短标题
        itemdesc = i['itemdesc']# 详情
        itempic = i['itempic']# 图片
        itemendprice = i['itemendprice']# 券后价
        print(itemdesc)
getDetail(url)