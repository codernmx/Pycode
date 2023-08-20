import pandas as pd

df = pd.read_csv('新闻.csv', encoding='utf-8')
pd.set_option('display.max_columns', None)
df['标题'].replace(r'\s+|\\n', ' ', regex=True, inplace=True)  # 去除\r\n
df['日期'].replace(r'\s+|\\n', ' ', regex=True, inplace=True)  # 去除\r\n
df['作者'].replace(r'\s+|\\n', ' ', regex=True, inplace=True)  # 去除\r\n
df['内容'].replace(r'\s+|\\n', ' ', regex=True, inplace=True)  # 去除\r\n
df['文章链接'].replace(r'\s+|\\n', ' ', regex=True, inplace=True)  # 去除\r\n

df = df.dropna(subset=['标题', '日期', '作者', '内容', '文章链接'])  # 清楚所有含有空的数据
# df = df.dropna(subset=['标题']) # 保留后边四个字段有为空的数据

df = df.drop_duplicates(['标题', '日期', '作者', '内容', '文章链接'], keep='last')  # 去重
print(len(df))
df.to_csv('新闻-处理之后.csv', index=False, encoding='utf_8_sig')
