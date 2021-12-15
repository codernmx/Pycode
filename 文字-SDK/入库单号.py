import math
import os
import time

import pandas as pd

from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '25216043'
API_KEY = ''
SECRET_KEY = 'oSUBrw1EG98n9x8AjpW9CEe1QXYWPul7'
dir = r'D:\PycharmCode\pycode\文字-SDK\img'  # 设置工作路径

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
    pdf_file = get_file_content(file_name)
    options = {}
    options["detect_direction"] = "true"
    options["probability"] = "true"
    wordList = client.basicAccurate(pdf_file, options)
    # print(wordList)
    for i in wordList['words_result']:
        if ('2101' in i['words']):
            print(i['words'])
            cutStr = i['words'].split('：')
            finalStr = cutStr[len(cutStr) - 1]
            print(finalStr,'------------------------------')
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
    df.columns = ['图片名称', '单号']
    fileName = time.time()
    fileName = math.floor(fileName * 1000)
    df.to_csv(str(fileName) + '.csv', encoding='utf_8_sig')
