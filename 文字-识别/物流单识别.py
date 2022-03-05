import math
import os
import time

import pandas as pd

from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '25485'
API_KEY = 'n6LGp3gxzR'
SECRET_KEY = 'EH9nDoqpzgik'
dir = "D:\\PycharmCode\\pycode\\文字-SDK-包括PDF转图片\\img"  # 设置工作路径

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


def getAllFile():
    allPath = []
    for root, dirs, files in os.walk(dir):
        for file in files:
            singlePath = os.path.join(root, file)
            allPath.append(singlePath)
    # 打印文件名
    return allPath


def getNumber(file_name):
    image = get_file_content(file_name)
    options = {}
    options["detect_direction"] = "true"
    options["probability"] = "true"
    wordList = client.basicAccurate(image, options)['words_result']
    for i in wordList:
        if ('CAE' in i['words']):
            cutStr = i['words'].split('：')
            finalStr = cutStr[len(cutStr) - 1]
            print(finalStr)
            return finalStr


if __name__ == '__main__':
    # years = "2001"
    allPath = getAllFile()
    print(len(allPath), '总文件个数')
    allInfo = []
    for i in allPath:
        print(i)
        number = getNumber(i)
        allInfo.append([i, number])
        print('-------------------------------------------------->>>>>>>>', number)
    df = pd.DataFrame(allInfo)
    df.columns = ['图片名称', '运输单号']
    fileName = time.time()
    fileName = math.floor(fileName * 1000)
    df.to_csv(str(fileName) + '.csv', encoding='utf_8_sig')
