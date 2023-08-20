import random
import pandas as pd
import requests
from bs4 import BeautifulSoup

headers = {
    "Cookie": 'UOR=,news.sina.com.cn,; ULV=1646571837976:1:1:1::; SEARCH-SINA-COM-CN=; SUB=_2A25PIMOkDeRhGeNG7VAR9CrMyDiIHXVsV7JsrDV_PUNbm9AfLWHikW9NSy8nwqCrFvz37BcEh4j0SAN-xVFfeear; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFnTj5Cf6OTDYFZWM1QCYXM5JpX5KzhUgL.Fo-RSoz7ShB7e0B2dJLoI7phqPiDdJ8kSKzc1KMt; ALF=1678108532; U_TRS1=000000e9.fe2d7c2e.6224b3f5.99ca807e; U_TRS2=000000e9.fe3e7c2e.6224b3f5.015bfb32; mYSeArcH=%u6C11%u6CD5%u5178; beegosessionID=622a493c1d40ebf245db5700050c01ca',
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.30'
}


def getItemInfo(url):
    try:
        response = requests.get(url, headers=headers).content.decode('utf-8')
        # print(response)
        print(len(response))
        soup = BeautifulSoup(response, "lxml")
        title = soup.select('.main-title')[0].string
        if soup.select('#article > p > font'):
            contentBox = soup.select('#article > p > font')
        else:
            contentBox = soup.select('#article > p')

        date = soup.select('.date')[0].string
        author = soup.select('.source.ent-source')[0].string
        content = ''
        for i in contentBox:
            if i.string:
                print(i.string)
                content += i.string
        return [title, date, author, content, url]
    except:
        print('获取单个信息报错了~~~~')


url = 'https://search.sina.com.cn/news'
for item in range(1, 21):
    data = {
        'q': '民法',
        'c': 'news',
        'range': 'all',
        'size': '10',
        'page': str(item),
    }
    response = requests.post(url, headers=headers, data=data).content.decode('utf-8')
    soup = BeautifulSoup(response, "lxml")
    listBox = soup.select('.box-result.clearfix > h2 > a')
    for i in listBox:
        try:
            print(i['href'])
            itemInfo = getItemInfo(i['href'])
        except:
            print('第一轮报错了~~~~~')
        df = pd.read_csv('新闻.csv', encoding='utf-8')
        df.loc[len(df)] = itemInfo  # 其中loc[]中需要加入的是插入地方dataframe的索引，默认是整数型
        df.columns = ['标题', '日期', '作者', '内容', '文章链接']
        df.to_csv('新闻.csv', index=False, encoding='utf_8_sig')
