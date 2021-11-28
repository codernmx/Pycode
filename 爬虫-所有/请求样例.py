import random
import xlwt
import requests
from bs4 import BeautifulSoup

url = 'https://zhidao.baidu.com'
headers = {
	# "Cookie": "JSESSIONID=99c927fc-931c-4cb9-b80a-f79772d456dc; route=4b4bdd0e2cdff4f8f9f520f338860b7c; MEIQIA_TRACK_ID=1zkbhabvXkonMQVawLKrEDgstAh; MEIQIA_VISIT_ID=1zkgactIYuF2xpPtHQsqUQYL9ek",
	# "Content-Type": "application/x-www-form-urlencoded"
}
header = {'User-agent': 'Googlebot'}
res = requests.get(url, headers=header).content.decode('GB2312')
soup = BeautifulSoup(res, "lxml")
name = soup.select(".name")
print(res)
