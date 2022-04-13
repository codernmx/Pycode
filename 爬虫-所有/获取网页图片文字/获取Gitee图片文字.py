# _*_ coding: utf-8 _*_
import requests
from bs4 import BeautifulSoup
url = 'https://gitee.com/'
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46'
}
def download_img(img_url):  # 下载图片
    r = requests.get(img_url, headers=headers, stream=True)
    if r.status_code == 200:
        img_name = img_url.split('/').pop()[-12:]  # 截取图片文件名
        try:
            with open('img/' + img_name, 'wb') as f:
                f.write(r.content)
            print('保存成功~~', img_name)
            return True
        except:
            print('保存失败~~', img_name)
def getImgAndWord():  # 获取文字
    res = requests.get(url, headers=headers).content.decode('utf-8')
    soup = BeautifulSoup(res, "lxml")
    img = soup.select("img")
    for i in img:
        if i['src'][0:1] == 'h':
            download_img(i['src'])
    # 拿到网页内容
    [script.extract() for script in soup.findAll('script')]
    [style.extract() for style in soup.findAll('style')]
    word = soup.get_text()
    word = word.replace('\n\n', '')  # 去除两次连着换行
    word = word.replace('/', '')  # 去除/
    with open('gitee文字.txt', 'w', encoding='utf-8') as f:  # 写入文件
        f.write(word + '\n')  # 添加‘\n’用于换行
        f.close()  # 关闭文件
        print('存储网站文字成功~~')
if __name__ == '__main__':
    getImgAndWord()
