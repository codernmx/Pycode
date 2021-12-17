import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rcParams['font.san-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_excel('abc公司销售数据.xls')
df.head()