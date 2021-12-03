import threading
import time
import requests
from bs4 import BeautifulSoup

urls = [
    f"https://www.cnblogs.com/sitehome/p/{page}"
    for page in range(1, 50 + 1)
]

info = []
def craw(url):
    print("craw url: ", url)
    r = requests.get(url)
    info.append(str(time.time()))
    # return r.text


def multi_thread():
    print("开始")
    threads = []
    for url in urls:
        threads.append(
            threading.Thread(target=craw, args=(url,))
        )

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
    print(info)
