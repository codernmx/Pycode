# @Time : 2022/2/26 19:30
# @Author : VX:Until_Day_Break
# @SoftWare : PyCharm


import requests
from bs4 import BeautifulSoup

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'accept-encoding': 'gzip, deflate, br',
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43',
    "Cookie": '_iuqxldmzr_=32; _ntes_nnid=baa34174ed0e3f1c644a0fb0a8b91f41,1645843443171; _ntes_nuid=baa34174ed0e3f1c644a0fb0a8b91f41; NMTID=00OGzpPjzX3cE5abkY7t6x7AlBlvCYAAAF_M-n88w; WNMCID=xukhlt.1645843443736.01.0; WEVNSM=1.0.0; WM_TID=Xv2awzG5SEhARQFQQUc7rloO%2BJ1AMQsm; JSESSIONID-WYYY=vx22rw5Pufq8DrxxXCQuqZK1Ozf%2FGU7F%2FPUZ4eJfExbmlsVsplCne%5CN8JT5omplBHHHu%5CWUPpEzzxPHyujINsDaXHhOM%2B%2Bq6fajHncB%2B1jc1empd01ct4p4ZoziwJrhj2XNbdK8Tvn7VlknhVyEM8MKhNevSXHyEekiMHt1XKu18X0Az%3A1645926763949; WM_NI=RujBoCdxfbzOrK7jCja6F6MmhoeDSoyoeddjWkpdPNt4VXRopAMcXUjRakHDHdz6hlX1%2Btat0Z69MA2GFDoPjSucVWrSLZb%2B%2B54Yj9Ue9lH8jw6XGjRG8ihY%2BU%2F4JlpYQU4%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee91c733a8eaadb8f63e82ef8fb3c84e979e9aaff825b0e98f95c26eaaeb9bb9e22af0fea7c3b92a92aba6a3ee49a8a8aa83f945b295f98bc262a3ea8ad7d067acb1aba5d265bbb1ab85e76295b5c085d346b8ec9ab9d165b49f8384db5faa8eaf8ccb508cbcb6d7eb689cefe595e480f486fadad04bf2998aa5ee5caa8dbb84d55db28d84bbe121e9ebfcbae93397bbf78dcb34aaa9fab9c6629299f88aeb53e98be1d5c968b4879fb6b737e2a3',
    'referer': 'https://music.163.com/',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "Windows",
    'sec-fetch-dest': 'iframe',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'upgrade-insecure-requests': '1',
}
userId = '1661121970'
userUrl = 'https://music.163.com/#/user/home?id={}'.format(userId)
print(userUrl)
userRes = requests.get(userUrl, headers=headers).content.decode('utf-8')  # 请求接口

soup = BeautifulSoup(userRes, "lxml")

print(soup.select("title")[0].contents[0].string, '------------------------>标题是网易云音乐就是出错了，限制了')
area = ''
if len(soup.select(".inf.s-fc3")) > 0:
    area = soup.select(".inf.s-fc3")[0].contents[1].string  # 地区
    print(area, '地区')
one = soup.select(".icn.u-icn.u-icn-01")
sex = ''
if len(one) > 0:
    sex = '男'
two = soup.select(".icn.u-icn.u-icn-02")
if len(two) > 0:
    sex = '女'
print(area, sex, '------------------------------>区域，性别')
