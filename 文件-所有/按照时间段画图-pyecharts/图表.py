
file = open("daynight.txt")
txt = []
for line in file.readlines():  #readlines获取所有行   line就是每行
    for ite in line.strip().split(','):
      txt.append(ite)
# print(txt[1:], 'txt存入一个列表')
txt = txt[1:]  #第一个数 和第二个为一个 时间段


import pandas as pd
# df = pd.read_excel('test.xlsx',index_col=0)
# data = df.head(30)
# print(data)
# data = pd.read_excel(r'pwv_weather.xlsx')
# # 每个excel保存3万行，那么530000+数据需要18个.csv文档保存
# for i in range(0, 10000):
#   save_data = data.iloc[i*106 + 1 : (i+1)*106+1]
#   file_name = r'' + str(i) + '.xlsx'  # 保存文件路径以及文件名称
#   save_data.to_excel('E:/PyCharmCode/咸鱼/test/分割/'+file_name, index=False)  # 保存格式为.csv，如果是xlsx则修改为save_data.to_excel
import datetime
import numpy as np
from pandas import Series, DataFrame

# 以 datetime 为索引，读取数据

# 将索引类型改成 DatetimeIndex
# df.index = pd.DatetimeIndex(df.index)
# time_start = datetime()
# # 根据索引筛选
# s_date = datetime.datetime.strptime('20180928', '%Y%m%d').date()
# e_date = datetime.datetime.strptime('20181001', '%Y%m%d').date()
# df = df[(df['date_time'] >= s_date) & (df['date_time'] <= e_date)]




df = pd.read_excel(r'test.xlsx')
df = pd.DataFrame(df)
# print(df['date_time'])
# print(df)
import time
s_date = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(20180928))
e_date = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(20180928))
# s_date = time.strftime("%Y/%m/%d %H:%M:%S", ['20180928'])
# e_date = time.strftime("%Y/%m/%d %H:%M:%S", ['20181001'])
# s_date = date(2012,12,1)
# e_date = date(2012,12,1)
#
df = df.loc[(df['date_time'] >= s_date) & (df['date_time'] <= e_date)]
print(df)















# import random
# import pyecharts.options as opts
# from pyecharts.charts import Line
# print(random.randint(0, 9))
# x=[]
# y=[]
# for i in range(500):
#     x.append(i)
#     y.append(random.randint(0, 10))
# line=(
#     Line(
#       init_opts=opts.InitOpts(
#         width='100%',
#         height='80vh',
#         # renderer='svg',
#         # page_title='0',
#         # theme='1',
#         # bg_color='#818181',
#         # js_host='file:///E:/%E5%8F%AF%E8%A7%86%E5%8C%96%E7%9B%AE%E5%BD%95/2019-10.html'
#
#       )
#     )
#     .set_global_opts(
#
#         datazoom_opts=opts.DataZoomOpts(),
#         tooltip_opts=opts.TooltipOpts(is_show=False),
#         xaxis_opts=opts.AxisOpts(type_="category"),
#         yaxis_opts=opts.AxisOpts(
#             type_="value",
#             axistick_opts=opts.AxisTickOpts(is_show=True),
#             splitline_opts=opts.SplitLineOpts(is_show=True),
#         ),
#     )
#     .add_xaxis(xaxis_data=x)
#     .add_yaxis('统计图',y)
#     # .add_yaxis(
#     #     series_name="统计图",
#     #     y_axis=y,
#     #     symbol="emptyCircle",
#     #     is_symbol_show=True,
#     #     label_opts=opts.LabelOpts(is_show=False),
#     # )
# )
# line.render()


