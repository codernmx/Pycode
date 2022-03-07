import random
import xlwt
import requests
from bs4 import BeautifulSoup

url = 'https://zhidao.baidu.com'
headers = {
}
res = requests.get(url, headers=headers).content.decode('GB2312')
soup = BeautifulSoup(res, "lxml")
name = soup.select(".name")
print(res)
