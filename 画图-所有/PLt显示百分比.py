# 绘制2020营业收入分布饼图
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']   #设置简黑字体
mpl.rcParams['axes.unicode_minus'] = False # 解决‘-’bug
fig = plt.figure()
fig.canvas.set_window_title("2020年营业收入饼图")
# 总数据
Num =4483700
# 单个数据
data = [345700,388000,354780,372300,322000,384200,401200,424000,392000,354820,343500,401200]
# 数据标签
labels = ['1月', '2月', '3月', '4月', '5月', '6月', '7月','8月','9月','10月','11月','12月']
# 各区域颜色
colors = ['red', 'orange', 'yellow', 'green', 'purple', 'blue', 'gray','pink','yellow','blue','green','orange']
# 数据计算处理
sizes = [i / Num * 100 for i in data]# 设置突出模块偏移值
expodes = (0, 0, 0.1, 0, 0, 0, 0,0,0,0,0,0)
# 设置绘图属性并绘图
plt.pie(sizes, explode=expodes, labels=labels, shadow=True, colors=colors,autopct = '%1.1f%%')
plt.title("2020年营业收入饼图")
## 用于显示为一个长宽相等的饼图
plt.axis('equal')
# 保存并显示
plt.savefig('fig3.png')
plt.show()