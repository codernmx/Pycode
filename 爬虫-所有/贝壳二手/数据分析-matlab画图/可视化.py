import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator

df = pd.read_csv('北京处理之后.csv', encoding='utf-8')

#获取可视化数据
df2 = df['房屋用途'].value_counts()
name = df['房屋用途'].value_counts().index.tolist()
data = []
for i in df2:
    data.append(i)

#区域房源数统计图
df3 = df['区域'].value_counts()
areaX = df['区域'].value_counts().index.tolist()
areaY = []
for i in df3:
    areaY.append(i)


# 房屋用途折线图
plt.xlabel('房屋用途种类')
plt.ylabel('房屋用途数量')
plt.title('北京房屋用途种类统计')
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.ylim = (10, 40000)
x_major_locator = MultipleLocator(1)
ax = plt.gca()# ax为两条坐标轴的实例
ax.xaxis.set_major_locator(x_major_locator)# 把x轴的刻度间隔设置为1，并存在变量里
for a, b, i in zip(name, data, range(len(name))):
    plt.text(a, b + 1, "%.f" % data[i], ha='center', fontsize=10)  #标注出每个点的值

plt.plot(name,data, color='red', linewidth=0.5, linestyle='-', label='数量')  # linestyle指定线
plt.legend()
plt.show()


# 房屋用途折线图
plt.xlabel('北京地区')
plt.ylabel('北京区域房源数')
plt.title('北京区域房源数统计')
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.ylim = (10, 40000)
x_major_locator = MultipleLocator(1)
ax = plt.gca()# ax为两条坐标轴的实例
ax.xaxis.set_major_locator(x_major_locator)# 把x轴的刻度间隔设置为1，并存在变量里

for a, b, i in zip(areaX, areaY, range(len(areaX))):
    plt.text(a, b + 1, "%.f" % areaY[i], ha='center', fontsize=10)  #标注出每个点的值

plt.plot(areaX,areaY, color='r', linewidth=0.5, linestyle='-', label='数量')  # linestyle指定线
plt.legend()
plt.show()