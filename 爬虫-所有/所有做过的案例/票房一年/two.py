import arrow
import datetime
import json
import random
import re
import time
from urllib.parse import urlencode
import xlwt
import requests

url = 'https://endata.com.cn/enlib-api/api/cinema/getcinemaboxoffice_day_list.do;JSESSIONID=e6fab563-ee5d-40f6-ae84-fa07c6177602'
headers = {
    "Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    "Cookie": "SECKEY_CID2=dd3c4b0d23dffb65a21357eeb3590cdccc77ee33; BMAP_SECKEY2=e7ccd76a71cca7384bc9d56993ddbed2e19bbff4744b85e39bb3d65be30e7613e76ae0b8689ae7f5bb14207898aef6950e69432a9314fa542a239fa64bfb5b45402ef2007702df7fe2b519ab0b481d9ea6c827f3e3a0b16228d15c808924f9df4cc16baa222e9dd3183e44e6e7e0221594aeb7e6ea4c6929252df52369a815d8b1a01740acabe8aa91428d68229138ae07a5b3f7057d461b9145ae266028bdfc55b351bd2b75011f849878b41ed0f2003f308398779bf90da0c6abdeae319c0443f09fc2a2e6dbe9ae6a1a5ebaa532ca6b878aa1d56cc08a135599aa1b43a869019d0cf9d455a8166049b4bd2b52c1d4; BMAP_SECKEY2=e7ccd76a71cca7384bc9d56993ddbed2e19bbff4744b85e39bb3d65be30e7613e76ae0b8689ae7f5bb14207898aef6950e69432a9314fa542a239fa64bfb5b45402ef2007702df7fe2b519ab0b481d9ea6c827f3e3a0b16228d15c808924f9df4cc16baa222e9dd3183e44e6e7e0221594aeb7e6ea4c6929252df52369a815d87cace4ed8ad61e4ccc2a2b11da9793a655a0c3cd12da73868a15f9f4b2d4abcc5c99cc705bf175e33a5feaa229a8dd067682dc9837b75609262dc5f76b481145471e413d55ddf10ef22d6f463b01dfd443dbdc5f2d4f2a3d4baa3768f1d846f946b583c1328569f6a849bfdcf61a90ef; MEIQIA_TRACK_ID=1zcdsAgM0TSsyGhC7T3uZz1nqLl; route=4b4bdd0e2cdff4f8f9f520f338860b7c; MEIQIA_VISIT_ID=20McxbBZGciw6GFTnSX13e4SF8M",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}


def isLeapYear(years):
    '''
    通过判断闰年，获取年份years下一年的总天数
    :param years: 年份，int
    :return:days_sum，一年的总天数
    '''
    # 断言：年份不为整数时，抛出异常。
    assert isinstance(years, int), "请输入整数年，如 2018"
    if ((years % 4 == 0 and years % 100 != 0) or (years % 400 == 0)):  # 判断是否是闰年
        # print(years, "是闰年")
        days_sum = 366
        return days_sum
    else:
        # print(years, '不是闰年')
        days_sum = 365
        return days_sum


def getAllDayPerYear(years):
    '''
    获取一年的所有日期
    :param years:年份
    :return:全部日期列表
    '''
    start_date = '%s-1-1' % years
    a = 0
    all_date_list = []
    days_sum = isLeapYear(int(years))
    print()
    while a < days_sum:
        b = arrow.get(start_date).shift(days=a).format("YYYY-MM-DD")
        a += 1
        all_date_list.append(b)
    # print(all_date_list)
    return all_date_list


# 存表格
def saveExcel(file_path, Info):
    f = xlwt.Workbook(encoding='utf-8')
    sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)  # 创建sheet
    info = [
        '排名', '影院名称', '票房(万)', '城市', '场次', '平均票价',
        '场均人次', '上座率', '线上票房占比'
    ]
    for col in range(0, len(info)):
        sheet1.write(0, col, info[col])
    # 将数据写入第 i 行，第 j 列
    row = 1
    for data in Info:
        for j in range(len(data)):
            sheet1.write(row, j, data[j])
        row = row + 1
    f.save(file_path)


# 获取excel数据
def getExcelInfo(date):
    all_info = []
    data = {
        "r": '0.9050680994611333',
        "columnslist": '100,101,99,102,122,103,108,109,117',
        "datetype": 'Day',
        "date": str(date),
        "sdate": str(date),
        "edate": str(date),
        "bserviceprice": 0,
        "citylevel": '',
        "cityregion": '',
        "provinceid": '',
        "cityid": '',
        "areaid": '',
        "lineid": '',
        "companyid": '',
        "pageindex": 1,
        "pagesize": 20000,
        "order": 102,
        "ordertype": "desc",
    }
    redata = urlencode(data)
    response = requests.post(url, headers=headers, data=redata).content.decode('utf-8')
    print(response)
    data = json.loads(response)['data']['table1']
    for i in data:
        Irank = i['Irank']
        CinemaName = i['CinemaName']
        BoxOffice = float(i['BoxOffice']) / 10000
        CityName = i['CityName']
        ShowCount = i['ShowCount']
        AvgBoxOffice = i['AvgBoxOffice']
        AvgShowAudienceCount = i['AvgShowAudienceCount']
        Attendance = i['Attendance']
        all_info.append(
            [Irank, CinemaName, BoxOffice, CityName, ShowCount, AvgBoxOffice, AvgShowAudienceCount, Attendance])
    return all_info


if __name__ == '__main__':
    # years = "2001"
    # years = int(years)
    # # 通过判断闰年，获取一年的总天数
    # days_sum = isLeapYear(years)
    # 获取一年的所有日期
    all_date_list = getAllDayPerYear("2016")
    # print(all_date_list)
    for item in all_date_list:
        all_info = getExcelInfo(str(item))
        print(item)
        saveExcel('E:/PycharmCode/票房/票房/2017/' + str(item) + ".xls", all_info)
        time.sleep(random.randint(60, 80))

