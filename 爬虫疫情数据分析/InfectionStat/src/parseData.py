#! /usr/bin/python3
# coding = UTF-8


import json
from dbTool import DBTool

# 确认数目 可疑数目 治愈数目 死亡数目


class ParseTool:
    def __init__(self):
        self.dbtool = DBTool("127.0.0.1", 3306, "root", "ln579683", "stat")

    def parse_and_save(self, json_str, id_name):
        object_value = json.loads(json_str)
        print(" =====> start to parse script id equals : ", end="")
        print(id_name)
        if id_name == "getListByCountryTypeService1":
            for province in object_value:
                pass
        elif id_name == "getAreaStat":
            for province in object_value:
                self.dbtool.save_area_stat(province)
        elif id_name == "getTimelineService":
            print(len(object_value))
            for service in object_value:
                self.dbtool.save_time_line_service(service)
        else:
            pass