# _*_ coding: utf-8 _*_
import io
import threading
import time
import requests
from bs4 import BeautifulSoup

headers = {
    'Cookie': 'channelid=0; sid=1647436636519488; _ga=GA1.2.442140817.1647436637; _gid=GA1.2.414938708.1647436637; MEIQIA_TRACK_ID=26T9KQafNMSUGTjiCshzKnjNdmm; MEIQIA_VISIT_ID=26T9KQ667Jsh63EJx9w3x3oFPlW; sessionid=04c7e250475d067f920d45e9a8ece869',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39'
}

urls = [
    f"https://www.kuaidaili.com/free/inha/{page}/"
    for page in range(1, 30 + 1)
]


def craw(url):
    res = requests.get(url, headers=headers).content.decode('utf-8')
    soup = BeautifulSoup(res, "lxml")
    trList = soup.select(".table.table-bordered.table-striped >tbody>tr")
    for i in trList:
        uurl = i.contents[1].string + ':' + i.contents[3].string
        # print(uurl)
        try:
            url5 = 'http://httpbin.org/get'
            r = requests.get(url5, proxies={'http': uurl}, timeout=2)
            # print(json.loads(r.text)['origin'])
            print(uurl)
            with io.open('记录.txt', 'a+', encoding='utf-8') as f:
                f.write(uurl + '\n')  # 添加‘\n’用于换行
                f.close()  # 关闭文件

        except:
            print('无效')


def multi_thread():
    print("开始")
    threads = []
    for url in urls:
        threads.append(threading.Thread(target=craw, args=(url,)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("结束")


if __name__ == "__main__":
    start = time.time()
    multi_thread()
    end = time.time()
    print("总共耗时:", end - start, "seconds")
