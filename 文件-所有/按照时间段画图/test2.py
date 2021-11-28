def test1(s):
    res = s.split(' ')
    result = {}
    for item in res:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    for item in result:
        if result[item] % 2 == 1:
            print(result[item])


def test2(n):
    num_list = []
    if 0 <= n <= 100:
        for i in range(0, n + 1):
            for j in range(0, n + 1):
                if (i + j) % 2 == 0:
                    for k in range(0, n + 1):
                        if (j + k) % 3 == 0 and (i + j + k) % 5 == 0:
                            num_list.append([i, j, k])
    print(num_list)
    result = [(item[0] + item[1] + item[2]) for item in num_list]
    print(max(result))


def test3():
    n = int(input())
    if n < 1:
        print("请输入大于0 的整数")
    elif 1 <= n <= 5:
        print(1)
    else:
        print(int(n / 5) + 1)


def test4():
    while True:
        num = input()
        num_in = 0
        if num.isdigit():
            num_in = int(num)
            flag = 1
            if num_in == 1 or num_in == 0:
                print(str(num_in) + ' 不是素数')
                flag = 0
            else:
                for i in range(2, num_in):
                    if i * i > num_in:
                        break
                    else:
                        if num_in % i == 0:
                            print(str(num_in) + ' 不是素数')
                            flag = 0
            if flag == 1:
                print(str(num_in) + ' 是素数')
        elif num == 'n' or num == 'N':
            break
        else:
            print('输入数字不合法，请重新输入')


test1('1 1 2 2 2 5 5')
test2(5)
test3()
test4()
