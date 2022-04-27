# PyCode-Github/爬虫-所有
# _*_ coding: utf-8 _*_
# @Time : 2022/4/27 21:19
# @FileName : 网易新闻.py
import random
import time

import pandas as pd
import requests
from bs4 import BeautifulSoup

headers = {
    "Cookie": 'WM_TID=vmnobKPZql5FQQAVBVIqvvBV1sX%2F4YTJ; WM_NI=cIS3xusLaiBpcwc1aU3Xy%2FsmuTRyBvwuDzOyWuyiI%2F8JTbyERrL8KzkBmmJXGu98YyEgTM77a89tnKc4OxLEzkHfAm4SOu8K0DyCznFvGgXszoVhvB6ijwhTFYu5Vjt7eUM%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee86d180a596aeb8e480b1968fb6d84e868e9e86c15e97e7b798fc738de9fdd1d32af0fea7c3b92aa1979dd4fb7fb194af8ac17ca1a9add2e45ff188b7d0f267b78c9e9ac17eb5ab8c9bce7395abb78acc25fc969c83fc4f92ae84d9ca72a99ea38ec95485abf7d9dc7387b99caeb63da3e8f795ed41a1ec8199cf4fbab58887c467f88d8196bb41f49cb7a4f96686aa8988db79bab19a89f54af6b7a698eb608687bbd6d562b8e9abb6d037e2a3; _ntes_nnid=dd35c7c0872421fca032e3d8604a9733,1650637481352; _ntes_nuid=dd35c7c0872421fca032e3d8604a9733; _antanalysis_s_id=1651065371996',
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.30'
}


# 获取文章文字
def getItemInfo(url):  # 获取文字
    try:
        res = requests.get(url, headers=headers).content.decode('utf-8')
        soup = BeautifulSoup(res, "lxml")
        title = soup.select('.post_title')[0].string  # （标题）
        contentList = soup.select('.post_body > p')
        content = ''  # （内容）
        for i in contentList:
            content += str(i.string)
        content = str(content).replace('None', '')
        content = content[0:200] #截取前200个
        time = soup.select('.post_info')[0].contents[0].string
        time = str(time).split('　')[0]  # 截取时间
        time = time.replace('  ', '')  # 替换空格（时间）
        author = soup.select('.post_info')[0].contents[1].string  # （作者）
        print('获取成功~~', url)
        return [title, author, time, content, url]
    except:
        title = soup.select('.title_wrap > h1')[0].string  # （视频标题）
        print('视频链接~~', url)
        return [title, ' ', ' ', ' ', url]


# 获取所有URL
# url = 'https://www.163.com/search?keyword=%E8%AF%88%E9%AA%97'  #获取诈骗关键字
url = 'https://www.163.com/search?keyword=%E5%8F%8D%E8%AF%88'  # 获取反诈关键字
response = requests.get(url, headers=headers).content.decode('utf-8')
print(len(response))
soup = BeautifulSoup(response, "lxml")
listBox = soup.select('.keyword_list > .keyword_new > h3 > a')
for i in listBox:
    try:
        itemInfo = getItemInfo(i['href'])
        # time.sleep(random.randint(1, 5))  # 延时随机1-5
    except:
        print('获取所有URl报错了~~~~~')
    df = pd.read_csv('新闻数据.csv', encoding='utf-8')
    df.loc[len(df)] = itemInfo  # 其中loc[]中需要加入的是插入地方dataframe的索引，默认是整数型
    df.columns = ['标题', '作者', '时间', '内容', '文章链接']
    df.to_csv('新闻数据.csv', index=False, encoding='utf_8_sig')
print('总共获取数据：', len(listBox))
