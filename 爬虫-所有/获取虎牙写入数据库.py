import requests
import chardet
from bs4 import BeautifulSoup
from requests import api
from lxml import etree
import threading
import time
import pymysql

flag = 1
channelLink, title, roomLink, viewNum, streamer = [], [], [], [], []

headUrl = 'https://www.huya.com/g/lol'

kind_path = '//*[@id="sidebar-scroll"]/div[2]/div[1]/div/div/a/@href'
title_path = '//*[@id="js-live-list"]/li/a/@title'
roomLink_path = '//*[@id="js-live-list"]/li/a[1]/@href'
viewNum_path = '//*[@id="js-live-list"]/li/span/span[2]/i[2]/text()'
streamer_path = '//*[@id="js-live-list"]/li/span/span[1]/img/@title'

hostName, userName, psWd, dbName = 'localhost', 'root', '20010903lc', 'mysql1'


def get_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
    response = requests.get(url, headers=headers)
    return response.text


def get_json(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
    response = requests.get(url, headers=headers)
    return response.json()


def insert_to_sql(chnLink, title, roomLink, viewNum, streamer):
    conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', db='db')
    sql = "insert into huya(chnLink, title, roomLink, viewNum, streamer) values('%s', '%s', '%s', '%s', '%s');" % (
    chnLink, title, roomLink, viewNum, streamer)
    print(sql)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()


def printAll(conn):
    cursor = conn.cursor()
    sql = "select * from huya;"
    cursor.execute(sql)
    data = cursor.fetchall()
    for x in data:
        print(x)


def main(s, id):
    global flag
    text = get_page(s)
    res = etree.HTML(text)
    print(s)
    print(id)

    title = res.xpath(title_path)
    roomLink = res.xpath(roomLink_path)
    viewNum = res.xpath(viewNum_path)
    streamer = res.xpath(streamer_path)

    for i in range(len(title)):
        print(title[i], roomLink[i], viewNum[i], streamer[i], sep='\n', end='\n\n')
        insert_to_sql(channelLink[id], title[i], roomLink[i], viewNum[i], streamer[i])


T = get_page(headUrl)
res = etree.HTML(T)
channelLink = res.xpath(kind_path)

for i in range(12):
    t = threading.Thread(target=main, args=(channelLink[i], i))
    t.start()
    conn = pymysql.connect(host=hostName, user=userName, password=psWd, db=dbName)
printAll(conn)
