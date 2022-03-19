import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Map

df = pd.read_csv('贵阳处理之后.csv', encoding='utf-8')
df3 = df['区域'].value_counts()
areaX = df['区域'].value_counts().index.tolist()
data = []
for i in range(0, len(df3)):
    data.append((areaX[i], int(df3[i])))
print(data)
print(type(data))

c = (
    Map()
        .add(series_name='房源数', data_pair=data, maptype='贵阳')
        .set_global_opts(
        title_opts=opts.TitleOpts(title="贵阳区域房源数"), visualmap_opts=opts.VisualMapOpts()
    )
        .render("贵阳区域房源数.html")
)
