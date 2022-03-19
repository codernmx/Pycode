
import json,random,time,requests,xlwt
import pandas as pd
from bs4 import BeautifulSoup


headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43',
    "Cookie": '_iuqxldmzr_=32; _ntes_nnid=baa34174ed0e3f1c644a0fb0a8b91f41,1645843443171; _ntes_nuid=baa34174ed0e3f1c644a0fb0a8b91f41; NMTID=00OGzpPjzX3cE5abkY7t6x7AlBlvCYAAAF_M-n88w; WNMCID=xukhlt.1645843443736.01.0; WEVNSM=1.0.0; WM_NI=MWLZx03p6QR04tsX55r%2FaGU84gnkBQsO6BC7vHs2lAuHlshAMMzHdEr8uDVxw92t%2B%2BEMLDj3vMZUQ%2BChmI%2FgLyQHWNRKh2KCElgxt0O7horxOUSVIr%2BO28cuBPjG0FvnMnQ%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee98c64b81ee82a4f45d92ac8ba2d44a838f8aaef57bacecafd8dc6192869e94ed2af0fea7c3b92a8f8984bbfb3cf1b0fab2d13cf8acbdb9b83fb2f1afa8d834f8b9a28cc15bb191faa3c23db698bdd3ef4bb798a494eb4b8f93b6a9e74fb2e8bba5d574b5e7fe95aa21879384a5e939b69396b6d42181b8a3aaae6d90a79fa9d6469295a8d3ca4987b4a999f73c8de9a890f1748d8b9db7cc7ae991fed9e27f8290a6a8b34eb6b2838fd437e2a3; WM_TID=Xv2awzG5SEhARQFQQUc7rloO%2BJ1AMQsm; JSESSIONID-WYYY=H0AWianDB0wb9IBSbo8tKo%2FnpPGktcClhobRgVdVFOwT7KyunTefvTcTvlzWJsi6STGtTRhDB6qpIhEwX9sXeUkb0iUv9pCvAdKz%2F40JGJwbJuUXFTJPgV%2B6u7B%2B5XsccavHNpiHYJKb%2BQ13SBYuFS1IGu%5CsJVjbXVibSZVoFS%2BcPoaK%3A1645885834882',
    'referer': 'https://music.163.com/',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "Windows",
    'sec-fetch-dest': 'iframe',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'upgrade-insecure-requests': '1',
}
baseUrl = 'http://localhost:3000/'
allInfo = []
res = requests.get(baseUrl + 'playlist/track/all?id=3778678&limit=200&offset=1').content.decode('utf-8')
data = json.loads(res)['songs']
print(len(data))
for i in data:
    print(i['id'], i['name'], i['ar'][0]['name'], i['al']['picUrl'])
    id = i['id']  # 歌曲id
    songName = i['name']  # 歌曲名
    creater = i['ar'][0]['name']  # 作者
    pic = i['al']['picUrl']  # 图片信息

    # 遍历 评论信息
    # for k in range(1, 2):
    for k in range(1, 5):
        commentUrl = baseUrl + 'comment/music?id={}&limit=50&offset={}'.format(id, k)
        print(commentUrl)
        commRes = requests.get(commentUrl).content.decode('utf-8')  # 请求接口
        commResData = json.loads(commRes)['comments']
        for l in commResData:
            nickname = l['user']['nickname']  #评论昵称
            userId = l['user']['userId']  #用户id
            avatarUrl = l['user']['avatarUrl']   #评论头像
            content = l['content']   #评论内容
            timeStr = l['timeStr']   #评论时间
            print(nickname,avatarUrl,content,timeStr,'++++++')

            #去请求 用户性别和 地区
            # time.sleep(random.randint(1, 5)) #延时
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
            itemInfo = [id,songName,creater,pic,nickname,area,sex,avatarUrl,content,timeStr]
            df = pd.read_csv('网易云.csv', encoding='utf-8',index_col=0)
            print(itemInfo)
            print(len(itemInfo))
            df.loc[len(df)] = itemInfo  # 其中loc[]中需要加入的是插入地方dataframe的索引，默认是整数型
            df.columns = ['歌曲ID', '名称', '作者', '照片', '评论昵称', '区域', '性别', '评论头像', '评论内容', '评论时间']
            df.to_csv('网易云.csv', encoding='utf_8_sig')


