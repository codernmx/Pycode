# PyCode-Github/天气-邮件
# _*_ coding: utf-8 _*_
import smtplib, requests, json
from email.mime.text import MIMEText
from email.header import Header
from bs4 import BeautifulSoup

# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "nmxgzs@foxmail.com"  # 用户名
mail_pass = "nwnerbeymwhjdiaj"  # 口令
sender = 'nmxgzs@foxmail.com'  # 发送者
receivers = 'nmxgzs@foxmail.com'  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

url = 'https://weather.cma.cn/api/weather/view?stationid=57516'
response = requests.get(url).content.decode('utf-8')
soup = BeautifulSoup(response, "lxml")
daily = json.loads(response)['data']['daily'][0]
now = json.loads(response)['data']['now']

high = daily['high']  # 最高温度
low = daily['low']  # 最低温度
dayText = daily['dayText']  # 天气情况
temperature = now['temperature']  # 当前温度
pressure = now['pressure']  # 压强
humidity = now['humidity']  # 湿度
# 配置邮件体
tag = '小宝贝,今日气温{}-{}摄氏度,{},现在温度为{},压强{},湿度{}'.format(low, high, dayText, temperature, pressure, humidity)
message = MIMEText(tag, 'plain', 'utf-8')
message['From'] = Header("nmxgzs@foxmail.com")
message['To'] = Header("nmxgzs@foxmail.com", 'utf-8')
message['Subject'] = Header("天气预报", 'utf-8')  # 标题

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 587)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("发送邮件错误")
