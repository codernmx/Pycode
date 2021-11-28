import arrow
import requests  #网络请求需要的库
import xlwt
from bs4 import BeautifulSoup   #解析网页需要的库
import pandas as pd    #存文件需要的库

listOne = ['经济', '金融']  # 需要筛选的分类一
# 需要筛选的分类二
listTwo = ['不确定', '不明确', '波动', '震荡', '动荡', '不稳', '未明', '不明朗', '不清晰', '未清晰'
    , '难料', '难以预料', '难以预测', '难以预计', '难以估计', '无法预料', '无法预计', '无法估计', '不可预料', '不可预测',
           '不可预计', '不可估计', '矛盾', '调整', '改革', '整改', '转换', '变化', '新的隐患', '失速', '忽视', '风险']
# 需要筛选的分类三
listThree = ['政策', '制度', '体制', '战略', '措施', '规章', '规例', '条例', '政治',
             '执政', '政府', '政委', '国务院', '人大', '人民代表大会', '中央国家主席', '总书记', '国家领导人', '总理', '改革', '整改', '整治', '规管', '监管',
             '财政',
             '税收人民银行', '央行', '赤字', '利率',
             '机制', '制度', '放管服', '营商环境', '房地产', '经信委', '发改委', '工商局']


# 断言：年份不为整数时，抛出异常。
def isLeapYear(years):   #获取一年每一天日期的函数
    assert isinstance(years, int), "请输入整数年，如 2018"  #整数
    if ((years % 4 == 0 and years % 100 != 0) or (years % 400 == 0)):  # 判断是否是闰年
        # print(years, "是闰年")
        days_sum = 366  #366天
        return days_sum
    else:
        # print(years, '不是闰年')
        days_sum = 365  #365天
        return days_sum


# 获取一年的所有天数
def getAllDayPerYear(years):
    start_date = '%s-1-1' % years  #格式化日期
    a = 0
    all_date_list = []  #存每一天的数据（2016-01-01，2016-01-02）
    days_sum = isLeapYear(int(years))  #得到总天数
    while a < days_sum:
        b = arrow.get(start_date).shift(days=a).format("YYYY-MM-DD")
        a += 1
        all_date_list.append(b)
    return all_date_list  #返回每一天的具体日期

def getShowCount(data, url, urlCut):  #获取每一页报纸的所有数据
    allInfo = []
    number = 0  #记录满足要求的次数
    total = 0 #记录总数
    headers = {  #请求头
        "Cookie": 'Guid=%7Bd1d6e764-4683-13c1-4788-cbb331b186a6%7D; Hm_lvt_419cfa1cc17e2e1dc6d4f431f8d19872=1635582160,1635582473; Hm_lpvt_419cfa1cc17e2e1dc6d4f431f8d19872=1635585796',
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    }
    response = requests.get(url, headers=headers).content.decode('utf-8')  #发送网络请求
    soup = BeautifulSoup(response, "lxml")  #解析网页
    list_a = soup.select('.main-ednav-nav > dl > dt > a')  # 找到一页报纸的所有详细链接（每一版）
    urlList = []
    for i in list_a[1:]:
        urlList.append(urlCut + i['href'])  #截取详细url地址
    urlList.append(url) #添加到一起 用于后边循环
    # 请求链接列表获取 每个新闻链接
    singleList = []  #每一页的地址
    for iii in urlList: #筛选出单个
        res = requests.get(iii, headers=headers).content.decode('utf-8')  #请求每一个详细的链接
        s = BeautifulSoup(res, "lxml") #解析单个网页
        list_b = s.select('.main-ed-articlenav-list > li > a')  # 每一页数据的列表
        for k in list_b:
            singleList.append(urlCut + k['href'])
    for kkk in singleList:
        total += 1  # 请求一次链接 总数加1
        print('当前查询的链接————————————————>>>>>', kkk)
        re = requests.get(kkk, headers=headers).content.decode('utf-8')
        so = BeautifulSoup(re, "lxml")  #解析页面
        list_c = so.select('.main-article-con > founder-content > p')  # 每一页数据的列表
        strAll = '' #拼接每一篇文章所有的文字
        for l in list_c:
            strAll += str(l.string) #组合到一起
        # 从三个数组中对比 是否满足条件
        oneFlag = False  #如果满足第一类改为真（如果不满足第一个分类就为假）
        for o in listOne:
            if o in strAll:
                oneFlag = True #
                break
        twoFlag = False #看是否满足第二个分类（不满足就为假，为真才继续判断是否符合下一个）
        if oneFlag:
            for t in listTwo:
                if t in strAll:
                    twoFlag = True
                    break
        threeFlag = False  #是否满足第三个
        if twoFlag:
            for th in listThree:
                if th in strAll:
                    threeFlag = True
                    break
        # 满足三个条件都满足的
        if threeFlag:
            number += 1 #（三个都满足 记录次数加1）
    allInfo.append([data, number, total])  # 返回满足条件的 日期  数量（用于存数据------>>单个信息）
    return allInfo

if __name__ == '__main__':
    saveInfo = []
    for i in getAllDayPerYear(2016): #调用日期的函数 请求每一天的日报
        url = 'https://zjrb.zjol.com.cn/html/' + i[:7] + '/' + i[8:] + '/node_18.htm'
        urlCut = 'https://zjrb.zjol.com.cn/html/' + i[:7] + '/' + i[8:] + '/'
        allInfo = getShowCount(i, url, urlCut)   #表格每一条数据
        saveInfo.extend(allInfo)  # 添加（最后存表）
        df = pd.DataFrame(saveInfo)  # 将获取到的所有数据生成表格
        df.columns = ['日期', '满足条件', '文章总数']  #设置表格的表头
        df.to_csv('测试.csv', encoding='utf_8_sig')  #存储表格
        # saveExcel('测试.xls',saveInfo)
