import re
import requests
count = 0
num = input("页面小于等于2,页面=：")
url1 = f"https://www.dytt8.net/html/gndy/dyzz/list_23_{num}.html"
url2 = "https://www.dytt8.net/html/gndy/dyzz"
resp = requests.get(url=url1,verify=False)
resp.encoding = 'gb2312'
#print(resp.text)
obj1 = re.compile(r'<a href="/html/gndy/dyzz(?P<子链接>.*?)" class="ulink">',re.S)
obj2 = re.compile(r'《(?P<电影名>.*?)》.*?<a target="_blank" href="'
                  r'(?P<迅雷下载链接>.*?)=%',re.S)#页面是1-2
obj4 = re.compile(r'《(?P<电影名>.*?)》.*?'
                  r'</font></font></strong> <br /><br /><br /><a href="'
                  r'(?P<迅雷下载链接>.*?)=%',re.S)#页面是4-56
obj3 = re.compile(r'《(?P<电影名>.*?)》.*?<div><a href="'
                  r'(?P<迅雷下载链接>.*?)=%',re.S)#页面是3
result = obj1.finditer(resp.text)
child_href_list = []
for it in result:
    child_href = it.group("子链接")
    #print(child_href.group("子链接"))
    url3 = url2+child_href
    #print(url3)
    child_href_list.append(url3)
    #print(child_href_list)

for href in child_href_list:
    resp2 = requests.get(href,verify=False)
    resp2.encoding = 'gb2312'
    #print(resp2.text)
    #break
    number = int(num)
    if number >=4:
        obj = obj4
    elif number == 3:
        obj = obj3
    else :
        obj = obj2
    result2 = obj.search(resp2.text)
    count = count+1
    print(count)
    print(result2.group("电影名"))
    print(result2.group("迅雷下载链接"))
#close()