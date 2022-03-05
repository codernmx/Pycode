import os
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Line, Radar, Bar, Page, Scatter

df = pd.read_excel('各地区预期寿命不同省份_雷达图.xlsx')

df = df.dropna()
two = df[['地区', '预期寿命_合计(岁)']]
area = []
age = []
for index, row in two.iterrows():
    area.append(row['地区'])
    age.append(row['预期寿命_合计(岁)'])
print(area)
c_schema = []
for i in area:
    c_schema.append({
        "name": i
    })
print(age)
c = (
    Radar()
        .add_schema(schema=c_schema, shape="circle")
        .add("预期寿命_合计/岁", [age], color="red")
        .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
        .set_global_opts(title_opts=opts.TitleOpts(title="地区预期寿命_合计"))
        .render("雷达图.html")
)
os.system('雷达图.html')
