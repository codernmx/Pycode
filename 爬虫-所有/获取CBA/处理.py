import pandas as pd


df = pd.read_csv('CBA.csv', encoding='utf-8')
pd.set_option('display.max_columns', None)
df = df.fillna('无')  # 替换所有NaN
# 户型,楼层,面积,装修情况,价格,小区,区域,房屋朝向,配置电梯,挂牌时间,房屋用途
df['球队名'].replace(r'\s+|\\n', ' ', regex=True, inplace=True)  # 去除\r\n
df['比赛时间'].replace(r'\s+|\\n', ' ', regex=True, inplace=True)  # 去除\r\n
df['主队'].replace(r'\s+|\\n', ' ', regex=True, inplace=True)  # 去除\r\n
df['得分情况'].replace(r'\s+|\\n', ' ', regex=True, inplace=True)  # 去除\r\n
df['客队'].replace(r'\s+|\\n', ' ', regex=True, inplace=True)  # 去除\r\n
df.to_csv('CBA处理之后.csv', encoding='utf_8_sig') #存入csv
