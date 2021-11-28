# @Time : 2021/11/27 11:02
# @Author : VX:Until_Day_Break
# @SoftWare : PyCharm
# 宁波租房房价爬虫类
import re
import time

import bs4
import requests


class nignbo_housing_price_crawler:
    def get_crawler_infomation(self, url):
        # 一定要设置headers信息
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34'
        }

        cook = {
            'Cookie': 'sessid=B31B086A-F818-4E5E-1D95-0F7C3F081501; aQQ_ajkguid=05BC5527-8D20-1BA0-2BAE-731815D83551; ctid=20; twe=2; obtain_by=2; id58=CrIIZ2Ghn+eqV1onA80+Ag==; _ga=GA1.2.2047045223.1637982184; _gid=GA1.2.2056475377.1637982184; _gat=1; wmda_uuid=b14c7b1baeccbdd512b789fcadf9f3f4; wmda_new_uuid=1; wmda_session_id_6289197098934=1637982184328-94629166-78a0-979d; wmda_visited_projects=%3B6289197098934; 58tj_uuid=43fc0c1b-e38b-429d-9375-27c7f3a5ab8c; new_session=1; init_refer=https%253A%252F%252Fwww.baidu.com%252Flink%253Furl%253DQyacoD0IIttl7rsBCsuBgv2p4xVcHNExspo0TG-5WLxTEQlUDWMDTnZ95m13yOHW%2526wd%253D%2526eqid%253Db62293b100004da00000000661a19fe1; new_uv=1; als=0; xxzl_cid=247bd8db7c4243ed847d6657b3de6814; xzuid=0568376e-028a-43c3-a9eb-6aae29c448b8'  # 这里的Cookie信息根据自己浏览器具体情况来设置
        }

        resp = requests.get(url, cookies=cook, headers=headers)
        resp.encoding = resp.apparent_encoding
        soup = bs4.BeautifulSoup(resp.text, "lxml")

        # 通过find_all找到所有div元素
        zoom_info = soup.find_all(name="div", class_="zu-itemmod")

        for item in zoom_info:
            # 房屋简介
            zoom_describe = item

            # 房屋超链接
            zoom_link = item.a["href"]

            # 房屋规模、楼层、售楼人信息
            zoom_details_find = item.p.text.strip()
            pat = re.compile(r'[\u4e00-\u9fa50-9]+')
            zoom_details_find_list = pat.findall(zoom_details_find)
            zoom_details_final_result = '-'.join(zoom_details_find_list)

            # 房屋地址
            zoom_address_find = item.find_all(name="address", class_="details-item")[0].text.strip()
            zoom_address_result_list = pat.findall(zoom_address_find)
            zoom_address_final_result = "-".join(zoom_address_result_list)

            # 房屋售价
            zoom_price = item.find_all(name="strong")[0].text

            # 打印爬取信息
            print(zoom_describe, zoom_link, zoom_details_final_result, zoom_address_final_result, zoom_price)

            time.sleep(0.2)
            pass
        pass

    pass


if __name__ == '__main__':
    # 设置url
    url = "https://nb.zu.anjuke.com/fangyuan/yinzhou/p1/"

    # main函数调用方法，传入url参数
    nignbo_housing_price_crawler().get_crawler_infomation(url)

    pass