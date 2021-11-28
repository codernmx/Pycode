# @Time : 2021/10/30 20:25
# @Author : VX:Until_Day_Break
# @SoftWare : PyCharm
import random

file = open("text.txt", encoding='utf-8')
txt = ''
for line in file.readlines():  # readlines获取所有行   line就是每行
    txt += line.strip()  # 将每一个添加到
print(txt)


# 替换字符串string中指定位置char的字符为index
def replace_char(string, char, index):
    xx = []
    for i in string:
        xx.append(str(i))
    xx[char] = index
    allStr = ''.join(xx)
    return allStr

a = random.sample(range(0, 1024), 50)  #随机生成50个数 用于替换随机数位置
a.sort()
print(len(a))
print(a)

for x in a:  #遍历每一次替换
    print(len(txt))
    if txt[x] == '0':
        newStr = '1'
        txt = replace_char(txt, x, newStr)
    else:
        newStr = '0'
        txt = replace_char(txt, x, newStr)
    print(txt)

# 按照三十二个切割
def cut(obj, sec):
    return [obj[i:i + sec] for i in range(0, len(obj), sec)]
cutList = cut(txt, 32)
with open('text.txt', 'w', encoding='utf-8') as f:
    for ite in cutList:
        f.write(ite + '\n')  # 添加‘\n’用于换行
    f.close()  # 关闭文件
