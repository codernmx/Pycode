# -*- coding: utf-8 -*-
# @Time : 2021/12/8 10:20
# @Author : MinChess
# @File : weibo.py
# @Software: PyCharm
import requests
from lxml import etree
from urllib.parse import quote
import csv
import re
import time
import random
from html.parser import HTMLParser

headers_com = {
    'Cookie': 'SINAGLOBAL=8530308723572.626.1594801309423; UOR=,,www.baidu.com; ALF=1649247528; SUB=_2A25PIYh4DeRhGeVJ7lQS8C_Oyz-IHXVs7SgwrDV8PUJbkNAKLU7kkW1NT8v1zHG7ndkzD92IXpMb9pyYayxZv5p-; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh0wcVpufLRVzXYfa3pjY.Q5JpX5oz75NHD95Q0S0-ce05peo50Ws4Dqcjci--fi-i2i-zpi--fi-82iK.7i--Xi-zRiKy2i--Ri-88i-zRi--fiKyWi-2Ri--Xi-zRi-zc; ULV=1646658060503:5:1:1:243708356859.10474.1646658060493:1627299580145; WBPSESS=--AcJbA8Oa9zAFKPUTSD5sLC7tlhjwiMerLK05g7m8lHcPohg3YiE1uguj3KKHQSomGyiIUaCIxDcQ8SorKYE4ke6D9-V88QEw1v2kXwKPZzIIKl9DmiSwzsb_sbtUU6Qjd2cgrlnOdjlrSBRc2ayQ==; XSRF-TOKEN=6W6_mdFm7HVugNLWYT4De_m1',
    # 'Cookie': 'SINAGLOBAL=6692839056672.04.1575211969653; XSRF-TOKEN=dvRQl6BFSaBrVQ9aoz2c-lau; _s_tentry=weibo.com; Apache=3761453327801.136.1646320550576; ULV=1646320550596:1:1:1:3761453327801.136.1646320550576:; UOR=,,www.baidu.com; login_sid_t=c055241708da7f3454da76e72babbf12; cross_origin_proto=SSL; ALF=1678169320; SCF=ApwEkyMNH24hMtFSKVLzEW_0pBDzpWweLRBt1V_aCUAGg_823TfLvw0CHZ5_j8J4itdbpBNo1i3scT2gChOhJEI.; WBPSESS=bwbIVYtIkNrJPKlhfJ1TLTI4ZrCYeqURLSWwfQ5QY1_xCzsPzZlG2luc9qbEWVTtt5VJEkReleyuvjb8g-Jcu6vCjNqx2-d46YFyR7feEIwjYWLqWU7e4c64BX02U-ujI5rXPTsoipPuP6cTVWkBFQ==; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWy-ExKsYH4ouv2pp40B4Md5NHD95QESoBcSoBXe0.pWs4Dqcj8TK84Ug2t; SSOLoginState=1646659617; SUB=_2A25PInhxDeRhGeRI71QX9CrPwj2IHXVs7Rg5rDV8PUJbkNB-LW3fkW1NUrg5CZibBb5RX_J1BdEiJc81kTpMpuEb',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}
headers_cn = {
    'Cookie': 'SUB=_2A25PIYh3DeRhGeVJ7lQS8C_Oyz-IHXVs7Sg_rDV6PUJbkdAKLU2nkW1NT8v1zA4Q0lakelzRb0x1ELOzOBSmUcOp; SCF=AtH4DCXADZs6FfnqoYSmwpUovXDFEGtPUyLpA8VSmAi8gymQXfWethijtJEZtyxd0rxS2BSamrES0Z3AQaim2FQ.; _T_WM=16923311902; WEIBOCN_FROM=1110006030; MLOGIN=1; M_WEIBOCN_PARAMS=uicode%3D20000174',
    # 'Cookie': '_T_WM=48060870584; BAIDU_SSP_lcr=https://security.weibo.com/; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWy-ExKsYH4ouv2pp40B4Md5NHD95QESoBcSoBXe0.pWs4Dqcj8TK84Ug2t; SCF=ApwEkyMNH24hMtFSKVLzEW_0pBDzpWweLRBt1V_aCUAGx_5t8MsvZWG0xU0wbpvlyHnR-BdbVzll0Tm4JqNmyzs.; SUB=_2A25PInhxDeRhGeRI71QX9CrPwj2IHXVs7Rg5rDV6PUJbktCOLRTYkW1NUrg5CV_Fr49NHRIZpmpCqqeqJSJ0Dpol; SSOLoginState=1646659617',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}

baseUrl = 'https://s.weibo.com/weibo?q={}&Refer=index'
topic = '郑州暴雨'
csvfile = open(topic + '.csv', 'a', newline='', encoding='utf-8-sig')
writer = csv.writer(csvfile)


def getTopic(url):
    page = 0
    pageCount = 1

    while True:
        weibo_content = []
        weibo_liketimes = []
        weibo_date = []
        page = page + 1
        tempUrl = url + '&page=' + str(page)
        print('-' * 36, tempUrl, '-' * 36)
        response = requests.get(tempUrl, headers=headers_com)
        html = etree.HTML(response.text, parser=etree.HTMLParser(encoding='utf-8'))
        count = len(html.xpath('//div[@class="card-wrap"]')) - 2
        for i in range(1, count + 1):
            try:
                contents = html.xpath('//div[@class="card-wrap"][' + str(
                    i) + ']/div[@class="card"]/div[1]/div[2]/p[@node-type="feed_list_content_full"]')
                contents = contents[0].xpath('string(.)').strip()  # 读取该节点下的所有字符串
            except:
                contents = html.xpath('//div[@class="card-wrap"][' + str(
                    i) + ']/div[@class="card"]/div[1]/div[2]/p[@node-type="feed_list_content"]')
                # 如果出错就代表当前这条微博有问题
                try:
                    contents = contents[0].xpath('string(.)').strip()
                except:
                    continue
            contents = contents.replace('收起全文d', '')
            contents = contents.replace('收起d', '')
            contents = contents.split(' 2')[0]

            # 发微博的人的名字
            name = \
                html.xpath(
                    '//div[@class="card-wrap"][' + str(i) + ']/div[@class="card"]/div[1]/div[2]/div[1]/div[2]/a')[
                    0].text
            # 微博url
            weibo_url = html.xpath(
                '//div[@class="card-wrap"][' + str(i) + ']/div[@class="card"]/div[1]/div[2]/p[@class="from"]/a/@href')[
                0]
            url_str = '.*?com\/\d+\/(.*)\?refer_flag=\d+_'
            res = re.findall(url_str, weibo_url)
            weibo_url = res[0]
            host_url = 'https://weibo.cn/comment/' + weibo_url
            # 发微博的时间
            timeA = \
                html.xpath(
                    '//div[@class="card-wrap"][' + str(i) + ']/div[@class="card"]/div[1]/div[2]/p[@class="from"]/a')[
                    0].text.strip()
            # 点赞数
            likeA = html.xpath(
                '//div[@class="card-wrap"][' + str(i) + ']/div[@class="card"]/div[2]/ul[1]/li[3]/a/button/span[2]')[
                0].text
            hostComment = \
                html.xpath('//div[@class="card-wrap"][' + str(i) + ']/div[@class="card"]/div[2]/ul[1]/li[2]/a')[0].text
            # 如果点赞数为空，那么代表点赞数为0
            if likeA == '赞':
                likeA = 0
            if hostComment == '评论 ':
                hostComment = 0
            if hostComment != 0:
                print('正在爬取第', page, '页，第', i, '条微博的评论。')
                getComment(host_url)
            try:
                hosturl, host_sex, host_location, hostcount, hostfollow, hostfans = getpeople(name)
                list = ['微博', name, hosturl, host_sex, host_location, hostcount, hostfollow, hostfans, contents, timeA,
                        likeA]
                writer.writerow(list)
            except:
                continue
            print('=' * 66)
        try:
            if pageCount == 1:
                pageA = html.xpath('//*[@id="pl_feedlist_index"]/div[5]/div/a')[0].text
                print(pageA)
                pageCount = pageCount + 1
            elif pageCount == 50:
                print('没有下一页了')
                break
            else:
                pageA = html.xpath('//*[@id="pl_feedlist_index"]/div[5]/div/a[2]')[0].text
                pageCount = pageCount + 1
                print(pageA)
        except:
            print('没有下一页了')
            break


def getpeople(name):
    findPoeple = 0
    url2 = 'https://s.weibo.com/user?q='
    while True:
        try:
            response = requests.post('https://weibo.cn/search/?pos=search', headers=headers_cn,
                                     data={'suser': '找人', 'keyword': name})
            tempUrl2 = url2 + quote(str(name)) + '&Refer=weibo_user'
            print('搜索页面', tempUrl2)
            response2 = requests.get(tempUrl2, headers=headers_com)
            html = etree.HTML(response2.content, parser=etree.HTMLParser(encoding='utf-8'))
            hosturl_01 = html.xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/div[3]/div[1]/div[2]/div/a/@href')[0]
            url_str = '.*?com\/(.*)'
            res = re.findall(url_str, hosturl_01)
            hosturl = 'https://weibo.cn/' + res[0]
            print('找人主页：', hosturl)
            break
        except:
            if findPoeple == 10:
                stop = random.randint(60, 300)
                print('IP被封等待一段时间在爬', stop, '秒')
                time.sleep(stop)
            if response.status_code == 200:
                return
            print('找人')
            time.sleep(random.randint(0, 10))
            findPoeple = findPoeple + 1
    while True:
        try:
            response = requests.get(hosturl, headers=headers_cn)
            # print('微博主人个人主页',hosturl)
            html = etree.HTML(response.content, parser=etree.HTMLParser(encoding='utf-8'))
            # 获取微博数
            # html2 = etree.HTML(html)
            # print(html2)
            hostcount = html.xpath('/html/body/div[4]/div/span')[0].text
            # 正则表达式，只获取数字部分
            # print(hostcount)
            hostcount = re.match('(\S\S\S)(\d+)', hostcount).group(2)
            # 获取关注数
            hostfollow = html.xpath('/html/body/div[4]/div/a[1]')[0].text
            # 正则表达式，只获取数字部分
            hostfollow = re.match('(\S\S\S)(\d+)', hostfollow).group(2)
            # 获取粉丝数
            hostfans = html.xpath('/html/body/div[4]/div/a[2]')[0].text
            # 正则表达式，只获取数字部分
            hostfans = re.match('(\S\S\S)(\d+)', hostfans).group(2)
            # 获取性别和地点
            host_sex_location = html.xpath('/html/body/div[4]/table/tr/td[2]/div/span[1]/text()')
            # print(hostcount, hostfollow, hostfans, host_sex_location)
            break
        except:
            print('找人失败')
            time.sleep(random.randint(0, 10))
            pass
    try:
        host_sex_locationA = host_sex_location[0].split('\xa0')
        host_sex_locationA = host_sex_locationA[1].split('/')
        host_sex = host_sex_locationA[0]
        host_location = host_sex_locationA[1].strip()
    except:
        host_sex_locationA = host_sex_location[1].split('\xa0')
        host_sex_locationA = host_sex_locationA[1].split('/')
        host_sex = host_sex_locationA[0]
        host_location = host_sex_locationA[1].strip()

    # print('微博信息',name,hosturl,host_sex,host_location,hostcount,hostfollow,hostfans)
    # nickname, hosturl, host_sex, host_location, hostcount, hostfollow, hostfans
    return hosturl, host_sex, host_location, hostcount, hostfollow, hostfans


def getComment(hosturl):
    page = 0
    pageCount = 1
    count = []  # 内容
    date = []  # 时间
    like_times = []  # 赞
    user_url = []  # 用户url
    user_name = []  # 用户昵称
    while True:
        page = page + 1
        print('正在爬取第', page, '页评论')
        if page == 1:
            url = hosturl
        else:
            url = hosturl + '?page=' + str(page)
        print(url)
        try:
            response = requests.get(url, headers=headers_cn)
        except:
            break
        html = etree.HTML(response.content, parser=etree.HTMLParser(encoding='utf-8'))
        user_re = '<div\sclass="c"\sid="C_\d+.*?<a\shref="(.*?)"'
        user_name_re = '<div\sclass="c"\sid="C_\d+.*?<a\shref=".*?">(.*?)</a>'
        co_re = '<div\sclass="c"\sid="C_\d+.*?<span\sclass="ctt">(.*?)</span>'
        zan_re = '<div\sclass="c"\sid="C_\d+.*?赞\[(.*?)\]'
        date_re = '<div\sclass="c"\sid="C_\d+.*?<span\sclass="ct">(.*?);'
        count_re = '回复<a.*</a>:(.*)'
        user_name2 = re.findall(user_name_re, response.text)
        zan = re.findall(zan_re, response.text)
        date_2 = re.findall(date_re, response.text)
        count_2 = re.findall(co_re, response.text)
        user_url2 = re.findall(user_re, response.text)
        flag = len(zan)
        for i in range(flag):
            count.append(count_2[i])
            date.append(date_2[i])
            like_times.append(zan[i])
            user_name.append(user_name2[i])
            user_url.append('https://weibo.cn' + user_url2[i])
        try:
            if pageCount == 1:  # 第一页找下一页标志代码如下
                pageA = html.xpath('//*[@id="pagelist"]/form/div/a')[0].text
                print('=' * 40, pageA, '=' * 40)
                pageCount = pageCount + 1
            else:  # 第二页之后寻找下一页的标志
                pageA = html.xpath('//*[@id="pagelist"]/form/div/a[1]')[0].text
                pageCount = pageCount + 1
                print('=' * 40, pageA, '=' * 40)
        except:
            print('没有下一页')
            break
    print("#" * 20, '评论爬取结束，下面开始爬取评论人信息', "#" * 20)
    print(len(like_times), len(count), len(date), len(user_url), len(user_name))
    flag = min(len(like_times), len(count), len(date), len(user_url), len(user_name))
    for i in range(flag):
        host_sex, host_location, hostcount, hostfollow, hostfans = findUrl(user_url[i])
        # print('评论',user_name[i], user_url[i] , host_sex, host_location,hostcount, hostfollow, hostfans,count[i],date[i],like_times[i])
        print('在爬取第', page, '页', '第', i + 1, '个人')
        list111 = ['评论', user_name[i], user_url[i], host_sex, host_location, hostcount, hostfollow, hostfans, count[i],
                   date[i], like_times[i]]
        writer.writerow(list111)
        time.sleep(random.randint(0, 2))


def findUrl(hosturl):
    while True:
        try:
            print(hosturl)
            response = requests.get(hosturl, headers=headers_cn)
            html = etree.HTML(response.content, parser=etree.HTMLParser(encoding='utf-8'))
            hostcount = html.xpath('/html/body/div[4]/div/span')[0].text
            hostcount = re.match('(\S\S\S)(\d+)', hostcount).group(2)
            hostfollow = html.xpath('/html/body/div[4]/div/a[1]')[0].text
            hostfollow = re.match('(\S\S\S)(\d+)', hostfollow).group(2)
            hostfans = html.xpath('/html/body/div[4]/div/a[2]')[0].text
            hostfans = re.match('(\S\S\S)(\d+)', hostfans).group(2)
            host_sex_location = html.xpath('/html/body/div[4]/table/tr/td[2]/div/span[1]/text()')
            break
        except:
            print('找人失败')
            time.sleep(random.randint(0, 5))
            pass
    try:
        host_sex_locationA = host_sex_location[0].split('\xa0')
        host_sex_locationA = host_sex_locationA[1].split('/')
        host_sex = host_sex_locationA[0]
        host_location = host_sex_locationA[1].strip()
    except:
        host_sex_locationA = host_sex_location[1].split('\xa0')
        host_sex_locationA = host_sex_locationA[1].split('/')
        host_sex = host_sex_locationA[0]
        host_location = host_sex_locationA[1].strip()
    time.sleep(random.randint(0, 2))
    # print('微博信息:','url:', hosturl, '性别:',host_sex, '地区：',host_location,'微博数:', hostcount, '关注数:',hostfollow,'粉丝数:', hostfans)
    return host_sex, host_location, hostcount, hostfollow, hostfans


if __name__ == '__main__':
    topic = '#郑州暴雨#'
    url = baseUrl.format(quote(topic))
    print(url)
    writer.writerow(['类别', '用户名', '用户链接', '性别', '地区', '微博数', '关注数', '粉丝数', '评论内容', '评论时间', '点赞次数'])
    getTopic(url)  # 去话题页获取微博
