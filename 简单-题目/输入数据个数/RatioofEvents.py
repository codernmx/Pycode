# 第一题
def func1():
    num = int(input('您想输入多少个数？'))
    allList = []
    for i in range(0, num):
        value = input('请输入第' + str(int(i) + 1) + '个整数：')
        allList.append(value)
    evenList = []
    numb = 0
    for i in allList:
        if float(i) % 2 == 0:
            numb += 1
            evenList.append(i)
    pro = numb / len(allList)
    print('您所输入的所有数中，偶数有', '、'.join(evenList), '一共', numb, '个，占所有输入数据的比例为：{:.6%}'.format(pro))


# 第二题
def func2():
    print('本程序将计算两个非负整数之间所有素数的和。')
    one = int(input('请输入第一个非负整数：'))
    two = int(input('请输入第二个非负整数：'))
    listAll = []
    for i in range(one, two + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            listAll.append(i)
    sun = 0
    for i in listAll:
        sun += i
    print("+".join('%s' % i for i in listAll), '=', sun)


def func3():
    value = input('请输入蔬菜名称：')
    info = {
        '鸡蛋': 2.95,
        '新土豆': 1.68,
        '长白菜	': 1.28,
        '圆白菜': 1.38,
        '青萝卜': 0.45,
        '西芹': 3.58
    }
    if str(value) in info:
        print('{}的单价为{}'.format(value, info[value]))
    else:
        print('无此品种。')
func3()
