file = open("成绩.txt", encoding='utf-8')
txt = []
for line in file.readlines():  #readlines获取所有行   line就是每行
    if line[0] == "#":  #过滤掉以#开头的
        continue
    txt.append(line.strip())  #将每一个添加到
print(txt, 'txt存入一个列表')


def sno_to_name():  #定义函数
    info = {}
    for item in txt:  #遍历  数据
        strlist = item.split('，') or item.split(',')  #以，或者,拆分数据
        info[strlist[0]] = strlist[1]  #添加字典的键和值
    print(info, '字典函数实现')


def avg(one, two, three):
    return (one + two + three)/3


sno_to_name()  #调函数 （实现学号到姓名的映射（字典））
test = []
for item in txt:
    strlist = item.split('，') or item.split(',')  # 用逗号分割str字符串，并保存到列表
    # average = round((int(strlist[2]) + int(strlist[3]) + int(strlist[4])) / 3)  #算平均值
    average = round(avg(int(strlist[2]),int(strlist[3]),int(strlist[4])))  #算平均值(取整和四舍五入往上取round)
    test.append(strlist)  #用于根据平均值排序（学号和姓名）
    strlist.append(average)  #用于根据平均值排序（平均值）
test.sort(key=lambda x: x[5], reverse=True)
data = []  #写入成绩排序的数据
for item in test:
    data.append('，'.join(item[0:2]) + '，' + str(item[5]))  #添加每一行数据
with open('成绩排序.txt', 'a+', encoding='utf-8') as f:
    for ite in data:
        f.write(ite + '\n')  # 添加‘\n’用于换行
    f.close()  #关闭文件
