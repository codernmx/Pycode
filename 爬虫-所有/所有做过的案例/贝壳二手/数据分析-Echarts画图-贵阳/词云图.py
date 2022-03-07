import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import WordCloud

df = pd.read_csv('贵阳处理之后.csv', encoding='utf-8')
df3 = df['房屋朝向'].value_counts()
areaX = df['房屋朝向'].value_counts().index.tolist()
data = []
for i in range(0, len(df3)):
    data.append((areaX[i], str(df3[i])))
print(data)

c = (
    WordCloud()
        .add(series_name='房屋朝向词云图', data_pair=data, word_size_range=[6, 66])
        .set_global_opts(
        title_opts=opts.TitleOpts(
            title='房屋朝向词云图', title_textstyle_opts=opts.TextStyleOpts(font_size=23)
        ),
        tooltip_opts=opts.TooltipOpts(is_show=True),
    )
        .render('房屋朝向词云图' + ".html")
)

df3 = df['小区'].value_counts()
areaX = df['小区'].value_counts().index.tolist()
data = []
for i in range(0, len(df3)):
    data.append((areaX[i], str(df3[i])))
print(data)
c = (
    WordCloud()
        .add(series_name='小区词云图', data_pair=data, word_size_range=[6, 66])
        .set_global_opts(
        title_opts=opts.TitleOpts(
            title='小区词云图', title_textstyle_opts=opts.TextStyleOpts(font_size=23)
        ),
        tooltip_opts=opts.TooltipOpts(is_show=True),
    )
        .render('小区词云图' + ".html")
)
