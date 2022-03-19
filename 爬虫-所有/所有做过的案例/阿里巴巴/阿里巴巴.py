# @Time : 2021/11/16 20:44
# @Author : VX:Until_Day_Break
# @SoftWare : PyCharm
import json
import random
import xlwt
import requests
import math
import time
from bs4 import BeautifulSoup


# 存表格
def saveExcel(file_path, Info):
    f = xlwt.Workbook(encoding='utf-8')
    sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)  # 创建sheet
    # id, fkmz, jdcy, searchKeyword, buyerCountry, totalVisitSellerCnt, visitPv, staySecondW, totalVisitPv,
    # totalMcFbCnt, totalMcSellerCnt, logTime, subject, realUrl, imageURL, staySecond]
    info = [
        'ID', '访客名称', '进店词语', '偏好词语', '国家', '浏览供应商',
        '浏览次数', '停留时长s', '总浏览量', '询盘行为', '日期', '产品', '产品url', '图片地址', '停留时长'
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


def getDetailInfo(header, buyerCookieId, info):
    print(buyerCookieId, '_____________>>>', info)
    url = 'https://hz-mydata.alibaba.com/self/.json?action=CommonAction&iName=getVisitorDetails&0.6535293780922804&ctoken=1bpru67dfwrn5&dmtrack_pageid=9fdf38f02101283c61979d3417d383e15941f68384&_bx-v=1.1.21'
    datas = {
        "statisticsType": 'day',
        "selected": 0,
        "startDate": '2021-10-21',
        "endDate": '2021-11-20',
        "orderBy": '',
        "orderModel": '',
        "pageSize": 5,
        "pageNO": 1,
        "buyerCookieId": buyerCookieId,
        "statDate": info['logTime'],
    }
    res = requests.post(url, headers=header, data=datas).content.decode('utf-8')
    detailValue = json.loads(res)['value']['data']
    print(len(detailValue),'--------->len详细',detailValue)
    allVpList = []
    for i in detailValue:
        if 'visitorId' in info:
            id = info['visitorId']  # ID
        else:
            id = ''
        fkmz = ''  # 访客名字
        jdcy = ''  # 进店词语
        if 'serKeywords' in info:
            serKeywords = info['serKeywords']  # 偏好词语
        else:
            serKeywords = ''
        if 'buyerCountry' in info:
            buyerCountry = info['buyerCountry']  # 国家
        else:
            buyerCountry = ''
        if 'totalVisitSellerCnt' in info:
            totalVisitSellerCnt = info['totalVisitSellerCnt']  # 总浏览供应商
        else:
            totalVisitSellerCnt = ''
        if 'visitPv' in info:
            visitPv = info['visitPv']  # 浏览次数
        else:
            visitPv = ''
        if 'staySecond' in info:
            staySecondW = info['staySecond']  # 停留时长
        else:
            staySecondW = ''
        if 'totalVisitPv' in info:
            totalVisitPv = info['totalVisitPv']  # 总浏览量
        else:
            totalVisitPv = ''
        if 'totalMcFbCnt' in info:
            totalMcFbCnt = info['totalMcFbCnt']  # 发起
        else:
            totalMcFbCnt = ''
        if 'totalMcSellerCnt' in info:
            totalMcSellerCnt = info['totalMcSellerCnt']  # 供应商询盘
        else:
            totalMcSellerCnt = ''
        if totalMcFbCnt != 0 and totalMcSellerCnt != 0:
            totaCntStr = '对' + str(totalMcFbCnt) + '供应商发起' + str(totalMcSellerCnt) + '个询盘'
        else:
            totaCntStr = ''
        if 'logTime' in i:
            logTime = i['logTime']  # 访问时间（日期加时间）
        else:
            logTime = ''
        if 'subject' in i:
            subject = i['subject']  # 标题（产品）
        else:
            subject = ''
        if 'realUrl' in i:
            realUrl = i['realUrl']  # 链接（url）
        else:
            realUrl = ''
        if 'imageURL' in i:
            imageURL = i['imageURL']  # 图片（img）
        else:
            imageURL = ''
        if 'staySecond' in i:
            staySecond = i['staySecond']  # 停留时间
        else:
            staySecond = ''
        allVpList.append(
            [id, fkmz, jdcy, serKeywords, buyerCountry, totalVisitSellerCnt, visitPv, staySecondW, totalVisitPv,
             totaCntStr, logTime, subject, realUrl, imageURL, staySecond])
        time.sleep(random.randint(1, 5))
    return allVpList


url = 'https://hz-mydata.alibaba.com/self/.json?action=CommonAction&iName=getVisitors&isVip=true&0.6876415980349655&ctoken=81ifk2_y20fh&dmtrack_pageid=7d54b1f70b01bdaf619bac5317d48193acb1e95da0&_bx-v=1.1.21'
headers = {
    "content-type": 'application/x-www-form-urlencoded; charset=UTF-8',
    "cookie": 'ali_apache_id=11.177.41.34.1637062389788.446124.6; t=ac16a38aef0a66dae25b5dc7bde08b82; xman_i=aid=2210923912176; cna=d+ruGYmBSy0CAWpb0xEN10xR; sc_g_cfg_f=sc_b_locale=en_US; xman_us_f=x_locale=zh_CN&x_l=1&last_popup_time=1637159421724&x_user=CN|null|null|cgs|251119114&no_popup_today=n; cbc=G94B6CD73AC6451E2FDA479F0D2252D800A26D4C4E82BC48276; umdata_=GF2D5255761390A3B8308101975D95E4FF1A4F2DB4CE8F4A7A6; acs_usuc_t=acs_rt=a68c0aa6b83c4486aee0bd90b45e9d0c; cookie2=10515b5cb7f5c41b07968414257c3db7; _tb_token_=e3e3b545736bd; _samesite_flag_=true; xlly_s=1; _hvn_login=4; xman_us_t=ctoken=81ifk2_y20fh&l_source=alibaba&x_user=Y6eJvgZ3FZq5F/48LlhmwNNNHtK1gMvuhanYCfaGDS4=&x_lid=amoydk&sign=y&need_popup=y; intl_locale=zh_CN; intl_common_forever=/7or4isqFu1oL6uoJhr/80r6ghhbeic91BrkRBYGlaUkqgaD/kfoag==; xman_f=uxDFlWboy46CHM4SRcMRdoaaC5Jzkxat/94QVlOIfP6DLURpqbbgo1siVMs4CmQUz5kn9qNGfmX1IhHXpWgN/0A3T9MZgC8HDRL+lw2FHGA7pcePizbfoFUlRbjgn19H3s9aMluvXpr7q8G8p8x9ha13V285pr2ZQSQX2SzxZgvnauSDkruJnlCxHFL6Bh2GUnife5Gckr3RPw2IBK3DWKmxY2Z9ppXDxoRhZAcunmLV+lDF+4lo/FAtV4AyhM1Z35JGwVuqQOy35is1UW8gPOxkreu87EIDusu6Rs+dfvWoHJ4FPhPXGfmlxtKZ2aWDEevmXUB8uVub4IGwOp5sjsKq6drHnlzeAONQKD3z6VASMcmA4yT+sSR/jX8UaX73TeDqnhkTeZg=; ali_apache_tracktmp=W_signed=Y; _m_h5_tk=97af2e8dcbf6819c636689a044ca2017_1637598333202; _m_h5_tk_enc=89cb7f77499fc5440100604e420a39d7; XSRF-TOKEN=d9b4908d-e6b0-4015-9e8c-41e93ff76836; ali_apache_track=ms=|mt=3|mid=amoydk; xman_t=Z3Rs7QyQMDn+tCq4V6T8tgYb2AxiyJlqH1YIPdK14R9lwSWFts15dkWShC4iz10OZ/vqg1T/s6ZEKgA5GHEw9p5+Pp4Mj8tl12QtkAy8kCOPzrkVML2ZQ/yXJ+AvaSe3rWcYBuAyxBFxb7RcWxk61brfr9b8zlwyMh5DFQFqs2AOI0WobSNVwf5qr/ZXyi9f/ndebWl8JLF6CquyaLofOpQ3Otg/cHfaR/7oxy71fpnSqRU1HRbIxyAfkytZds6B23T3oidYJJsOB6KG6tQlzRcdb/NtgPrrfqLBig6WB4WzaXLxSSdPAdfw+7P5tr+uwCtq6NtxZVaR+xjjhKRi9BVDfv2Tu/lyKsdI63BaovhF2oKF/NbcDqtrh+hz4g5rKrtDtLfCAAvRr6A5gd/1LsZoq6t9z3OYuFYwMg9AxFSd4eMheXs9yNh7a07kDtdi+mCBbYMyKBmOryP/L8dPYibXEg0MJfhUyBXiEIjmUqEWmwbPGjIsxkZRTFvaASPvuj1IS/nOOOxObmBqkqhB3U2vnbtWsF0PWa6cMzhvxLoPX1CTep+p57EXdk/ms9+YyD6bisZw5k3LPXbOpe5c6C53/7yOBeJsNEOFxsvlCVSDbqVy0HaJsxNnviYnagcz2SYPWVFyPO9SrLtOI+UIO9ex+LBLgEOO; csg=491fd614; l=eBMpwHcIgpJG5cqFBO5Churza779yIRf1lVzaNbMiInca1kfTUQ5cOCdI2o27dtjgt5A6etyzAmWiRnW7v4LRx6sI_oCDNsjuBJ6Re1..; isg=BDIyagBAh9Y9mLv_QCK-YOw8g3gUwzZd4yo4MfwL6uX2j9GJ5FBcbcGpfyszxK71; tfstk=cN1GBi2ldOJ6jpphF5O1J_ZpsMZdZtwwfs5FT_WKCZiRPn1FijDEUCeL-hE7bx1..',
    "origin": 'https://data.alibaba.com',
    "referer": 'https://data.alibaba.com/',
    # "sec-ch-ua": "Microsoft Edge";v="95", "Chromium";v="95", ";Not A Brand";v="99",
    "sec-ch-ua-mobile": '?0',
    "sec-ch-ua-platform": "Windows",
    "sec-fetch-dest": 'empty',
    "sec-fetch-mode": 'cors',
    "sec-fetch-site": 'same-site',
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.53'
}
datas = {
    "orderBy": '',
    "orderModel": '',
    "pageSize": 10,
    "pageNO": 1,
    "statisticsType": 'day',
    "selected": 0,
    "startDate": '2021-10-21',
    "endDate": '2021-11-20',
    "searchKeyword": '',
    "buyerRegion": '',
    "buyerCountry": '',
    "subMemberSeq": '',
    "isMcFb": 'false',
    "isAtmFb": 'false',
    "mailable": 'false',
    "mailed": 'false',
    "hasRemarks": 'false',
    "statisticType": 'os',
    "desTime": '1637590431845',
}

for j in range(1, 5):
    all_info = []
    print('第' + str(j) + '页')
    ts = time.time()
    ts = math.floor(ts * 1000)

    datas['pageNO'] = j
    # datas['desTime'] = str(ts-1000)
    print(datas['pageNO'],'------------>>>pageNO')
    print(datas['desTime'],'------------>>>desTime')
    res = requests.post(url, headers=headers, data=datas).content.decode('utf-8')
    configData = json.loads(res)['value']['data']
    for i in configData:
        singInfo = getDetailInfo(headers, i['buyerCookieId'], i)
        all_info.extend(singInfo)
    time.sleep(random.randint(5, 15))
    saveExcel('./结果/'+str(j) + '.xls', all_info)
