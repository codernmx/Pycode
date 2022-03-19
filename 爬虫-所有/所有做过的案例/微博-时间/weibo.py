import xlwt
import requests
from bs4 import BeautifulSoup


def three(a, b, c):
  if a > b:
    if b > c:  # a>b，b>c
      return c
    elif a > c:  # a>b，b<c，a>c
      return b
    else:  # a>b，a<c
      return b
  elif a > c:  # a<b，a>c
    return c
  elif b > c:  # a<b，a<c，b>c
    return a
  else:  # a<b，a<c，b<c
    return a


# 存储到excel
def saveExcel(file_path, all_info):
  f = xlwt.Workbook(encoding='utf-8')
  sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)  # 创建sheet
  info = ['发布者', '时间', '内容']
  for col in range(0, 3):
    sheet1.write(0, col, info[col])
  # 将数据写入第 i 行，第 j 列
  row = 1
  for data in all_info:
    for j in range(len(data)):
      sheet1.write(row, j, data[j])
    row = row + 1
  f.save(file_path)


headers = {
  "Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  "Accept-Encoding": 'gzip, deflate, br',
  "Accept-Language": 'zh-CN,zh;q=0.9',
  "Cache-Control": 'max-age=0',
  "Connection": 'keep-alive',
  "Cookie": 'SUB=_2AkMWLw8Jf8NxqwJRmP4QxGLrZIp-yQ7EieKgc_7SJRMxHRl-yT8XqkBTtRB6Pa8h5kF9Ru3aKkGlYzkf1_ZOBxUoH4X1; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W5e9oTSZFdlb2ojdxqM.-GO; _s_tentry=weibo.com; Apache=7267933806159.166.1634959444829; SINAGLOBAL=7267933806159.166.1634959444829; ULV=1634959444907:1:1:1:7267933806159.166.1634959444829',
  "Host": 's.weibo.com',
  "Referer": 'https://weibo.com/',
  "sec-ch-ua": '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
  "sec-ch-ua-mobile": '?0',
  "Sec-Fetch-Dest": 'document',
  "Sec-Fetch-Mode": 'navigate',
  "Sec-Fetch-Site": 'same-site',
  "Sec-Fetch-User": '?1',
  "Upgrade-Insecure-Requests": '1',
  "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
}
all_info = []
for iii in range(1, 25):
  print(iii)
  url = 'https://s.weibo.com/weibo?q=%E6%97%B6%E9%97%B4%E9%93%B6%E8%A1%8C&page=' + str(
    iii)
  response = requests.get(url, headers=headers).content.decode('utf-8')
  print(response,'////')
  soup = BeautifulSoup(response, "lxml")
  # 时间
  list0 = soup.select('.content .from > a')
  list00 = []
  num0 = 0
  for i in list0:
    num0 += 1
    if (num0 % 2 == 1):
      strd = i.contents[0].string
      strd = strd.replace(' ', '')
      list00.append(strd)
  # 昵称
  list1 = soup.select('.content .info > div .name')
  list11 = []
  num1 = 0
  for i in list1:
    list11.append(i.string)

  # 内容
  list2 = soup.select('.content .txt')
  list22 = []
  for i in list2:
    print(i)
    if (i['node-type'] == 'feed_list_content'):
      strt = ''
      for aaa in i.contents:
        strt += str(aaa.string)
        strt = strt.replace('None', '')
      list22.append(strt)
      print(strt, '+++++++++')
  a = len(list00)
  b = len(list11)
  c = len(list22)
  mini = three(len(list00), len(list11), len(list22))
  print(mini,'--------------------------')
  # if a == b and b == c:
  for item in range(0, mini):
    name = list11[item]
    time = list00[item]
    content = list22[item]
    temp = [name, time, content]
    all_info.append(temp)
  # else:
  #   print(url)
saveExcel("2-50-full-1.xls", all_info)
