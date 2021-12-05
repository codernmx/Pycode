import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator

df = pd.read_csv('厦门.csv', encoding='utf-8')
pd.set_option('display.max_columns', None)
df = df.fillna('无')  # 替换所有NaN
# 区域,小区,总价,房型,面积,单价,朝向,楼层位置,装修情况,建筑时间,是否有电梯,产权类型,挂牌时间
df['区域'].replace(r'\s+|\\n', ' ', regex=True, inplace=True)  # 去除\r\n
df['小区'].replace(r'\s+|\\n', ' ', regex=True, inplace=True)  # 去除\r\n
df['总价'].replace(r'\s+|\\n', ' ', regex=True, inplace=True)  # 去除\r\n
df['房型'].replace(r'\s+|\\n', ' ', regex=True, inplace=True)  # 去除\r\n
df['面积'].replace(r'\s+|\\n', ' ', regex=True, inplace=True)  # 去除\r\n
df['单价'].replace(r'\s+|\\n', ' ', regex=True, inplace=True)  # 去除\r\n
df['朝向'].replace(r'\s+|\\n', ' ', regex=True, inplace=True)  # 去除\r\n
df['楼层位置'].replace(r'\s+|\\n', ' ', regex=True, inplace=True)  # 去除\r\n
df['装修情况'].replace(r'\s+|\\n', ' ', regex=True, inplace=True)  # 去除\r\n
df['建筑时间'].replace(r'\s+|\\n', ' ', regex=True, inplace=True)  # 去除\r\n
df['是否有电梯'].replace(r'\s+|\\n', ' ', regex=True, inplace=True)  # 去除\r\n
df['产权类型'].replace(r'\s+|\\n', ' ', regex=True, inplace=True)  # 去除\r\n
df['挂牌时间'].replace(r'\s+|\\n', ' ', regex=True, inplace=True)  # 去除\r\n


df['朝向'] = df['朝向'].str.replace(' ', '', regex=False) #房屋朝向去除空格


# print(df.head(10))
#
# pd.set_option('display.max_columns', None)  #展示所有字段
# topTen = df.sort_values(by = '单价',ascending=False).head(10)    #按照某一个字段排序
# topTen = topTen[['小区', '单价']]  #展示两个字段



df.to_csv('厦门处理之后.csv', index=False, encoding='utf_8_sig')

