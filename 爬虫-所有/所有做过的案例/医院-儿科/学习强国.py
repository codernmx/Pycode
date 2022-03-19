import requests
import json
from bs4 import BeautifulSoup
def getQuestionInfo():
    url = 'http://m.syiban.com/search/index/init.html?is_wap=1&modelid=1&q=%E4%B8%AD%E5%9B%BD%E5%85%B1%E4%BA%A7%E5%85%9A'
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML, likeGecko) Chrome/80.0.3987.163Safari/537.36"
    }
    response = requests.get(url, headers=headers).content.decode('utf-8')
    web = response
    soup = BeautifulSoup(web, "lxml")
    # list = soup.select(".title_color")[0]["alt"]
    # list = soup.select(".title_color")
    # list = soup.select(".title_color").parent.previous_sibling.get_text()
    list = soup.select("span", {"style": "font-size: 16px; color: #0000FF;"})
    arr = []
    for item in list:
        print(item.get_text())
        arr.append(item.get_text())
    print(json.dumps(arr, ensure_ascii=False))
getQuestionInfo()