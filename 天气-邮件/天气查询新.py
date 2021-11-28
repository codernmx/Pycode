# import xlwt
import requests
from bs4 import BeautifulSoup

url = 'https://weather.cma.cn/web/text/XN/AGZ.html'
response = requests.get(url).content.decode('utf-8')
soup = BeautifulSoup(response, "lxml")
list = soup.select('.provincetable > table > tr >td > dl > dd > a')
urlList= []
print(len(list))
for item in list:
        itemUrl = 'https://weather.cma.cn' + item['href']
        res = requests.get(itemUrl).content.decode('utf-8')
        itemSoup = BeautifulSoup(res, "lxml")
        itemList = itemSoup.select('.odd > td > a')
        num = 0
        print(len(itemList))
        for ite in itemList:
                num = num +1
                if(num%2==1):
                        print(ite['href'][-5:] + '-----------' + ite.string)
        break

