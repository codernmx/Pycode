from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import requests
from lxml import etree

if __name__ == '__main__':
    driver = webdriver.Chrome(r'chromedriver.exe')
    # driver = webdriver.Chrome()
    driver.get("https://hotel.qunar.com")

    pass
    # 选取城市
    # toCity = driver.find_element_by_xpath("//input[@tabindex='1']")  # 用xpath定位到城市的输入框
    # toCity.clear()  # 清除输入框原本的数据
    # toCity.send_keys("上海")  # 输入上海
    # toCity.send_keys(Keys.TAB)  # 输入TAB键
    time.sleep(2)

    # 选取开始日期
    checkInDate = driver.find_element_by_xpath("//input[@tabindex='2']")
    checkInDate.click()
    checkInDate.send_keys(Keys.CONTROL, "a")
    checkInDate.send_keys(Keys.DELETE)
    checkInDate.send_keys("2021-12-07")

    # 选取结束日期
    checkOutDate = driver.find_element_by_xpath("//input[@tabindex='3']")
    checkOutDate.click()
    checkOutDate.send_keys(Keys.CONTROL, "a")
    checkOutDate.send_keys(Keys.DELETE)
    checkOutDate.send_keys("2021-12-08")

    # 进行搜索
    search = driver.find_element_by_xpath("//a[@tabindex='5']")
    search.click()
    # 定位到当前页面
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[0])
    new_url = driver.current_url
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
    }
    cookies = {
        'QN1': '00005f00319829df5c702e97',
        'HN1': 'v1b1c8303c8baa2359ebb145a991a74a6f',
        'HN2': 'quzqqcqsngqlz',
        'QN300': 'organic',
        'csrfToken': 'DEKN7FH5xNSuYx6iemD47gRY7vw7IEDD',
        'QN205': 'organic',
        'QN277': 'organic',
        '_i': 'RBTjeCcd1wEx33hRlirI_q1t88ex',
        '_vi': 'cXbZyZ4BEOh4wBX9J1cQYcFSDw7dMnuW6r866eG6uTLr2331x2aHSq2To22tuRaNX98Df2nZGmhz0cLAr7upqmqCbdOQAIdmlWtslBHfje5IuNMQw8EFJdQqcYryaJwEVTuYNxcCm_65Ngnh_WrURpXQy7Hcm3ytO0twTZsG4AtJ',
        'QN269': '4EFF41210D2E11EB8470FA163E9C4675',
        'fid': '13f15660-e827-4b68-b89b-58c65d29e4ba',
        'QN267': '01176786801cc3c53c8',
        'QN271': '0fd118d6-0b4a-4ba3-9005-e8a223f2d096'
    }
    res = requests.get(new_url, headers=headers, cookies=cookies)
    text = etree.HTML(res.text)
    '''content = response.text
    text = parsel.Selector(content)'''
    hotel_name = text.xpath('//div[@class="cont"]/p[@class="name"]/a/text()')
    hotel_gold = text.xpath('//div[@class="operate fl_right"]/p[@class="price_new"]/a/text()')
    hotel_addres = text.xpath('//div[@class="cont"]/p[@class="adress"]/text()')
    # hotel_Dict = list(name +" "+ value +" "+ money + "起" for name, value, money in zip(hotel_name, hotel_gold, hotel_money))
    print(hotel_name)
    print(hotel_addres)
    print(hotel_gold)
