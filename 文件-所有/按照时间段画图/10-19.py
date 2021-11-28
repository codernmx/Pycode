import pandas as pd
from datetime import datetime
txt_path='daynight.txt'
excel_path='test.xlsx'

with open(txt_path,'r',encoding='utf-8') as f:
    text=f.read()
    text=text.replace(' ,',',')
    text=text.replace('\n',',')
    lines=text.split(',')[:-1]
list=[]
print(lines)
for i in range(1,len(lines)-1,2):
    start=datetime.strptime(lines[i]+':00', '%Y-%m-%d %H:%M:%S')
    end=datetime.strptime(lines[i+1]+':00','%Y-%m-%d %H:%M:%S')
    cop=(start,end)
    list.append(cop)


df=pd.read_excel(excel_path)
indexs=[]
for cop in list:
    temp_df=df[(df['date_time']>=cop[0]) & (df['date_time']<=cop[1])]
    if len(temp_df)>0:
        indexs+=temp_df.index.values.tolist()

df=df.iloc[indexs]

import random
import pyecharts.options as opts
from pyecharts.charts import Line
print(random.randint(0, 9))
from pyecharts.faker import Faker


x=df['date_time']
y=df['PWV']

line=(
    Line(
      init_opts=opts.InitOpts(
        width='100%',
        height='80vh',
      )
    )

    .set_global_opts(

        datazoom_opts=opts.DataZoomOpts(),
        tooltip_opts=opts.TooltipOpts(is_show=False),
        xaxis_opts=opts.AxisOpts(
          type_="category",
          splitline_opts=opts.SplitLineOpts(is_show=True),# 这里将分割线显示
        ),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
    )
    .add_xaxis(xaxis_data=x)
    .add_yaxis('统计图',y)
)
line.render()
