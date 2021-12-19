import pandas as pd


df = pd.read_csv('CBA.csv', encoding='utf-8')
pd.set_option('display.max_columns', None)
df = df.fillna('无')  # 替换所有NaN
#
df['球队名'].replace(r'\s+|\\n', ' ', regex=True, inplace=True)  # 去除\r\n\t
df['比赛时间'].replace(r'\s+|\\n', ' ', regex=True, inplace=True)  # 去除\r\n\t
df['主队'].replace(r'\s+|\\n', ' ', regex=True, inplace=True)  # 去除\r\n\t
df['比分情况'].replace(r'\s+|\\n', ' ', regex=True, inplace=True)  # 去除\r\n\t
df['客队'].replace(r'\s+|\\n', ' ', regex=True, inplace=True)  # 去除\r\n\t
df.to_csv('CBA处理之后.csv', encoding='utf_8_sig') #存入csv
