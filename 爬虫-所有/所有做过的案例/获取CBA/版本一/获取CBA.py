import pandas as pd
import xlwt
import requests
from bs4 import BeautifulSoup
url = 'http://cbadata.sports.sohu.com/teams/team_sch/NTe003'
headers = {
    "Cookie": "IPLOC=CN5000; SUV=211206094136CEYA; gidinf=x099980109ee145e3691f94740000bca0d8b9fa5c47c; t=1638770110650",
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43'
}
def getDetailInfo(url):
    print(url)
    res = requests.get(url, headers=headers).content.decode('utf-8') #对每一个网页发请求
    soup = BeautifulSoup(res, "lxml")
    allInfo = soup.select(".area > .cutE > div > table > tr")[1:]   #排除掉第一个空值  （表头）
    singleInfo = []  #存每一个球队的所有比赛信息
    for i in allInfo:
        title = soup.select("title")[0].string.split(':')[-1]  #<title>CBA球队介绍:八一</title> 分割取冒号之后的部分
        time = i.contents[1].string  # 时间
        zhu = i.contents[3].string  # 主队
        score = i.contents[5].string  # 比分情况
        score = score.replace(' ','')
        score = score.replace('\n','')
        score = score.replace('\t','')
        scoreList = score.split(':')
        # print(score.split(':'))
        ke = i.contents[7].string  # 客队
        singleInfo.append([title,time,zhu,scoreList[0],ke,scoreList[1],score])
    return singleInfo
res = requests.get(url, headers=headers).content.decode('utf-8')
soup = BeautifulSoup(res, "lxml")
allList = soup.select(".area > .cutG > h2 > span > select > option")  #拿到所有球队的链接
allInfo = []
for i in allList:
    if i['value'] != '0' and i['value']:
        singleUrl = 'http://cbadata.sports.sohu.com/teams/team_sch/' + str(i['value']) #拼接真实url
        singleInfo = getDetailInfo(singleUrl) #传入函数
        allInfo.extend(singleInfo)
df = pd.DataFrame(allInfo)  #转为dataframe
df.columns = ['球队名', '比赛时间', '主队', '得分', '客队','得分','比分情况'] #设置表头
df.to_csv('CBA.csv', encoding='utf_8_sig') #存入csv
