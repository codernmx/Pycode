import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator

df = pd.read_csv('北京.csv', encoding='utf-8')
pd.set_option('display.max_columns', None)
df = df.fillna('无')  # 替换所有NaN
# 户型,楼层,面积,装修情况,价格,小区,区域,房屋朝向,配置电梯,挂牌时间,房屋用途
df['户型'].replace(r'\s+|\\n', ' ', regex=True, inplace=True)  # 去除\r\n
df['楼层'].replace(r'\s+|\\n', ' ', regex=True, inplace=True)  # 去除\r\n
df['面积'].replace(r'\s+|\\n', ' ', regex=True, inplace=True)  # 去除\r\n
df['装修情况'].replace(r'\s+|\\n', ' ', regex=True, inplace=True)  # 去除\r\n
df['价格'].replace(r'\s+|\\n', ' ', regex=True, inplace=True)  # 去除\r\n
df['小区'].replace(r'\s+|\\n', ' ', regex=True, inplace=True)  # 去除\r\n
df['区域'].replace(r'\s+|\\n', ' ', regex=True, inplace=True)  # 去除\r\n
df['房屋朝向'].replace(r'\s+|\\n', ' ', regex=True, inplace=True)  # 去除\r\n
df['配置电梯'].replace(r'\s+|\\n', ' ', regex=True, inplace=True)  # 去除\r\n
df['挂牌时间'].replace(r'\s+|\\n', ' ', regex=True, inplace=True)  # 去除\r\n
df['房屋用途'].replace(r'\s+|\\n', ' ', regex=True, inplace=True)  # 去除\r\n


df['房屋朝向'] = df['房屋朝向'].str.replace(' ', '', regex=False) #房屋朝向去除空格

# print(df.head(10))





# df.to_csv('北京处理之后.csv', index=False, encoding='utf_8_sig')

