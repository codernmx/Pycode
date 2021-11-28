# -*- coding:utf-8 -*-
import re
import requests


def dowmloadPic(html, keyword):
    pic_url = re.findall('"objURL":"(.*?)",', html, re.S)
    i = 1
    # print('找到关键词:' + keyword + '的图片，现在开始下载图片...')
    # print(pic_url)
    for each in pic_url:
        print(each)
        # print('正在下载第' + str(i) + '张图片，图片地址:' + str(each))
        try:
            pic = requests.get(each, timeout=100)
        except requests.exceptions.ConnectionError:
            # print('【错误】当前图片无法下载')
            continue

        dir = 'img/' + keyword + '_' + str(i) + '.jpg'
        fp = open(dir, 'wb')
        fp.write(pic.content)
        fp.close()
        i += 1
        if(i>10):
            break


word = '美女'

url = 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1637989892047_R&pv=&ic=&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&dyTabStr=MCw0LDEsNiw1LDMsNyw4LDIsOQ%3D%3D&ie=utf-8&sid=&word='+word
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34',
    "Cookie":'BIDUPSID=2598DDF6662E9C9A8F5AF3168D8D9724; PSTM=1634563444; BAIDUID=28BACA22D10FA15496D151F5C1345C72:FG=1; indexPageSugList=%5B%22OCR%22%5D; __yjs_duid=1_826744e86e18174e94ac35902be11cd01635682478057; BDUSS=TNidzRmci1ud0t2eFAxbmV6RG1tSXFiaWNPQW5ZT3Z-VXVrOXF2Zlc3LTQ0OFZoRUFBQUFBJCQAAAAAAAAAAAEAAACfrLp~QW1tYWx5ZWFyAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALhWnmG4Vp5hR; BDUSS_BFESS=TNidzRmci1ud0t2eFAxbmV6RG1tSXFiaWNPQW5ZT3Z-VXVrOXF2Zlc3LTQ0OFZoRUFBQUFBJCQAAAAAAAAAAAEAAACfrLp~QW1tYWx5ZWFyAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALhWnmG4Vp5hR; BAIDUID_BFESS=52C0097566AB4223AF32C8F250D6A3D4:FG=1; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm; userFrom=null; firstShowTip=1; ab_sr=1.0.1_YzNlNmM0MDQ5ZGMwNGVjNDRkNjlhZGU5MmNhOGY3NzFiY2UwZmVkZjMzMGExYzZjNjYxMmRiMzU1OWFkMmFiNTQwZWFiZTliOWNlMGYzYjk4Yzc5ZjI1MmNhOGE1OGQwMTM2YmNiYmU5MjhjN2VkNWJiMDgzYjZjM2ZlNDA1NzM4MTY0ZGQwZGJmMDM5ZTJlMWE4ZTE0NDZiYWIyNTkxMGMxNTMxNGIyNTk1MDAwZWQxZmI1OTA3NjlmZDU5MGJk',
}

response = requests.get(url, headers=headers).content.decode('utf-8')
dowmloadPic(response, word)