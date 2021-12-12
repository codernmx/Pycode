from urllib import parse
from urllib.parse import urlencode
from lxml import etree
from collections import namedtuple
import re
import time
import requests
from bs4 import BeautifulSoup
# import docx
# from docx.shared import RGBColor
# from docx.shared import Inches
# from docx.shared import Pt


def get_page(keywords):
    headers = {
        "Cookie":'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIyisGGMorBhRH; BDUSS_BFESS=dvbFRpdUVPSjktZGV6eG12MWx6OHk0RTNrTjA0OXF3MnI3SzJRTjQzU01MOWhoRUFBQUFBJCQAAAAAAAAAAAEAAACfrLp~QW1tYWx5ZWFyAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIyisGGMorBhRH; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=0485A42B6B9E6A4B56F7CA28DF852708:FG=1; delPer=0; PSINO=6; BCLID=10901066223465143761; BDSFRCVID=3K8OJexroG38ZMOHRCZu-MMBnFWYvd6TDYLtOwXPsp3LGJLVJeC6EG0Pts1-dEu-EHtdogKKKmOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tJID_KDXtCL3H48k-4QEbbQH-UnLq-J922OZ04n-ah02oq04-U7TK-uWqtcuXnJMW20j0h7m3UTdfh76Wh35K5tTQP6rLtbuLK34KKJxbPOYVfotLt50bfDNhUJiBMnLBan7_qvIXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtpChbC_GDjtaejoBeU5eetjK2CntsJOOaCvVEIJOy4oWK441DbrxJtJ7Je7Pbj6zBxn5epvoD-Jc3M04XhO9-hvT-54e2p3FBUQJ8fOcQft20b0yXJQN3foaMDTG2J7jWhvvDq72y5jvQlRX5q79atTMfNTJ-qcH0KQpsIJM5-DWbT8IjHCDt5FDJJPqVbobHJoHjJbGq4bohjn05a39BtQO-DOxonka3Ub1sUJ6bCcYXj80bPRiL6-tQgnk2PbvbMnmqPtRXMJkXhKsXq7t0x-jLTne5fKKXh4VDPnwj4nJyUPUhtnnBT5i3H8HL4nv2JcJbM5m3x6qLTKkQN3T-PKO5bRu_CFhfbo5KRopMtOhq4tehH4eB5v9WDTOQJ7TtKnA8q7S0xbA5DuIXt5X0qbkbDPq-pbwBPbcfUnMKn05XM-pXbjZKxtq3mkjbPbbt66fstKzQf7Mb-4syPRi2xRnWnciKfA-b4ncjRcTehoM3xI8LNj405OTbIFO0KJzJCcjqR8Zj5KBejOP; BCLID_BFESS=10901066223465143761; BDSFRCVID_BFESS=3K8OJexroG38ZMOHRCZu-MMBnFWYvd6TDYLtOwXPsp3LGJLVJeC6EG0Pts1-dEu-EHtdogKKKmOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tJID_KDXtCL3H48k-4QEbbQH-UnLq-J922OZ04n-ah02oq04-U7TK-uWqtcuXnJMW20j0h7m3UTdfh76Wh35K5tTQP6rLtbuLK34KKJxbPOYVfotLt50bfDNhUJiBMnLBan7_qvIXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtpChbC_GDjtaejoBeU5eetjK2CntsJOOaCvVEIJOy4oWK441DbrxJtJ7Je7Pbj6zBxn5epvoD-Jc3M04XhO9-hvT-54e2p3FBUQJ8fOcQft20b0yXJQN3foaMDTG2J7jWhvvDq72y5jvQlRX5q79atTMfNTJ-qcH0KQpsIJM5-DWbT8IjHCDt5FDJJPqVbobHJoHjJbGq4bohjn05a39BtQO-DOxonka3Ub1sUJ6bCcYXj80bPRiL6-tQgnk2PbvbMnmqPtRXMJkXhKsXq7t0x-jLTne5fKKXh4VDPnwj4nJyUPUhtnnBT5i3H8HL4nv2JcJbM5m3x6qLTKkQN3T-PKO5bRu_CFhfbo5KRopMtOhq4tehH4eB5v9WDTOQJ7TtKnA8q7S0xbA5DuIXt5X0qbkbDPq-pbwBPbcfUnMKn05XM-pXbjZKxtq3mkjbPbbt66fstKzQf7Mb-4syPRi2xRnWnciKfA-b4ncjRcTehoM3xI8LNj405OTbIFO0KJzJCcjqR8Zj5KBejOP; ab_sr=1.0.1_YzA5YWI4MTFmMTMwZGM4ZTA3NjhjYWUwMzBkYmIwNDU4ZjBiMzlkZmUwYzZkNmVhYzY1YjAyOWIyNTU3N2QwNGQyMzU5ZWZhNjlhZjg5OWY5NjU2YjQwYzI4OWUzMzA3NjA1ZTY5ZTRmYTQ1Nzk0MDA4ZTA2N2IyOWRjYzI3YTc5Mzk5NThmY2QzNmJlM2ZlYWIzMDQzYmJjYjUxN2ZkOTM3N2EwNTE0OGI0N2E2ZWQxNTc5YWU0YTdiZjQ3ODIx; BD_UPN=12314753; sug=3; sugstore=0; ORIGIN=0; bdime=0; BA_HECTOR=a1802h002k210g2l7p1grc0g50r; BD_HOME=0; H_PS_PSSID=; COOKIE_KEY_INDEX_KAITI=; Hm_lvt_43115ae30293b511088d3cbe41ec099c=1639312352,1639318026; Hm_lpvt_43115ae30293b511088d3cbe41ec099c=1639318026; Hm_lvt_f28578486a5410f35e6fbd0da5361e5f=1639312352,1639318026; Hm_lpvt_f28578486a5410f35e6fbd0da5361e5f=1639318026; BD_CK_SAM=1; BDRCVFR[w2jhEs_Zudc]=mk3SLVN4HKm; BDSVRTM=541',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/95.0.4638.54 Safari/537.36 '

    }
    params = {
        'wd': keywords,
    }
    url = "https://xueshu.baidu.com/s?" + urlencode(params)
    print(url)
    try:
        response = requests.get(url, headers=headers)
        print(len(response.content.decode('utf-8')))
        if response.status_code == 200:
            return response.text.encode('utf-8')
    except requests.ConnectionError:
        return None


def get_urls(text):
    titles = []
    content = []
    authors = []
    urlls = []
    soup = BeautifulSoup(text, 'lxml')
    title_datas = soup.select('.result.sc_default_result.xpath-log')
    print(title_datas)
    author_datas = soup.find_all('div', 'sc_info')
    abstract_datas = soup.find_all('div', 'c_abstract')
    for item in title_datas:
        result = {
            'title': item.get_text(),
            'href': item.get('href')
        }
        titles.append(item.get_text())
        wd = str(parse.urlparse(item.get('href')).query).split('&')[0]
        paperid = wd.split('%')[2][2]
        params = {
            'paperid': paperid,
            'site': 'xueshu_se'
        }
        url = 'https://xueshu.baidu.com/usercenter/paper/show?' + urlencode(params)
        urlls.append(url)
paper = namedtuple('paper', ['title', 'author', 'content', 'download_urls'])

if __name__ == '__main__':
    keywords = str(input("请输入关键词：\n"))
    text = get_page(keywords)
    print(len(text))
    titles = get_urls(text)
    # soup = BeautifulSoup(text,'lxml')
    # soup.prettify
    # print(soup)
