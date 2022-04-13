#! /usr/bin/python3
# coding=UTF-8

import pymysql
import time

class DBTool:
    def __init__(self, host, port, user, passwd, dbname):
        self.host = host
        self.port = int(port)
        self.user = user
        self.passwd = passwd
        self.dbname = dbname

    def create_connection(self):
        return pymysql.Connect(
            host=self.host,
            port=self.port,
            user=self.user,
            passwd=self.passwd,
            db=self.dbname,
            charset='utf8'
        )


    @staticmethod
    def get_cursor(conn):
        return conn.cursor()

    @staticmethod
    def close_conn(conn, cursor):
        cursor.close()
        conn.close()

    def execute_update(self, sql):
        conn = self.create_connection()
        cursor = self.get_cursor(conn)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 执行sql语句
            conn.commit()
        except:
            conn.rollback()
        self.close_conn(conn, cursor)

    def IsExssit(self, province, cityName):
        sql = "select province, city from confirmedStat where province='%s' and city='%s'"%(province, cityName)
        conn = self.create_connection()
        cursor = self.get_cursor(conn)
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            conn.commit()
            self.close_conn(conn, cursor)
            if len(result) == 0:
                return False
            else:
                return True
        except:
            conn.rollback()
            self.close_conn(conn, cursor)
            print("select error")
            return False

    #def IsExssitService(self, ):

    def save_area_stat(self, area):
        sql_list = []
        province = area['provinceName']
        province_short_name = area['provinceShortName']
        confirmedCount = area['confirmedCount']
        suspectedCount = area['suspectedCount']
        curedCount = area['curedCount']
        deadCount = area['deadCount']
        if self.IsExssit(province, province_short_name):
            sql = "update confirmedStat set confirmedCount=%s, suspectedCount=%s, curedCount=%s, deadCount=%s where province='%s' and city='%s'"%(confirmedCount, suspectedCount, curedCount, deadCount, province, province_short_name)
            sql_list.append(sql)
        else:
            sql = "insert into confirmedStat (province, city, confirmedCount, suspectedCount, curedCount, deadCount) values ('%s', '%s', %s, %s, %s, %s)"%(province, province_short_name, confirmedCount, suspectedCount, curedCount, deadCount)
            sql_list.append(sql)
        for city in area['cities']:
            city_name = city['cityName']
            confirmedCount = city['confirmedCount']
            suspectedCount = city['suspectedCount']
            curedCount = city['curedCount']
            deadCount = city['deadCount']
            if self.IsExssit(province, city_name):
                sql = "update confirmedStat set confirmedCount=%s, suspectedCount=%s, curedCount=%s, deadCount=%s where province='%s' and city='%s'"%(confirmedCount, suspectedCount, curedCount, deadCount, province, city_name)
                sql_list.append(sql)
            else:
                sql = "insert into confirmedStat (province, city, confirmedCount, suspectedCount, curedCount, deadCount) values ('%s', '%s', %s, %s, %s, %s)"%(province, city_name, confirmedCount, suspectedCount, curedCount, deadCount)
                sql_list.append(sql)
        for sqls in sql_list:
            print(sqls)
            self.execute_update(sqls)

    def check(self):
        sql = "select id from pushService"
        conn = self.create_connection()
        cursor = self.get_cursor(conn)
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            conn.commit()
            self.close_conn(conn, cursor)
            if len(result) > 4:
                return True
            else:
                return False
        except:
            conn.rollback()
            self.close_conn(conn, cursor)
            print("select error")
            return False

    def clean(self):
        if self.check():
            sql = "delete from pushService where id = id"
            self.execute_update(sql)
        else:
            print("not need to clean")

    def save_time_line_service(self, service):
        self.clean()
        pubDate = int(service['pubDate'])/1000
        timeArray = time.localtime(pubDate)
        pubdate = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        title = service['title']
        summary = service['summary']
        infoSource = service['infoSource']
        sourceUrl = service['sourceUrl']
        pubDateStr = service['pubDateStr']
        sql = "insert into pushService (pushDateStr, title, summary, infoSource, sourceUrl, pushDate)VALUES('%s', '%s', '%s', '%s', '%s', '%s')"%(pubDateStr, title, summary, infoSource, sourceUrl, pubdate)
        print(sql)
        self.execute_update(sql)





