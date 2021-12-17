import os
import pandas as pd
import numpy as np
path='E:/PyCharmCode/咸鱼/324文件夹/异常数据/'
all_path=os.listdir(path)
all_path.sort()
print(all_path)
# all_path.remove("result1111.xlsx")
all_path.sort(key=lambda x: int(x[:-7]))
#print(all_path)
#all_path.remove('.DS_Store')
#all_path.sort(key=lambda x:int(x.split('.')[0]))
#all_path.sort()
numb = 0
for name in all_path:
    print(name)
    list1 = {}
    with open(path+name,mode='r',encoding='utf-8') as f:
        for i in f.readlines():
            a=i.strip().split(':')
            b=a[1]   #b时间戳那一列
            c=a[-4]  #距离实测值那一列
            list1.setdefault(b,[]).append(c)
    jishu=0
    matrix1 = []
    for time,dist in list1.items():
        if len(dist) != 4:
                jishu +=1
        if len(dist)==4:
                dist.insert(0,time)
                matrix1.append(dist)
    numb+=1
    df1 = pd.DataFrame(matrix1, columns=['时间戳', '距离1', '距离2', '距离3', '距离4'])
    # print(df1.shape)
    df1.drop_duplicates(subset=['距离1', '距离2', '距离3', '距离4'], keep='first', inplace=True)
    # print(df1.shape)
    # 用3sigma排出异常点del_abnormal
    def del_abnormal(df1, ks_res=1):
        u = df1.mean()  # 均值
        std = df1.std()
        if ks_res == 1:
            error = df1[np.abs(df1 - u) > 3 * std]
            return error
    matrix2 = []
    data1 = del_abnormal(df1['距离1'].transform(lambda x: int(x))).index
    for i in data1:
        matrix2.append(i)
    data1 = del_abnormal(df1['距离2'].transform(lambda x: int(x))).index
    for i in data1:
        matrix2.append(i)
    data1 = del_abnormal(df1['距离3'].transform(lambda x: int(x))).index
    for i in data1:
        matrix2.append(i)
    data1 = del_abnormal(df1['距离4'].transform(lambda x: int(x))).index
    for i in data1:
        matrix2.append(i)
    df1.drop(matrix2, inplace=True)
    # print(df1.shape)
    df1.to_excel('E:/PyCharmCode/咸鱼/324文件夹/结果44/' + str(numb) + '.异常.xlsx', encoding='utf-8', index=False)



