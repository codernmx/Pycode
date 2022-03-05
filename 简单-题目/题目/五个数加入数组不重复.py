infoList = []
a = input('请输入第一个数字：')
infoList.append(a)
# 如果数组中存在当前输入的值就重新输入  再添加到数组中 避免重复
def inList(x, reList):
	if (x in reList):
		x = input('请重新输入一个数字替代当前重复数：')
		inList(x, reList)
	else:
		infoList.append(x)
b = input('请输入第二个数字：')
inList(b, infoList)
c = input('请输入第三个数字：')
inList(c, infoList)
d = input('请输入第四个数字：')
inList(d, infoList)
e = input('请输入第五个数字：')
inList(e, infoList)
infoList.sort()  #排序求最大值和最小值
num = 0
for i in infoList:  #遍历求和
	num += int(i)
infoList[3] = 100
print('所有元素之和为：', num)
print('最小值为：', infoList[0])   #取第一个为最小值
print('最大值为：', infoList[len(infoList) - 1])  #取最后一个为最大值
print(infoList)  #输出列表
print('J2000408 刘嘉诚')
