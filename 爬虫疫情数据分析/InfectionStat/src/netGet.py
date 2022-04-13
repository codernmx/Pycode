#! /usr/bin/python3
# coding = UTF-8

import requests
import bs4
from parseData import ParseTool

path = "https://3g.dxy.cn/newh5/view/pneumonia?from=groupmessage&isappinstalled=0"

class NetGet:
    def __init__(self):
        pass

    @staticmethod
    def getHtml():
        rq = requests.get(url=path)
        rq.encoding = 'utf-8'
        bs = bs4.BeautifulSoup(rq.text, 'html5lib')
        scrips = bs.find_all('script')
        parsetool = ParseTool()
        for scrip in scrips:
            sc = scrip
            if "id" in sc.attrs:
                if sc.attrs['id'] == 'getTimelineService': # 根据时间线抓取的要点新闻
                    str = sc.get_text()
                    start = str.find('[')
                    end = str.rfind(']')
                    ob_json_str = str[start: end + 1]
                    parsetool.parse_and_save(ob_json_str, sc.attrs['id'])
                elif sc.attrs['id'] == 'getListByCountryTypeService1': # 根据省级单位抓取指标数据
                    str = sc.get_text()
                    start = str.find('[')
                    end = str.rfind(']')
                    ob_json_str = str[start: end + 1]
                    parsetool.parse_and_save(ob_json_str, sc.attrs['id'])
                elif sc.attrs['id'] == 'getAreaStat': #　根据市级单位抓取数据指标 数据下钻过程
                    str = sc.get_text()
                    start = str.find('[')
                    end = str.rfind(']')
                    ob_json_str = str[start: end + 1]
                    parsetool.parse_and_save(ob_json_str, sc.attrs['id'])
                else:
                    pass
        #print(scrips[9])
NetGet.getHtml()