# _*_ coding: utf-8 _*_
import requests
import re
from datetime import datetime


def cctv(company, page):
    num = (page)

    # 第一步：模拟浏览器，在央视网中输入相应的企业，并得到网页源代码
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'}
    url = 'https://search.cctv.com/search.php?qtext=' + company + '&sort=date&type=web&vtime=&page=' + str(num)
    print('正在获取----------------》》》',url)
    res = requests.get(url, headers=headers, timeout=10).text

    # print(res)
    # 第二步：正则表达式提取文本信息
    p_href = '<span lanmu1=".*?"'
    p_title = 'target="_blank">.*?</a>'
    p_source = '<div class="src-tim">.*?<span class="src">(.*?)</span>'
    p_date = '<div class="src-tim">.*?<span class="tim">(.*?)</span>'
    href = re.findall(p_href, res, re.S)
    title = re.findall(p_title, res, re.S)
    for i in range(20):
        title.remove('target="_blank"></a>')
    source = re.findall(p_source, res, re.S)
    date = re.findall(p_date, res, re.S)

    # 第三步：信息清洗
    for i in range(len(title)):
        title[i] = title[i].strip().replace('target="_blank">', '')
        title[i] = title[i].strip().replace('</a>', '')
        href[i] = href[i].strip().replace('<span lanmu1="', '')
        href[i] = href[i].strip().replace('"', '')
        source[i] = source[i].strip()
        date[i] = date[i].strip()

    # 第四步：自动生成报告
    # time = datetime.now().strftime('%Y-%M-%d')
    # file_path = time
    file1 = open('结果数据' + '.txt', 'a', encoding='utf-8')
    file1.write(company + '数据爬取开始了!' + '\n' + '\n')

    # 第五步:输出爬取信息到数据报告中
    for i in range(len(title)):
        file1.write(str(i + 1) + '.' + title[i] + '(' + date[i] + '-' + source[i] + ')' + '\n')
        file1.write(href[i] + '\n')

    file1.write('-' * 60 + '\n' + '\n')
    file1.close()


# 第六步:依次爬取不同的企业

companys = ['阿里巴巴', '京东', '万科集团', '腾讯', '小米', '新东方']
for company in companys:
    for i in range(10):
        try:
            cctv(company, i + 1)
            print(company + '第' + str(i + 1) + '页信息爬取成功!')
        except:
            print(company + '第' + str(i + 1) + '页信息爬取失败!')
