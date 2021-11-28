import datetime
import re

import requests
from bs4 import BeautifulSoup


class getInfo:
    def __init__(self, url):
        # 分析网页，并获取网页文件
        headers = {
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML, likeGecko) Chrome/80.0.3987.163Safari/537.36"
        }
        response = requests.get(url, headers=headers).content.decode('utf-8')
        self.url = url
        self.web = response
        self.soup = BeautifulSoup(self.web, "lxml")

    def getDocInfo(self):
        soup = self.soup
        # 1 唯一标识
        _id = self.url
        # 2 采集时间
        grab_date = datetime.datetime.now().strftime('%Y-%m-%d')
        # 3 标识 N
        extracted = "N"
        # 4 网站名
        regular = re.compile(r'[a-zA-Z]+://[^\s]*.com|.cn]')
        website = ''.join(re.findall(regular, self.url))

        # 5 医院名
        doctor_hospital = soup.select(".phoneNav > a")[0]['title']

        # 6 医生链接
        url = self.url

        # 7 医生姓名
        doctor_name = soup.select(".doc_pic")[0]["alt"]
        # 8 医生所在科室
        doctor_department = soup.select(".pic-name")[0].string
        # 9 医生照片，必须是有人像的照片，若遇到官网有统一的非人像链接，可以将其置空。
        doctor_img = website + soup.select(".doc_pic")[0]["src"]
        # (10)
        # doctor_sex：医生性别
        # (11)
        # doctor_works：医生的主要著作
        # (12)
        # experience：医生经历
        # (13)
        # social_position：医生的社会任职
        # (14)
        # doctor_achievement：医生的主要成果（成就）
        # (15)
        # education：医生的学历
        # (16)
        # doctor_major：医生专业
        # (17)
        # doctor_title：医生的职务、职称，若网站中两个都出现了，需要自行拼接到这个字段当中
        # (18)
        # skill：医生擅长
        # (19)
        # doctor_info：医生的简介

        print(doctor_img)
        print(doctor_name)
        return soup


doctor = getInfo('https://www.bch.com.cn/Html/Doctors/Main/Index_1098.html')
doctor.getDocInfo()