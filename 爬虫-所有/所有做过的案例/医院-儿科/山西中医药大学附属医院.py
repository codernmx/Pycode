import datetime
import random
import re
import time

import xlwt
import requests
from bs4 import BeautifulSoup


class getInfo:
    def __init__(self, url,ke = ''):
        # 分析网页，并获取网页文件
        headers = {
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML, likeGecko) Chrome/80.0.3987.163Safari/537.36"
        }
        response = requests.get(url, headers=headers).content.decode('utf-8')
        self.url = url
        self.ke = ke
        self.web = response
        self.soup = BeautifulSoup(self.web, "lxml")

    # 获得医生信息
    def getDocInfo(self):
        soup = self.soup
        # 1 唯一标识  0
        _id = self.url
        # 2 采集时间 0
        grab_date = datetime.datetime.now().strftime('%Y-%m-%d')
        # 3 标识 N 0
        extracted = "N"
        # 4 网站名 0
        regular = re.compile(r'[a-zA-Z]+://[^\s]*.com|.cn]')
        website = ''.join(re.findall(regular, self.url))

        # 5 医院名
        doctor_hospital = soup.select("title")[0].string[-11:]

        # 6 医生链接 0
        url = self.url

        # 7 医生姓名
        doctor_name = soup.select("h1")[0].string
        # 8 医生所在科室
        doctor_department = self.ke
        # doctor_department = soup.select("h1")[0].string
        # 9 医生照片，必须是有人像的照片，若遇到官网有统一的非人像链接，可以将其置空。
        doctor_img = website + soup.select("img")[0]["src"][5:]
        # 10 医生性别
        doctor_sex = '男'
        # 11 医生的主要著作
        works = [
            "《" + item + "》"
            for item in re.findall(re.compile("《(.*?)》"), str(soup))
        ]
        doctor_works = "，".join(works)

        # 12 医生经历
        experience = soup.select("#content > p")[0].string
        #  13 医生的社会任职
        social_position = ','.join([
            str(item.string).replace(" ", "")
            for item in soup.select("#content > p")
        ])
        # 14 医生的主要成果（成就）
        doctor_achievement = ""
        # 15 医生的学历
        education = ""
        # 16 医生专业
        doctor_major = ""
        # 17 医生的职务、职称，若网站中两个都出现了，需要自行拼接到这个字段当中
        doctor_title = soup.select("#content > p")[0].string
        # 18 医生擅长
        if len(soup.select("#content > p")) > 1:
            skill = soup.select("#content > p")[1].string
        else:
            skill = soup.select("#content > p")[0].string
        # 19 医生的简介
        doctor_info = soup.select("#content > p")[0].string

        return [
            _id, grab_date, extracted, website, doctor_hospital, url,
            doctor_name, doctor_department, doctor_img, doctor_sex,
            doctor_works, experience, social_position, doctor_achievement,
            education, doctor_major, doctor_title, skill, doctor_info
        ]


# 存储到excel
def saveExcel(file_path, doctorInfo):
    f = xlwt.Workbook(encoding='utf-8')
    sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)  # 创建sheet
    info = [
        '_id', 'grab_date', 'extracted', 'website', 'doctor_hospital', 'url',
        'doctor_name', 'doctor_department', 'doctor_img', 'doctor_sex',
        'doctor_works', 'experience', 'social_position', 'doctor_achievement',
        'education', 'doctor_major', 'doctor_title', 'skill', 'doctor_info'
    ]

    for col in range(0, 19):
        sheet1.write(0, col, info[col])

    # 将数据写入第 i 行，第 j 列
    row = 1
    for data in doctorInfo:
        for j in range(len(data)):
            sheet1.write(row, j, data[j])
        row = row + 1
    f.save(file_path)


# 获得所有医生url
def getAllUrl(url, tag_rule):
    urlList = []
    doc = getInfo(url,'')
    soup = doc.soup
    url_list_doc = soup.select(tag_rule)
    # ke = soup.select(tag_rule).string
    web_f = re.compile(r'[a-zA-Z]+://[^\s]*.com|.cn]')
    web_name = ''.join(re.findall(web_f, url))
    for item in url_list_doc:
        ke = item.string
        url_item = str(web_name) + item['href']  #单个科室链接
        response = requests.get(url_item).content.decode('utf-8')
        soup = BeautifulSoup(response, "lxml")
        url_list_doc = soup.select('#doctor_list > li > figure > a')
        for ite in url_list_doc:
            url = 'http://www.sxzyfy.com/doctor/e' + str(ite['href'])[18:27] + '/'
            urlList.append({
              "url":url,
              "ke":ke
            })
    return urlList


# 过滤条件
def setFilter():
    doc_filter = []
    return doc_filter


if __name__ == "__main__":
    all_doctor = []
    rule = ".mt_r_b > dd > a"
    url_list = getAllUrl("http://www.sxzyfy.com/section/index/", rule)
    print(len(url_list))
    i = 0
    for item in url_list:
        doctor = getInfo(item['url'],item['ke'])
        # print(doctor.getDocInfo())
        print(i)
        i += 1
        all_doctor.append(doctor.getDocInfo())
        tem = random.random()
        time.sleep(tem)

    # 存储到excel
    saveExcel("山西中医药大学附属医院.xls", all_doctor)