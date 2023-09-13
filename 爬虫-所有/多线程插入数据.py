# !/usr/bin/python3
import pymysql
import json
import random
import threading
import time
import requests
from id_validator import validator

urls = []


def multi_thread():
    threads = []
    for i in urls:
        threads.append(threading.Thread(target=saveItem, args=(i,)))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


def saveItem(data):
    # 保证每个线程有连接
    db = pymysql.connect(host='127.0.0.1', user='root', password='root', database='xxxx')
    cursor = db.cursor()
    try:
        memberPhone = data['memberPhone']
        memberIdCard = data['memberIdCard']
        memberName = data['memberName']
        orderStatus = data['orderStatus']
        createTime = data['createTime']
        id = data['id']
        valid = validator.is_valid(memberIdCard)
        if valid:
            parsed_info = validator.get_info(memberIdCard)
            address = parsed_info['address']
            birthday = parsed_info['birthday_code']
            zodiac = parsed_info['chinese_zodiac']
            age = parsed_info['age']
            if parsed_info['sex'] == 0:
                sex = '女'
            else:
                sex = '男'
            sql = """INSERT INTO s_order_c (id, memberPhone, memberIdCard, memberName,orderStatus,createTime,address,birthday,zodiac,age,sex) VALUES (%s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s)"""
            data = (id, memberPhone, memberIdCard, memberName, orderStatus, createTime,address,birthday,zodiac,age,sex)
            cursor.execute(sql, data)
            db.commit()
            print(id, '插入成功----------------------------------------------------------------》')
            db.close()
        else:
            print("无效的身份证号码", memberIdCard)
    except Exception as error:
        print(error, '插入数据错误信息----------------------------------------------------------------》')
        pass


# 获取每一页的数据
def getItemInfo(page):
    print('开始获取第{}页的数据--------------------------------------------》'.format(page))
    data = {
        "pageNo": page, "pageSize": 10
    }
    try:
        url = 'http://XXXXXXXXXX.com'
        headers = {
            "Content-Type": "application/json",
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
        }
        response = requests.post(url, headers=headers, json=data,timeout=5)
        mv_list = json.loads(response.content)['data']['data']
        print('获取到的数据长度----------------------------》',len(mv_list))
        for i in mv_list:
            urls.append(i)
    except Exception as error:
        print(error)


if __name__ == "__main__":
    start = time.time()
    for i in range(1, 10): #获取1-10页数据
        getItemInfo(i)
        multi_thread()
        # sleep_time = random.randint(1, 5)
        # time.sleep(sleep_time) # 执行随机睡眠
        urls = []
        end = time.time()
    print("总共耗时:", end - start, "秒")
