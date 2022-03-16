import json
import random
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.30'
}


def createPhone():
    prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139",
               "147", "150", "151", "152", "153", "155", "156", "157", "158", "159",
               "186", "187", "188", "189", "172", "176", "185"]
    four = "".join(random.choice("0123456789") for i in range(4))
    phone = random.choice(prelist) + four + four
    return phone


def sendCode(number):
    url = 'https://www.aliboxx.com/sunlight/client/anno/sendMobileVerifyCode'
    data = {"type": 0, "mobile": number, "GR": "86"}
    res = requests.post(url, json=data).content.decode('utf-8')
    data = json.loads(res)['body']['status']
    with open('记录.txt', 'a+', encoding='utf-8') as f:
        f.write(number + data + '\n')  # 添加‘\n’用于换行
        f.close()  # 关闭文件
    print(data)


if __name__ == '__main__':
    for i in range(0, 1):
        number = createPhone()
        sendCode(number)
