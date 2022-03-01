import random
import xlwt
import requests
from bs4 import BeautifulSoup

url = 'https://www.bilibili.com/video/BV13S4y1f78X?share_source=copy_web'
headers = {
}
res = requests.get(url, headers=headers).content.decode('utf-8')
# soup = BeautifulSoup(res, "lxml")
print(res)
