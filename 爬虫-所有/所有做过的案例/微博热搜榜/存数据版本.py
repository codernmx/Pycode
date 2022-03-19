import requests
from bs4 import BeautifulSoup
import pandas as pd
import bs4

url = "https://s.weibo.com/top/summary?cate=realtimehot"


def getHTMLText(url):
    try:
        kv = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 Edg/96.0.1054.53",
            "Cookie": 'UOR=,,login.sina.com.cn; ALF=1666445729; SCF=AscEHVE2sTV05zTwYj5M7tduM7Zz3ktqPi21c2dTBB0sGFGcFIldixokcQ1yN8xFwVW-ywKnUt3rugqpWgzVXsE.; SINAGLOBAL=7267933806159.166.1634959444829; SUB=_2AkMW3d0wf8NxqwJRmPERzW_nbIx0yQ7EieKggSzrJRMxHRl-yT9jqhdftRB6PV3z3z21fp5a3CkZMXy5gZcyj15_nia0; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W56DO1wnAXX89yZnIENST5-; _s_tentry=-; Apache=6131946571247.373.1639292770571; ULV=1639292770592:2:1:1:6131946571247.373.1639292770571:1634959444907'
        }
        r = requests.get(url, headers=kv, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "error"


html = getHTMLText(url)
# print(html)
soup = BeautifulSoup(html, 'html.parser')
sou = soup.find_all("td", class_='td-02')
print(len(sou))
allInfo = []
for x in sou:
    print(x.a.string)
    allInfo.append(x.a.string)
df = pd.DataFrame(allInfo)
df.columns = ['热搜标题']
df.to_csv('data.csv', encoding='utf_8_sig')

