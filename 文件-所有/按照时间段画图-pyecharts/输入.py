import math
a = int(input("请输入一 冷量:"))
b = int(input("请输入每台机子的冷量:"))
print('需要开的冷机数量为',math.ceil(a/b))