# @Time : 2021/11/22 22:21
# @Author : VX:Until_Day_Break
# @SoftWare : PyCharm
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import os
import pandas as pd
import xlrd
import numpy as np

dir = "E:\\PyCharmCode\\文档-学习\\爬虫-所有\\阿里巴巴\\结果"  # 设置工作路径
# 新建列表，存放文件名（可以忽略，但是为了做的过程能心里有数，先放上）
filename_excel = []
# 新建列表，存放每个文件数据框（每一个excel读取后存放在数据框）
frames = []
for root, dirs, files in os.walk(dir):
    for file in files:
        print(os.path.join(root,file))
        filename_excel.append(os.path.join(root, file))
        df = pd.read_excel(os.path.join(root,file))  # excel转换成DataFrame
        frames.append(df)
# 打印文件名
print(filename_excel)
# 合并所有数据
result = pd.concat(frames)
# 查看合并后的数据
result.head()
result.shape
# df.to_csv('data.csv', encoding='utf_8_sig')
result.to_csv(dir+'总.csv', sep=',', index=False, encoding='utf_8_sig')  # 保存合并的数据到电脑