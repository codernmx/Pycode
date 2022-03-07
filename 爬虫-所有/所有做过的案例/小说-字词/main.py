import random

import requests
import os
import jieba
import pandas as pd
import jieba.posseg as pseg #引入词性标注接口
path = 'file/'  # file文件夹


# 获取小说内容
# def capture(url):
#     # 获取小说网页地址
#     response = requests.get(url)
#     response.encoding = "utf-8"
#     text = response.text
#     title = text[text.find("<h1>") + 4: text.find("</h1>")]
#     context = text[text.find("查找最新章节") + 7: text.find("神仙给我发微信最新章节地址")]
#     # 去掉除内容以外的字符
#     context = context.replace("<p>", "").replace("</p >", "").replace(" ", "").replace(
#         '<pstyle="color:#999;font-size:10px;line-height:18px;">', "")
#     context = context.replace('</p>','')  #去掉没用的内容
#     print(title)
#     # print(context)
#     with open('file/'+str(title) + '.txt', 'a+', encoding='utf-8') as f:
#         f.write(context + '\n')  # 添加‘\n’用于换行
#         f.close()  # 关闭文件
#
# urlx = "https://www.bxwxorg.com/read/100383/240.html"
# for i in range(3397, 3515):
#     url = urlx.split('.html')[0] + '{}'.format(i) + '.html'# 改变地址
#     capture(url)


# 读取将路径下的所有txt文件 组成一个字符串
def func1(path):
    all_path = os.listdir(path)
    print(all_path)
    all_str = ''
    for name in all_path:
        with open(path + name, mode='r', encoding='utf-8') as f:
            for i in f.readlines():
                # print(i)
                all_str += i
    return all_str  # 所有文件组成的字符串

#使用结巴分词排序
def func2():
    strAll = func1(path)
    strAll = strAll.replace(' ', '')  # 空格
    strAll = strAll.replace('。', '')  # 。
    strAll = strAll.replace('\\n', '')  # \n
    ex = {'神仙', '给我发', '微信'}
    poss = pseg.cut(strAll)
    #jieba.load_userdict(r"中文停用词库.txt")
    #test = jieba.cut(strAll, cut_all=True)
    '''
    strAll = "，".join(test)
    strAll = strAll.replace(' ', '')  # 空格
    strAll = strAll.replace('。', '')  # 。
    strAll = strAll.replace('\n', '')  # \n
    strAllList = strAll.split('，')
    '''
    count = {}
    # 获取出现最多次数的单词
    for word in poss:
        if word.flag != 'n' or len(word.word) < 2 or word.word in ex:
            continue
        elif word.word in count and word != '':
            count[word.word] += 1
        else:
            count[word.word] = 1
    # 排序 # 按字典集合中，每一个元组的第二个元素排列。# x相当于字典集合中遍历出来的一个元组。
    count_order = sorted(count.items(), key=lambda x: x[1], reverse=True)
    for key in count_order[0:5]:
        print('频率最高前五的词——————————————>', key[0], '——————————————>', '次数', key[1])

# 读取人物列表 获取章节出现次数
def func3():
    # 计算全文 人物出现次数
    strAll = func1(path)
    file = open("people.txt", encoding='utf-8')
    for line in file.readlines():  # readlines获取所有行   line就是每行
        # 每一个人物出现的次数
        print(line.strip(),'共出场',strAll.count(line.strip()),'次')

    allInfo = []
    all_path = os.listdir(path)
    for name in all_path:  # 打开所有章节找任务
        # print(i)
        c = []
        a = [name]
        b = []
        with open(path + name, mode='r', encoding='utf-8') as f:
            all_str = ''
            for i in f.readlines():
                all_str += i
            file = open("people.txt", encoding='utf-8')
            for line in file.readlines():  # readlines获取所有行   line就是每行
                x = line.strip().replace('\n','')
                b.append(all_str.count(x))  # 每一个人物出现的次数
                # print(line.strip(),'---------',str(f.read()).count(str(line.strip())))
        c.extend(a)
        c.extend(b)
        allInfo.append(c)
    #存表格
    df = pd.DataFrame(allInfo)  # 将获取到的所有数据生成表格
    # 设置下边表格的字段
    df.columns = ['名称', '鲁力', '张宁', '卢出海', '柯震东', '观音姐姐', '徐鹏', '柯敏', '谢永年', '孟芸', '孟如兮', '雷灵', '李逍遥', '柳轻丝', '韦三腿',
                  '雷建功', '蓝长州', '陈圆圆', '莫小琪', '王帅', '熊本圣舞']
    #存文件
    df.to_csv('测试.csv',encoding='utf_8_sig')

#全文中匹配同时出现 片段
def find_co_occurrence(p1,p2):
    strAll = func1(path)
    strAll = strAll.replace(' ', '')  # 空格
    strAll = strAll.replace('。', '')  # 。
    strAll = strAll.replace('\n', '')  # \n
    jieba.load_userdict(r"中文停用词库.txt")
    test = jieba.tokenize(strAll)

    p1Liist = []
    p2Liist = []
    for i in test:
        if i[0] ==p1:
            p1Liist.append(i[1])
        if i[0] ==p2:
            p2Liist.append(i[1])
    for ii in p1Liist:
        if len(p2Liist)<=0:
            print('当前不存在满足条件的片段')
            break
        for num in p2Liist:
            if int(ii)-50 < num & num < int(ii)+50:
                p1Index = ii
                p2Index = p2Liist[p2Liist.index(num)]
                if p2Index!=p1Index and strAll[p1Index:p2Index + len(p2)] !='':
                    cutStr = strAll[p1Index:p2Index + len(p2)].replace(str(p1),'{'+str(p1)+'}')
                    cutStr = cutStr.replace(str(p2),'['+str(p2)+']')
                    print(cutStr)

# func2()
func3()
# find_co_occurrence('鲁力','徐鹏')
