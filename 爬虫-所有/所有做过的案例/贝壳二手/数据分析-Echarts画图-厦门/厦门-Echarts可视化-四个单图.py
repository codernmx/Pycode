import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Pie
from pyecharts.charts import Bar, Page

page = Page()

df = pd.read_csv('厦门处理之后.csv', encoding='utf-8')

y_data = []
df1 = df[(df['单价'] >= 0) & (df['单价'] <= 50000)]
y_data.append(len(df1))
df2 = df[(df['单价'] >= 50001) & (df['单价'] <= 100000)]
y_data.append(len(df2))
df3 = df[(df['单价'] >= 100001) & (df['单价'] <= 150000)]
y_data.append(len(df3))
df4 = df[(df['单价'] >= 150001)]
y_data.append(len(df4))

# 饼图
x_data = ["0-5W", "5W-10W", "10W-15W", "大于15W"]
data_pair = [list(z) for z in zip(x_data, y_data)]
data_pair.sort(key=lambda x: x[1])

pie = (
    Pie()
        .add("", [list(z) for z in zip(x_data, y_data)])
        .set_global_opts(title_opts=opts.TitleOpts(title="厦门房价价格区间统计"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
        .render("厦门房价价格区间统计-饼图.html")
)

# 柱状图数据
df3 = df['区域'].value_counts()
areaX = df['区域'].value_counts().index.tolist()
areaY = []
for i in df3:
    areaY.append(i)

# 柱状图
bar = Bar()
bar.add_xaxis(areaX)
bar.add_yaxis("区域房源数", areaY)
bar.render("区域统计-柱状图.html")

# 折线图
# 获取折线图数据
df2 = df['小区'].value_counts()
name = df['小区'].value_counts().index.tolist()
data = []
for i in df2:
    data.append(i)

x_data = name[0:5]
y_data = data[0:5]
print(x_data)
from pyecharts.charts import Line

c = (
    Line()
        .add_xaxis(x_data)
        .add_yaxis("小区房源数量统计", y_data)
        .set_global_opts(title_opts=opts.TitleOpts(title="前五小区房源数折线图"))
        .render("小区房源数量统计-折线图.html")
)
from pyecharts.charts import Scatter

# 散点图
two = df[['单价', '总价']].head(100)  # 一百个数据的散点图
data = []
for index, row in two.iterrows():
    print(row["单价"], row["总价"])
    one = row["单价"]
    two = row["总价"]
    data.append([one, two])
data.sort(key=lambda x: x[0])
x_data = [d[0] for d in data]
y_data = [d[1] for d in data]
(
    Scatter()
        .add_xaxis(xaxis_data=x_data)
        .add_yaxis(
        series_name="",
        y_axis=y_data,
        symbol_size=20,
        label_opts=opts.LabelOpts(is_show=False),
    )
        .set_series_opts()
        .set_global_opts(
        title_opts=opts.TitleOpts(
            title="一百个单价房价散点图",
            pos_left="center",
            pos_top="20",
            title_textstyle_opts=opts.TextStyleOpts(color="#fff"),
        ),
        legend_opts=opts.LegendOpts(is_show=False),
        xaxis_opts=opts.AxisOpts(
            type_="value", splitline_opts=opts.SplitLineOpts(is_show=True)
        ),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
        tooltip_opts=opts.TooltipOpts(is_show=False),
    )
        .render("单价总价散点图-散点图.html")
)
