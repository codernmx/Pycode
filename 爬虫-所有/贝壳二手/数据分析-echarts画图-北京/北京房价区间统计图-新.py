import os
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Line, Pie, Bar, Page, Scatter
from pyecharts.globals import ThemeType

# 读取文件
df = pd.read_csv('北京处理之后-新.csv', encoding='utf-8')

y_data = []
df1 = df[(df['价格'] >= 0) & (df['价格'] <= 200)]
y_data.append(len(df1))
df2 = df[(df['价格'] >= 201) & (df['价格'] <= 400)]
y_data.append(len(df2))
df3 = df[(df['价格'] >= 401) & (df['价格'] <= 600)]
y_data.append(len(df3))
df4 = df[(df['价格'] >= 601) & (df['价格'] <= 800)]
y_data.append(len(df4))
df5 = df[(df['价格'] >= 801)]
y_data.append(len(df5))
# 饼图
x_data = ["0-200W", "201W-400W", "401W-600W", "601W-800W", "大于800W"]

pie = (
    Pie(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add("", [list(z) for z in zip(x_data, y_data)])
        .set_global_opts(title_opts=opts.TitleOpts(title="北京房价区间统计"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
        .render("北京房价区间统计.html")
)

os.system('北京房价区间统计.html')
