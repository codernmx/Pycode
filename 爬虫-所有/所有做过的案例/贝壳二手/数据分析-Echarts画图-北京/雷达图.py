import os

import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Line, Radar, Bar, Page, Scatter

df = pd.read_csv('北京处理之后-新.csv', encoding='utf-8')

df3 = df['房屋朝向'].value_counts()
areaX = df['房屋朝向'].value_counts().index.tolist()
areaY = []
for i in df3:
    areaY.append(i)
info = {}
for i in range(0, len(areaX)):
    info[areaX[i]] = areaY[i]
houseCount = []  # 八个方位对应的房源数
directionList = ['东', '东北', '东南', '北', '南', '西', '西北', '西南']  # 八个方位
for i in directionList:
    houseCount.append(info[i])

# 计算房屋朝向均价(按照朝向分组筛选八个)
priceList = []
df = df.groupby("房屋朝向")["价格"].mean()
for index, row in df.items():
    if index == '东' or index == '南' or index == '西' or index == '北' or index == '东北' or index == '西北' or index == '东南' or index == '西南':
        priceList.append(int(row))

c_schema = []
for i in directionList:
    # c_schema.append({"name": i, "max": 400, "min": 10},)
    c_schema.append({"name": i}, )

c = (
    Radar()
        .add_schema(schema=c_schema, shape="circle")
        .add("房屋朝向/房源数", [houseCount], color="red")
        .add("均价/万元", [priceList], color="blue")
        .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
        .set_global_opts(title_opts=opts.TitleOpts(title="房屋朝向价格雷达图"))
        .render("雷达图.html")
)
os.system('雷达图.html')
