#coding: utf-8
import pandas as pd
import numpy as np
df = pd.read_csv('成绩登记表.csv',encoding='gbk',index_col=0)
#求平均成绩
temp = df[["数学","语文","英语","专业课"]]
# df["total"] = temp.sum(axis=1)#axis 0为列，1为行
df["平均成绩"] = temp.mean(axis=1)
# print(df)
chineseMax = df['语文'].max() #最高成绩
chineseMin = df['语文'].min() #最低成绩
print(chineseMin)
allBoy = df[df.性别=='男']
allBoy =allBoy.sort_values('平均成绩',ascending=False)
# print(allBoy)  #平均值排序之后
# print(allBoy.mean())  #均值
# print(allBoy.var())  #方差
print(allBoy.std())  #标准差