import pandas as pd



path = 'E:\\PyCharmCode\\文档-学习\\爬虫-所有\\香港支行\\index.html'
htmlfile = open(path, 'r', encoding='utf-8')
htmlhandle = htmlfile.read()
from bs4 import BeautifulSoup

bigSoup = BeautifulSoup(htmlhandle, 'lxml')
name = bigSoup.select("item")


def reStr(str):
    if str:
        strNew = str.replace('   ', '')
        strNew = strNew.replace('\n', '')
        return strNew
    else:
        return str

allInfo = []
for i in name:
    soup = BeautifulSoup(str(i), 'lxml')

    name = soup.select("item > Name")[0].string
    # 维度
    Latitude = soup.select("item > Latitude")[0].string.replace(' ', '')
    # 经度
    Longitude = soup.select("item > Longitude")[0].string.replace(' ', '')
    # 營業時間  营业时间
    if soup.select("Branch > Opening > Mon2Fri"):
        Mon2Fri = soup.select("Branch > Opening > Mon2Fri")[0].string
        Mon2Fri = '星期一至星期五:' + reStr(Mon2Fri)
    else:
        Mon2Fri = ''

    if soup.select("Branch > Opening > SAT"):
        SAT = soup.select("Branch > Opening > SAT")[0].string
        SAT = '星期六:' + reStr(SAT)
    else:
        SAT = ''
    if soup.select("Branch > Opening > SUNHOLIDAY"):
        SUNHOLIDAY = soup.select("Branch > Opening > SUNHOLIDAY")[0].string
        SUNHOLIDAY = '星期日和公眾假期:' + reStr(SUNHOLIDAY)
    else:
        SUNHOLIDAY = ''
    # 电话
    if soup.select("Branch > Personal > Phone"):
        Phone = soup.select("Branch > Personal > Phone")[0].string
        Phone = reStr(Phone)
    else:
        Phone =''
    # 传真
    if soup.select("Branch > Personal > Fax"):
        Fax = soup.select("Branch > Personal > Fax")[0].string
        Fax = reStr(Fax)
    else:
        Fax =''
    # 地址
    if soup.select("atm > Address"):
        Address = soup.select("atm > Address")[0].string
        Address = reStr(Address)
    elif soup.select("Corporate > Address"):
        Address = soup.select("Corporate > Address")[0].string
        Address = reStr(Address)
    elif soup.select("Personal > Address"):
        Address = soup.select("Personal > Address")[0].string
        Address = reStr(Address)
    else:
        Address =''
    Services = soup.select("Branch > Personal > Services > Service")
    Service = ''
    for i in Services:
        Service += reStr(i.string)
    print(Service)
    if 'ATM_CENTRE' in str(Service):
        Atm  = '有'
    else:
        Atm = '没有'
    print(Atm)
    if 'ATM_RMB' in str(Service):
        gui = '有'
    else:
        gui = '没有'
    allInfo.append([name,Latitude,Longitude,Mon2Fri,SAT,SUNHOLIDAY,Phone,Fax,Address,Atm,gui])
# if __name__ == '__main__':

df = pd.DataFrame(allInfo)
df.columns = ['分行名称', '纬度', '经度', '星期一至星期五', '星期六', '星期日和公眾假期', '电话', '传真','地址','是否有ATM','是否有柜台']
df.to_csv('data3.csv', encoding='utf_8_sig')