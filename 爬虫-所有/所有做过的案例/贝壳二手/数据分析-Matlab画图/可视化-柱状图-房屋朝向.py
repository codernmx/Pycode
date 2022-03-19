import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('北京处理之后.csv', encoding='utf-8')

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


df3 = df['房屋朝向'].value_counts()[:8]
x = df['房屋朝向'].value_counts().index.tolist()[:8]
y = []
for i in df3:
    y.append(i)  #获取y的值
plt.bar(x, y, 0.4, color="bygrmck")
for a, b, i in zip(x, y, range(len(x))):
    plt.text(a, b + 5, "%.f" % y[i], ha='center', fontsize=10)  # 标注出每个点的值
plt.xlabel("房屋朝向")
plt.ylabel("数量")
plt.title("房屋朝向前八柱状图")
plt.show()
