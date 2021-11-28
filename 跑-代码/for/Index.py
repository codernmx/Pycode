import pandas as pd
from selenium import webdriver
import time
from bs4 import BeautifulSoup as bs
#chromedriver需要替换自己的路径
chromedriver = r'C:\Users\B30307\AppData\Local\Google\Chrome\Application\chromedriver'
option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_experimental_option("useAutomationExtension", False)
option.add_argument('lang=zh_CN.UTF-8')
option.add_argument('--dns-prefetch-disable')
option.add_argument('--no-first-run')
# option.add_argument('--incognito')
option.add_argument('--disable-javascript')  # 禁用javascript
option.add_argument('--disable-extensions')  # 禁用拓展
option.add_argument(
    'user-agent= "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"')
browser = webdriver.Chrome(executable_path=chromedriver, options=option)
browser.get("https://edx.dataeye.com/index/home/Shop")
#
ID= browser.find_element_by_xpath('//*[@id="userID"]')
ID.send_keys('15692004254')
Password= browser.find_element_by_xpath('//*[@id="password"]')
Password.send_keys('kuaizi2021')
time.sleep(8)

bussiness=browser.find_element_by_xpath('//*[@id="container"]/div/div[2]/div/ul/li[6]/a')
bussiness.click()
browser.implicitly_wait(20)
time.sleep(5)
list=[]
browser.implicitly_wait(20) #增加隐性等待时间
gettext=browser.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[3]/div/div/div[2]/div/div/div[2]/div/table/tbody/tr[1]/td[1]/a')
print(gettext.text) #去掉括号
total_page = browser.find_elements_by_class_name('_7f3aa282')
next_page = total_page[-1]
total_page = total_page[-2].text
for page in range(1,int(total_page)+1):
    resp = browser.page_source
    soup = bs(resp, 'lxml')
    df = pd.read_html(soup.prettify())
    if page == 1:
        df[0].to_csv('./123.csv',encoding = 'utf_8_sig',mode = 'a')
    df[1].to_csv('./123.csv', encoding='utf_8_sig', mode='a',header = None)
    browser.execute_script("arguments[0].click();", next_page)
    browser.implicitly_wait(20)
    time.sleep(5)
