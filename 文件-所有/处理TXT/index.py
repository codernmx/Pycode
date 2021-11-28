import os

path = 'docs/'
# 读取将路径下的所有txt文件 组成一个字符串
def func1(path):
    all_path = os.listdir(path)
    all_str = ''
    for name in all_path:
        with open(path + name, mode='r', encoding='utf-8') as f:
            for i in f.readlines():
                # print(i)
                all_str += i
    return all_str

def func2(str_en):
    str_en = str_en.replace('  ', '')  # 去掉空格
    str_en = str_en.replace('\n', '')  # 去掉换行
    str_en = str_en.replace('.', '')  # 去掉.
    str_en = str_en.replace(',', '')  # 去掉，
    str_en = str_en.replace('"', '')  # 去掉''
    str_en = str_en.replace(';', '')  # 去掉;
    str_en = str_en.replace('?', '')  # 去掉?
    str_en = str_en.replace('!', '')  # 去掉!
    str_en = str_en.replace('  ', '')  # 最后去除一次空格
    last_str = str_en.lower() #转为小写
    print(last_str)
    return last_str

def func3():
    str = func1(path)
    last_str = func2(str)
    count = {}
    # 获取出现最多次数的单词
    str_list = last_str.split(' ')
    for word in str_list:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    # 排序 # 按字典集合中，每一个元组的第二个元素排列。# x相当于字典集合中遍历出来的一个元组。
    count_order = sorted(count.items(), key=lambda x: x[1], reverse=True)
    for key in count_order[0:5]:
        print('前五的单词', key[0], '---------', '次数', key[1])
func3()
