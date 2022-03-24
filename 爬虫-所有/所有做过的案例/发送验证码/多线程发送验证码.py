import json
import random
import threading
import time
import requests

urls = []

def createPhone():
    prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139",
               "147", "150", "151", "152", "153", "155", "156", "157", "158", "159",
               "186", "187", "188", "189", "172", "176", "185"]
    end = "".join(random.choice("0123456789") for i in range(8))
    phone = random.choice(prelist) + end
    return phone

def craw(number):
    url = 'https://www.aliboxx.com/sunlight/client/anno/sendMobileVerifyCode'
    data = {"type": 0, "mobile": number, "GR": "86"}
    res = requests.post(url, json=data).content.decode('utf-8')
    data = json.loads(res)['body']['status']
    with open('记录.txt', 'a+', encoding='utf-8') as f:
        f.write(number + data + '\n')  # 添加‘\n’用于换行
        f.close()  # 关闭文件
    print(data)

def multi_thread():
    threads = []
    for i in urls:
        threads.append(threading.Thread(target=craw, args=(i,)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    for i in range(0, 1000):
        urls.append(createPhone())
    start = time.time()
    multi_thread()
    end = time.time()
    print("总共耗时:", end - start, "秒")
