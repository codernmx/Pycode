import pandas as pd
import json

#read_excel()用来读取excel文件，记得加文件后缀
data = pd.read_excel('F:\Desktop\模板.xlsx') 
# print('显示表格的属性:',data.shape)   #打印显示表格的属性，几行几列
print('显示表格的列名:',data.columns) #打印显示表格有哪些列名
# #head() 默认显示前5行，可在括号内填写要显示的条数
# print('显示表格前三行:',data.head(1)) 
# print('--------------------------华丽的分割线----------------------------')
# #tail() 默认显示后5行，可在括号内填写要显示的条数
# print('显示表格后五行:',data.tail())
# print(data.to_json(orient='index'))
