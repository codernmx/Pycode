import os
import pandas as pd
imgPath = 'D:\\PycharmCode\\pycode\\文字-SDK-包括PDF转图片\\img'  #需要修改的文件夹路径
df = pd.read_csv('1641874413656.csv', index_col=['图片名称', '单号'])
num = 0
for row in df.iterrows():
    path = row[0][0]
    newName = row[0][1]
    if 'nan' not in str(newName):
        num += 1
        suffix = '.' + path.split('.')[1]
        try:
            print(imgPath + newName + suffix)
            os.rename(path, imgPath+newName+suffix)

        except:
            print('{}------>>修改失败，找不到当前文件'.format(path))
print('文件总个数{}，当前处理的文件个数为{}'.format(len(df), num))
