import csv
import time
import pandas as pd

data = []
abroad_data = []
china = []
abroad = []
overalldata = []
# 读取数据
def read():
    with open('DXYArea.csv', encoding='utf-8') as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            del row[14], row[13], row[6], row[5], row[3], row[1], row[0]
            data.append(row)
    with open('DXYArea.csv', encoding='utf-8') as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            del row[18], row[17], row[16], row[15], row[14], row[13], row[12], row[6], row[5], row[4], row[3], row[1]
            abroad_data.append(row)
    with open('DXYOverall.csv', encoding='utf-8') as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            del row[39], row[38], row[37], row[36], row[35], row[34], row[33],row[32], row[31], row[30],row[29],row[28],row[27], row[26], row[25], row[24], row[23],row[22], row[21], row[20], row[19],row[6],row[5],row[4],row[3],row[2],row[1],row[0]
            overalldata.append(row)

# 合并数据
def merge():
    for i in range(len(data)):
        if i > 0 and data[i][0] == '中国':
            t = data[i][6]
            timeStruct = time.strptime(t, "%Y-%m-%d %H:%M:%S")
            strTime = time.strftime("%m-%d", timeStruct)
            data[i][6] = strTime
            china.append(data[i])
    for i in range(len(abroad_data)):
        if i > 0 and abroad_data[i][1] != '中国' and abroad_data[i][0]!='':
            t = abroad_data[i][6]
            timeStruct = time.strptime(t, "%Y-%m-%d %H:%M:%S")
            strTime = time.strftime("%m-%d", timeStruct)
            abroad_data[i][6] = strTime
            abroad.append(abroad_data[i])
    for i in range(len(overalldata)):
        if i > 0:
            t = overalldata[i][12]
            timeStruct = time.strptime(t, "%Y-%m-%d %H:%M:%S")
            strTime = time.strftime("%m-%d", timeStruct)
            overalldata[i][12] = strTime
# 添加表头
def reverse():
    china.reverse()
    china.insert(0, ['countryName', 'provinceName', 'province_confirmedCount', 'province_suspectedCount',
                     'province_curedCount', 'province_deadCount'
        , 'updateTime', 'cityName', 'city_confirmedCount', 'city_suspectedCount', 'city_curedCount', 'city_deadCount'])


# 写出数据
def write():
    with open('chinaArea_data.csv', 'w', newline='', encoding='utf-8') as f:
        f_csv = csv.writer(f)
        for row in china:
            f_csv.writerow(row)

    df = pd.DataFrame(overalldata[1:])
    df.drop_duplicates(subset=12, keep='first', inplace=True)
    df.to_csv('overall.csv')

    df1 = pd.DataFrame(abroad[1:])
    df1.drop_duplicates(subset=[1,6], keep='first', inplace=True)
    df1.to_csv('abroadArea_data.csv')

read()
merge()
reverse()
write()


