import random

import pandas as pd
import xlwt
import requests
from bs4 import BeautifulSoup

headers = {
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 Edg/96.0.1054.53',
    "cookie":'STATSESSID=kfu5dvtns5ndfd1o7nrksjs6i5; statistaContentView=211540452761b9ce34b9d1a8853497911; _ga=GA1.2.279181788.1639566901; _gid=GA1.2.1757894525.1639566901; OptanonAlertBoxClosed=2021-12-15T11:16:12.539Z; localeDefault=xx; regionDefault=1; _dc_gtm_UA-76064938-1=1; OptanonConsent=isGpcEnabled=0&datestamp=Wed+Dec+15+2021+19%3A23%3A05+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=6.23.0&isIABGlobal=false&consentId=bf20ec5a-70cf-40ac-937a-837674a1658b&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&hosts=H14%3A1%2Crwn%3A1%2CH16%3A1%2Cwna%3A1%2CH18%3A1%2Cieo%3A1%2CH13%3A1%2Cthl%3A1%2CH7%3A1%2CH21%3A1%2CH1%3A1%2CH22%3A1%2Cbsh%3A1%2Chdp%3A1%2CH2%3A1%2CH26%3A1%2CH3%3A1%2CH4%3A1%2Ctlv%3A1%2CH6%3A1%2CH11%3A1%2CH25%3A1%2Cbsr%3A1%2Chkw%3A1%2CH8%3A1&geolocation=%3B&AwaitingReconsent=false',
    "referer":'https://www.statista.com/search/?q=Artificial+Intelligence&qKat=newSearchFilter&sortMethod=idrelevance&isRegionPref=1&statistics-group=1&statistics=1&forecasts=1&infos=1&topics=1&studies-reports=1&groupD=1&dossiers=1&dossiersplus=1&groupA=1&branchreports=1&countryreports=1&cityreports=1&ecommercedbreports=1&xmo=1&groupB=1&companyreports=1&brandreports=1&toplists=1&surveys=1&groupC=1&expert-tools=1&cmo=1&mmo=1&co=1&tmo=1&amo=1&io=1&hmo=1&dmo=1&accuracy=and&isoregion=0&isocountrySearch=&category=0&interval=0&archive=1'
}


def getInfo(url):
    print(url)
    res = requests.get(url, headers=headers).content.decode('utf-8')
    soup = BeautifulSoup(res, "lxml")
    # 标题
    title = soup.select("title")[0].string
    # 日期
    if soup.select(".content__author--date"):
        date = soup.select(".content__author--date")[0].string
    else:
        date = ''
    if soup.select(".article.readingAid__text.responsiveText.responsiveText--underlinedLinks.margin-right-20.margin-right-s-0"):
        content = soup.select(".article.readingAid__text.responsiveText.responsiveText--underlinedLinks.margin-right-20.margin-right-s-0")[0].contents[0]
    else:
        content = ''
    print(content)
    info =[title,date,content]
    # return [title,date,content]
    df = pd.read_csv('数据.csv', encoding='utf-8')
    df.loc[len(df)] = info  # 其中loc[]中需要加入的是插入地方dataframe的索引，默认是整数型
    df.columns = ['标题', '时间', '内容']
    df.to_csv('数据.csv', index=False, encoding='utf_8_sig')

def getAllUrl():
    for i in range(1,31):
        url = 'https://www.statista.com/search/?q=Artificial%20Intelligence&qKat=newSearchFilter&sortMethod=idrelevance&isRegionPref=1&statistics-group=1&statistics=1&forecasts=1&infos=1&topics=1&studies-reports=1&groupD=1&dossiers=1&dossiersplus=1&groupA=1&branchreports=1&countryreports=1&cityreports=1&ecommercedbreports=1&xmo=1&groupB=1&companyreports=1&brandreports=1&toplists=1&surveys=1&groupC=1&expert-tools=1&cmo=1&mmo=1&co=1&tmo=1&amo=1&io=1&hmo=1&dmo=1&accuracy=and&isoregion=0&isocountrySearch=&category=0&interval=0&archive=1&language=0&p={}'.format(i)
        res = requests.get(url, headers=headers).content.decode('utf-8')
        print(len(res))
        soup = BeautifulSoup(res, "lxml")
        urlList = soup.select(".list__itemWrap.text--linkReset.padding-vertical-15")
        for k in urlList:
            singleUrl = 'https://www.statista.com' + k['href']
            getInfo(singleUrl)


if __name__ == '__main__':
    getAllUrl()