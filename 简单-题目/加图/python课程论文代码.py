# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
@author: caijiashuo
"""
#Python课程论文——明星基业绩的可持续性#

import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.ticker import FuncFormatter

pd.set_option('display.max_rows', 10000)
pd.set_option('expand_frame_repr', False)  # 当列太多时不换行

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 设置命令行输出时的列对齐功能
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

# 读取基金数据文件
df = pd.read_csv('基金数据.csv', encoding='utf-8', skiprows=1)

# 读取指数涨跌幅数据并处理
exponent_df = pd.read_csv('指数涨跌幅.csv', encoding='gbk')
exponent_df['年份'] = pd.to_datetime(exponent_df['candle_end_time']).dt.year
exponent_df['年份'] = exponent_df['年份'].apply(str)
df.set_index('基金代码', inplace=True)
d = list(df.columns)


# 定义绘图函数
def draw_equity_curve(df, time, data_dict, pic_size=[22, 9], dpi=72, font_size=25):
    plt.rcParams['font.sans-serif'] = ['Heiti TC']
    plt.rcParams['axes.unicode_minus'] = False
    plt.figure(figsize=(pic_size[0], pic_size[1]), dpi=dpi)
    plt.xticks(fontsize=font_size)
    plt.yticks(fontsize=font_size)
    for key in data_dict:
        plt.plot(df[time], df[data_dict[key]], label=key)
    plt.legend(fontsize=font_size)
    plt.show()


# 次年表现统计
all_df = pd.DataFrame()
for i in range(df.shape[1] - 1):
    # 排序并选择前十基金
    df_ = df.copy().rank(ascending=False)
    df_now = df_.sort_values(d[i])
    now_ = list(df_now.head(10).index)

    # 次年排名、收益率、相对收益率计算
    all_df.loc[f'{d[i]}年前十基金次年', '年份'] = d[i + 1]
    all_df.loc[f'{d[i]}年前十基金次年', '排名均数'] = df_.loc[now_][d[i + 1]].mean() / df_[d[i + 1]].dropna().shape[0]
    all_df.loc[f'{d[i]}年前十基金次年', '平均收益率'] = df.loc[now_][d[i + 1]].mean()
    all_df.loc[f'{d[i]}年前十基金次年', '相对收益率'] = (
            df.loc[now_][d[i + 1]] - exponent_df[exponent_df['年份'] == d[i + 1]]['涨跌幅'].values[0]).mean()

# 将次年表现数据整理后输出
all_df.reset_index(inplace=True)
all_df = pd.merge(left=all_df, right=exponent_df[['涨跌幅', '年份']], how='left', on='年份')
all_df.rename(columns={'涨跌幅': '指数涨跌幅'}, inplace=True)
all_df.set_index('index', inplace=True)
print(all_df)

df3 = all_df[['年份', '相对收益率']]  #只要这两列

def to_percent(temp, position):
    return '%1.0f'%(10*temp) + '0%'

def drawBar(data):
    x = []
    y = []
    for index, row in data.iterrows():
        # print(row["面积"], row["价格"])
        x.append(row['年份'])
        y.append(row['相对收益率'])
    plt.bar(x, y, 0.4, color="bygrmck")
    plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))
    for a, b, i in zip(x, y, range(len(x))):
        if float(y[i])>0:
            plt.text(a, b+0.02, "%.2f%%" % (float(y[i]) * 100), ha='center', fontsize=8)  # 标注出每个点的值
        else:
            plt.text(a, b-0.03, "%.2f%%" % (float(y[i]) * 100), ha='center', fontsize=8)  # 标注出每个点的值
    plt.xlabel("年份")
    plt.ylabel("相对收益率")
    plt.title("当年超额收益前10基金 次年平均超额收益")
    plt.show()
drawBar(df3)

# 为画图表现准备，计算净值
all_df['基金净值计算'] = all_df['平均收益率'] + 1
all_df['指数净值计算'] = all_df['指数涨跌幅'] + 1
all_df['年份'] = all_df['年份'].astype('int')
all_df['年份'] = all_df['年份'] + 1
all_df['年份'] = all_df['年份'].apply(lambda x: str(x).split('.')[0])
all_df['基金净值'] = all_df['基金净值计算'].cumprod()
all_df['指数净值'] = all_df['指数净值计算'].cumprod()

# 展示数据结束时间
all_df.loc['2020年前十基金次年', '年份'] = '20210930'
all_df.set_index('年份', inplace=True)

# 默认开始的时候为1元
all_df.loc['2009', '基金净值'] = 1
all_df.loc['2009', '指数净值'] = 1
all_df.sort_values('年份', inplace=True)
all_df.reset_index(inplace=True)
print(all_df[['年份', '基金净值', '指数净值']])

# 画出净值图
draw_equity_curve(all_df, '年份', {'基金净值': '基金净值', '指数净值': '指数净值'})
