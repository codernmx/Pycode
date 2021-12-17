
import pandas as pd
import os

# 读取news_data.csv，保存到新建的news_data.txt中
data = pd.read_csv('北京处理之后.csv', encoding='utf-8')
with open('news_data.txt', 'a+', encoding='utf-8') as f:
    for line in data.values:
        # # str(line[0])：csv中第0列；+','+：csv两列之间保存到txt用逗号（，）隔开；'\n'：读取csv每行后在txt中换行
        # f.write((str(line[0]) + ',' + str(line[1]) + ',' + str(line[2]) + str(line[3]) + ','+str(line[4]) + ','+str(line[5]) + ','+str(line[6]) + ','+str(line[7]) + ','+str(line[8]) + ','+str(line[9]) + ','+str(line[10]) +'\n'))


        # 修改版
        x = ",".join(str(i) for i in line) + '\n'
        f.write(x)