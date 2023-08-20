import os

import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker

data = [('海淀区', 650), ('朝阳区', 234), ('顺义区', 257)]


df = pd.read_csv('北京处理之后.csv', encoding='utf-8')
df3 = df['区域'].value_counts()
areaX = df['区域'].value_counts().index.tolist()
data = []
for i in range(0,len(df3)):
    data.append((areaX[i]+'区',int(df3[i])))
print(data)
print(type(data))

c = (
    Map()
        .add(series_name='房源数', data_pair=data, maptype='北京')
        .set_global_opts(
        title_opts=opts.TitleOpts(title="北京区域房源数"), visualmap_opts=opts.VisualMapOpts()
    )
        .render("map_guangdong.html")
)

os.system('map_guangdong.html')
