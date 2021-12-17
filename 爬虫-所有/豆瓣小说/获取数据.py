# @Time : 2021/12/12 15:38
# @Author : VX:Until_Day_Break
# @SoftWare : PyCharm
import random
import time

import requests
import re
from bs4 import BeautifulSoup
import pymysql.cursors


# 给出url，爬取页面信息
def getHTMLText(url, kv):
    try:
        r = requests.get(url, timeout=30, headers=kv)
        r.raise_for_status()
        # r.encoding = r.apparent_encoding #该语句导致标签显示为乱码
        r.encoding = 'utf-8'
        return r.text
    except:
        print('爬取失败')


# 建立表格
def buildTable():
    conn = pymysql.connect(
        host='127.0.0.1',
        user='root',
        passwd='137928',  # 数据库密码
        db='douban_novels',
        charset='utf8mb4'
    )
    cursor = conn.cursor()

    sql_create1 = '''CREATE TABLE NOVELS(
                     NO INT PRIMARY KEY, 
                     TITLE VARCHAR(45), 
                     AUTHOR VARCHAR(45),
                     RATING DECIMAL(2,1),
                     PUBLISHER VARCHAR(45))             
                  '''
    cursor.execute(sql_create1)
    print('BOOKS CREATED')

    sql_create2 = '''CREATE TABLE NOVEL_TAGS(
                     BOOKNO INT, 
                     TAG VARCHAR(45))             
                  '''
    cursor.execute(sql_create2)
    print('TAGS CREATED')

    cursor.close()
    conn.close()


# 给出书籍编号、链接与标题，爬取书籍详情信息，形成字典并返回
def getBookInfo(no, href, title):
    kv = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 Edg/96.0.1054.53',
        "Cookie": 'bid=4TlQlROE0K8; ap_v=0,6.0; _pk_ses.100001.3ac3=*; __utma=30149280.1568299378.1639295472.1639295472.1639295472.1; __utmc=30149280; __utmz=30149280.1639295472.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=81379588.2032203717.1639295472.1639295472.1639295472.1; __utmc=81379588; __utmz=81379588.1639295472.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); dbcl2="236757327:icXHDkEuxkw"; ck=5Vaz; push_noty_num=0; push_doumail_num=0; _pk_id.100001.3ac3=ebf91ff52ab1ccf4.1639295472.1.1639296801.1639295472.; __utmb=30149280.4.10.1639295472; __utmb=81379588.4.10.1639295472'
        # 略。提示：将头文件的头部信息复制过来，加上引号和逗号形成字典，注意要删掉Accept-Encoding一行。
    }

    html = getHTMLText(href, kv)
    book = BeautifulSoup(html, 'html.parser')

    bookInfo = {'author': '未知',
                'rating': 0.0,
                'publisher': '未知'}

    bookInfo['no'] = no

    bookInfo['title'] = title

    rating = book.find('strong')
    if rating.string:
        try:
            bookInfo['rating'] = float(rating.text)
        except:
            pass

    for keyTag in book.find_all(name='span', attrs={'class': 'pl'}):
        if re.search(r'作者', str(keyTag.string)):
            author = keyTag  # .parent
            for i in range(4):
                author = author.next_element
            author = author.replace('\n', '')
            author = author.replace(' ', '')
            bookInfo['author'] = author

    for keyTag in book.find_all(string='出版社:'):
        publisher = keyTag.parent
        for i in range(2):
            publisher = publisher.next_element
        publisher = publisher.replace('\n', '')
        publisher = publisher.replace(' ', '')
        bookInfo['publisher'] = publisher

    tags = []
    for tag in book.find_all(attrs={'class': 'tag'}):
        tags.append(tag.text)
    print(tags)
    bookInfo['tags'] = tags

    print(bookInfo)
    return bookInfo


# 爬取豆瓣读书小说标签下综合排序前1000本小说的信息
def getBooks():
    conn = pymysql.connect(
        host='127.0.0.1',
        user='root',
        passwd='137928',  # 数据库密码
        db='douban_novels',
        charset='utf8mb4'
    )
    cursor = conn.cursor()

    no = 0
    start_url = "https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start="
    kv = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 Edg/96.0.1054.53',
        "Cookie": 'bid=4TlQlROE0K8; ap_v=0,6.0; _pk_ses.100001.3ac3=*; __utma=30149280.1568299378.1639295472.1639295472.1639295472.1; __utmc=30149280; __utmz=30149280.1639295472.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=81379588.2032203717.1639295472.1639295472.1639295472.1; __utmc=81379588; __utmz=81379588.1639295472.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); dbcl2="236757327:icXHDkEuxkw"; ck=5Vaz; push_noty_num=0; push_doumail_num=0; _pk_id.100001.3ac3=ebf91ff52ab1ccf4.1639295472.1.1639296801.1639295472.; __utmb=30149280.4.10.1639295472; __utmb=81379588.4.10.1639295472'
        # 略。提示：将头文件的头部信息复制过来，加上引号和逗号形成字典，注意要删掉Accept-Encoding一行。
    }

    for i in range(50,250):
        print('第{0}页'.format(i + 1))
        end_url = str(20 * i)
        html = getHTMLText(start_url + end_url, kv)
        topBooks = BeautifulSoup(html, 'html.parser')

        for book in topBooks.find_all('a'):
            href = str(book['href'])
            if re.match(r'https://book.douban.com/subject/', href):
                title = book.get('title')
                if title:
                    no += 1

                    info = getBookInfo(no, href, title)

                    sql_insert1 = "INSERT INTO NOVELS(NO, TITLE, AUTHOR, RATING, PUBLISHER)\
                                  VALUES({0}, '{1}', '{2}', {3}, '{4}')".format(info['no'], \
                                                                                info['title'], info['author'],
                                                                                str(info['rating']), info['publisher'])
                    cursor.execute(sql_insert1)
                    print(('book{0} stored').format(info['no']))

                    tags = info['tags']
                    for i in range(len(tags)):
                        sql_insert2 = "INSERT INTO NOVEL_TAGS(BOOKNO, TAG) VALUES({0}, '{1}')".format(info['no'],
                                                                                                      tags[i])
                        cursor.execute(sql_insert2)
                    print(('book{0} tags stored').format(info['no']))
                    conn.commit()
        time.sleep(random.randint(1, 5))
    time.sleep(random.randint(1, 10))
    cursor.close()
    conn.close()


if __name__ == '__main__':
    # buildTable()
    getBooks()
