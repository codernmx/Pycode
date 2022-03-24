"""
@ProjectName: DXY-2019-nCov-Crawler
@FileName: crawler.py
@Author: Jiabao Lin
@Date: 2020/1/21
"""
from bs4 import BeautifulSoup
from service.db import DB
from service.userAgent import user_agent_list
from service.nameMap import country_type_map, city_name_map, country_name_map, continent_name_map
import re
import json
import time
import random
import logging
import requests


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)


class Crawler:
    def __init__(self):
        self.session = requests.session()
        self.db = DB()
        self.crawl_timestamp = int()

    def run(self):
        while True:
            self.crawler()
            time.sleep(60)

    def crawler(self):
        while True:
            self.session.headers.update(
                {
                    'user-agent': random.choice(user_agent_list)
                }
            )
            self.crawl_timestamp = int(time.time() * 1000)
            try:
                r = self.session.get(url='https://ncov.dxy.cn/ncovh5/view/pneumonia')
            except requests.exceptions.ChunkedEncodingError:
                continue
            soup = BeautifulSoup(r.content, 'lxml')
            area_information = re.search(r'\[(.*)\]', str(soup.find('script', attrs={'id': 'getAreaStat'})))
            if area_information:
                self.area_parser(area_information=area_information)
            break
            #
            # abroad_information = re.search(r'\[(.*)\]', str(soup.find('script', attrs={'id': 'getListByCountryTypeService2true'})))
            # if abroad_information:
            #     self.abroad_parser(abroad_information=abroad_information)


        logger.info('Successfully crawled.')

    # def province_parser(self, province_information):
    #     provinces = json.loads(province_information.group(0))
    #     for province in provinces:
    #         province.pop('id')
    #         province.pop('tags')
    #         province.pop('sort')
    #         province['comment'] = province['comment'].replace(' ', '')
    #
    #         if self.db.find_one(collection='DXYProvince', data=province):
    #             continue
    #
    #         province['provinceEnglishName'] = city_name_map[province['provinceShortName']]['engName']
    #         province['crawlTime'] = self.crawl_timestamp
    #         province['country'] = country_type_map.get(province['countryType'])
    #
    #         self.db.insert(collection='DXYProvince', data=province)

    def area_parser(self, area_information):
        area_information = json.loads(area_information.group(0))
        for area in area_information[-1:]:
            area['comment'] = area['comment'].replace(' ', '')

            # Because the cities are given other attributes,
            # this part should not be used when checking the identical document.
            #cities_backup = area.pop('cities')

            # if self.db.find_one(collection='DXYArea', data=area):
            #     continue

            # If this document is not in current database, insert this attribute back to the document.
            #area['cities'] = cities_backup
            area['cities'] = ''
            area['countryName'] = '中国'
            area['continentName'] = '亚洲'
            #
            # for city in area['cities']:
            #     if city['cityName'] != '待明确地区':
            #         try:
            #             city['cityEnglishName'] = city_name_map[area['provinceShortName']]['cities'][city['cityName']]
            #         except KeyError:
            #             print(area['provinceShortName'], city['cityName'])
            #             pass
            #     else:
            #         city['cityEnglishName'] = 'Area not defined'

            area['updateTime'] = self.crawl_timestamp
            #省名
            print(area['provinceName'])
            #当前确诊
            print(area['currentConfirmedCount'])
            # 总确诊数 = 当前确诊+治愈+死亡
            print(area['confirmedCount'])
            # 疑似数
            print(area['suspectedCount'])
            # 治愈数
            print(area['curedCount'])
            # 死亡数
            print(area['deadCount'])
            print(area)
            #self.db.insert(collection='DXYArea', data=area)

    def abroad_parser(self, abroad_information):
        countries = json.loads(abroad_information.group(0))
        for country in countries[0:10]:
            try:
                country.pop('id')
                country.pop('tags')
                country.pop('sort')
                # Ding Xiang Yuan have a large number of duplicates,
                # values are all the same, but the modifyTime are different.
                # I suppose the modifyTime is modification time for all documents, other than for only this document.
                # So this field will be popped out.
                country.pop('modifyTime')
                # createTime is also different even if the values are same.
                # Originally, the createTime represent the first diagnosis of the virus in this area,
                # but it seems different for abroad information.
                country.pop('createTime')
                country['comment'] = country['comment'].replace(' ', '')
            except KeyError:
                pass
            country.pop('countryType')
            country.pop('provinceId')
            country.pop('cityName')
            # The original provinceShortName are blank string
            country.pop('provinceShortName')
            # Rename the key continents to continentName
            country['continentName'] = country.pop('continents')
            #
            # if self.db.find_one(collection='DXYArea', data=country):
            #     continue

            country['countryName'] = country.get('provinceName')
            country['provinceShortName'] = country.get('provinceName')
            country['continentEnglishName'] = continent_name_map.get(country['continentName'])
            country['countryEnglishName'] = country_name_map.get(country['countryName'])
            country['provinceEnglishName'] = country_name_map.get(country['countryName'])

            country['updateTime'] = self.crawl_timestamp
            print(country)
            #self.db.insert(collection='DXYArea', data=country)

if __name__ == '__main__':
    crawler = Crawler()
    crawler.run()
