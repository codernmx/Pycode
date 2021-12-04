import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime

# 日期格式化
def dateReplace(date_list):
    new_date_list = []
    for date in date_list:
        new_date_list.append(str(date).replace("T", " ").split(".")[0])
    return new_date_list


if __name__ == '__main__':
    # excel绝对路径
    excel_path = "E:\\PyCharmCode\\咸鱼\\test\\test.xlsx"
    # 日期格式化
    date_format = "%Y-%m-%d %H:%M:%S"
    # 开始时间段
    date_start = datetime.datetime.strptime("2018-09-28 13:10:00", date_format)
    # 结束时间段
    date_end = datetime.datetime.strptime("2018-09-28 13:18:00", date_format)
    x_data = []
    y_data = []
    # 读取第一列
    excel = pd.read_excel(excel_path, index_col=0)
    # 列名
    excel_col = excel.columns.values
    # 读取最后一列
    excel1 = pd.read_excel(excel_path, index_col=len(excel_col))
    # 时间格式化
    date_list = dateReplace(excel.index.values)
    # 判断数据是否一致
    if (len(date_list) == len(excel1.index.values)):
        for index in range(0, len(date_list), 2):
        # 时间段判断
        # date = datetime.datetime.strptime(date_list[index], date_format)
        # if(date>=date_start and date<=date_end):
        #     index1=index+1
        #     if(index1==len(date_list)):
        #         index1=index
        #     print(str(date_list[index])+"-----"+str(excel1.index.values[index]))
        #     print(str(date_list[index1])+"-----"+str(excel1.index.values[index1]))
        #     avg=excel1.index.values[index]+excel1.index.values[index1]/2
        #     print(avg)
        #     date_str=str(date_list[index])+"-"+str(date_list[index1])
        #     x_data.append(date_str)
        #     y_data.append(avg)
            # 全部数据
            index1 = index + 1
            if (index1 == len(date_list)):
                index1 = index
            print(str(date_list[index]) + "-----" + str(excel1.index.values[index]))
            print(str(date_list[index1]) + "-----" + str(excel1.index.values[index1]))
            avg = excel1.index.values[index] + excel1.index.values[index1] / 2
            print(avg)
            # date_str = str(date_list[index]) + "-" + str(date_list[index1])
            date_str = str(date_list[index])
            x_data.append(date_str)
            y_data.append(avg)

# 弹窗
figsize = 12, 15
figure, ax = plt.subplots(figsize=figsize)
plt.plot(x_data, y_data, label='折线图', marker='.', linestyle='-', mfc='orange', ms=20, alpha=0.7, mec='c')
plt.xticks()
for tick in ax.get_xticklabels():
    tick.set_rotation(90)
plt.show()



# 网页的
# import random
# import pyecharts.options as opts
# from pyecharts.charts import Line
# print(random.randint(0, 9))
# x=x_data
# y=y_data
# # for i in range(500):
# #     x.append(i)
# #     y.append(random.randint(0, 10))
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
