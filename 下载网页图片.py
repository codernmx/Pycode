import os

import pymysql
import requests


def download_img(img_url, savePath):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }
    try:
        r = requests.get(img_url, headers=headers, stream=True)
        if r.status_code == 200:
            img_name = savePath + '/' + img_url.split('/').pop()[-12:]  # 截取图片文件名
            print(img_name)
            with open(img_name, 'wb') as f:
                f.write(r.content)
    except:
        print('保存报错--------------------------------------------------------->',img_url)


path = 'idcard_img/'

db = pymysql.connect(host="127.0.0.1", user="root", password="137928", database="PURINE", port=3306)
cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
sql = f"select NAME,IDENTITY,FILE_IDENTITY_FRONT,FILE_IDENTITY_BACK,FILE_SELF,FILE_SIGN from USER WHERE IDENTITY !='' AND FILE_IDENTITY_FRONT !='' ORDER BY CREATE_TIME DESC"
# sql = f"select * from USER WHERE ID = 18"
cursor.execute(sql)
res = cursor.fetchall()

for i in res:
    print(i)
    fileName = i['NAME'] + '-' + i['IDENTITY']
    isExists = os.path.exists(path + fileName)
    if not isExists:
        # 如果不存在则创建目录
        os.makedirs(path + fileName)
        url = 'https://purine.spiritlong.com' + i['FILE_IDENTITY_FRONT']
        download_img(url, path + fileName)
        if i['FILE_IDENTITY_BACK'] is not None:
            url = 'https://purine.spiritlong.com' + i['FILE_IDENTITY_BACK']
            download_img(url, path + fileName)
        if i['FILE_SIGN'] is not None:
            url = 'https://purine.spiritlong.com' + i['FILE_SIGN']
            download_img(url, path + fileName)
        if i['FILE_SELF'] is not None:
            url = 'https://purine.spiritlong.com' + i['FILE_SELF']
            download_img(url, path + fileName)
    else:
        print('已经存过了','--------------------------------------------------->>>>>>',i['NAME'])
