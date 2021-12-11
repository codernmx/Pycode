
import xlwt
import requests
from bs4 import BeautifulSoup
path = 'E:/PycharmCode/py-charm-code/utils/img/'


# 下载图片
def download_img(img_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }
    r = requests.get(img_url, headers=headers, stream=True)
    if r.status_code == 200:
        img_name = img_url.split('/').pop()[-12:]  # 截取图片文件名
        print(img_name)
        with open(path + img_name, 'wb') as f:
            f.write(r.content)
        return True


def getImgUrl(url):
    headers_all = {
        "Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        "Accept-Encoding": 'gzip, deflate',
        "Accept-Language": 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        # "Cache-Control": 'max-age=0',
        "Connection": 'keep-alive',
        "Cookie": '__yjs_duid=1_1ded8ba9b536c5b42796529239319dd21635240082530; Hm_lvt_14b14198b6e26157b7eba06b390ab763=1635240084,1635302667; xygkqecookieclassrecord=%2C7%2C; Hm_lpvt_14b14198b6e26157b7eba06b390ab763=1635303536',
        "Host": 'www.netbian.com',
        "Referer": 'http://www.netbian.com/meinv/',
        "Upgrade-Insecure-Requests": '1',
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30',
    }
    headers = {
        "Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        "Accept-Encoding": 'gzip, deflate',
        "Accept-Language": 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        # "Cache-Control": 'max-age=0',
        "Connection": 'keep-alive',
        "Cookie": '__yjs_duid=1_1ded8ba9b536c5b42796529239319dd21635240082530; Hm_lvt_14b14198b6e26157b7eba06b390ab763=1635240084,1635302667; xygkqecookieclassrecord=%2C7%2C; Hm_lpvt_14b14198b6e26157b7eba06b390ab763=1635303536',
        "Host": 'www.netbian.com',
        "Referer": 'http://www.netbian.com/meinv/',
        "Upgrade-Insecure-Requests": '1',
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30',
    }
    # url = 'http://www.netbian.com/meinv/'
    response = requests.get(url, headers=headers).content
    # print(response, '========')
    soup = BeautifulSoup(response, "lxml")
    # 图片列表
    imgUrlList = soup.select('.list > ul > li > a > img')
    for i in imgUrlList:
        imgUrl = i['src']
        ret = download_img(imgUrl)
        if not ret:
            print(imgUrl + "下载失败")
        print(imgUrl + "---------下载成功")


if __name__ == '__main__':
    # 下载要的图片
    for i in range(3, 30):
        imgUrl = 'http://www.netbian.com/meinv/index_' + str(i) + '.htm'
        getImgUrl(imgUrl)
    # img_url = "http://www.py3study.com/Public/images/article/thumb/random/48.jpg"
    # ret = download_img(img_url)
    # if not ret:
    #     print(img_url + "下载失败")
    # print(img_url + "---------下载成功")
