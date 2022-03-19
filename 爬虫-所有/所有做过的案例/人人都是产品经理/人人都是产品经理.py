import random
import time
import re
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy.sparse import data
import jieba
import os
from PIL import Image
from os import path
from decimal import *
import requests
from bs4 import BeautifulSoup
import csv

headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
           'Cache-Control': 'max-age=0',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
           'Connection': 'keep-alive',
           'Host': 'www.woshipm.com',
           'Cookie': 'isFooterShow=feelinglucky; isOverlayShow=feelinglucky; dts_device_info=%7B%22device_id%22%3A%22%22%2C%22device_brand%22%3A%22%22%2C%22device_model%22%3A%22%22%2C%22client_type%22%3A%22pc%22%2C%22os_type%22%3A%22Win32%22%2C%22os_version%22%3A%22%22%2C%22network_type%22%3A%22%22%2C%22browser_type%22%3A%22Chrome%26dts1635315448912%22%2C%22browser_version%22%3A%2292.0.4515.159%22%7D; new_device_id=device_f2120250-ae0c-4d41-b87a-3cdd63bba816'
           }
# with open('data.csv', 'w', encoding='utf-8',newline='') as csvfile:
#     fieldnames = ['title', 'author', 'date', 'views', 'loves', 'zans', 'comment_num', 'art', 'url']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
all_info = []
for page_number in range(1, 3):
    page_url = "http://www.woshipm.com/category/pmd/page/{}".format(page_number)
    print('正在抓取第' + str(page_number) + '页>>>')
    response = requests.get(url=page_url, headers=headers, allow_redirects=True)
    time.sleep(5)
    if response.status_code == 200:
        page_data = response.text
        if page_data:
            soup = BeautifulSoup(page_data, 'lxml')
            article_urls = soup.find_all("h2", class_="post-title")
            for item in article_urls:
                url = item.find('a').get('href')
                res = requests.get(url=url, headers=headers, allow_redirects=False)
                print('正在抓取：' + url)
                if res.status_code == 200:
                    article = res.content.decode('utf-8')
                    if article:
                        # try:
                        sou = BeautifulSoup(article, 'lxml')
                        title = sou.select('.article--title')[0].string
                        print(title)
                        # title = soup.find(class_='article-title').get_text().strip()
                        author = sou.select('.ui-captionStrong')[0].string
                        date = sou.select('.meta--sup > time')[0].string
                        # date = sou.find(class_='post-meta-items').find_all(class_='post-meta-item')[
                        #     0].get_text().strip()
                        # views = sou.select('.meta--sup__right')[0].contents[0]
                        views = sou.select('.meta--sup__right')[0].contents[2].string
                        views = views.replace(' ', '')
                        views = views.replace('\n', '')
                        # views = sou.select('.meta--sup__right')[0].contents[4]

                        loves = sou.select('.meta--sup__right')[0].contents[4]
                        loves = loves.replace(' ', '')
                        loves = loves.replace('\n', '')

                        zans = sou.select('.article--actions__right >button>span')[4]
                        # print(zans,'-------------------------------')
                        comment = sou.find('ol', class_="comment-list").find_all('li')
                        comment_num = len(comment)
                        art = sou.find(class_="grap").get_text().strip()
                        print({'title': title, 'author': author, 'date': date, 'views': views,
                               'loves': loves, 'zans': zans, 'comment_num': comment_num})
                        all_info.append([title, author, date, views, loves, zans, comment_num, art, url])
                    # except:
                    #     print("抓取成功")
    time.sleep(random.randint(1, 10))
print(all_info)
df = pd.DataFrame(all_info)
df.columns = ['title', 'author', 'date', 'views', 'loves', 'zans', 'comment_num', 'art', 'url']
df.to_csv('data.csv', encoding='utf_8_sig')
print("抓取完毕！")


def views_to_num(item):
    m = re.search('.*?(万)', item['views'])
    if m:
        ns = item['views'][:-1]
        nss = Decimal(ns) * 10000
    else:
        nss = item['views']
    return int(nss)


# 数据清洗处理
def parse_woshipm():
    csv_file = "data.csv"
    csv_data = pd.read_csv(csv_file, low_memory=False)  # 防止弹出警告
    csv_df = pd.DataFrame(csv_data)
    csv_df['date'] = pd.to_datetime(csv_df['date'])
    csv_df['views_num'] = csv_df.apply(views_to_num, axis=1)
    data['title_length'] = data['title'].apply(len)
    data['year'] = data['date'].dt.year
    print(csv_df.info())
# if __name__ == '__main__':
# parse_woshipm()
