
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.header import Header
# 第三方 SMTP 服务
mail_host="smtp.qq.com"  #设置服务器
mail_user="nmxgzs@foxmail.com"    #用户名
mail_pass=""   #口令
sender = 'nmxgzs@foxmail.com'
receivers = 'nmxgzs@foxmail.com' # 接收邮件，可设置为你的QQ邮箱或者其他邮箱


url = f"http://weathernew.pae.baidu.com/weathernew/pc?query=%E9%87%8D%E5%BA%86%E5%A4%A9%E6%B0%94&srcid=4982&city_name=%E9%87%8D%E5%BA%86&province_name=%E9%87%8D%E5%BA%86"
resp = requests.get(url=url,verify=False)
resp.encoding = 'gb2312'
soup = BeautifulSoup(resp.content,"html.parser")
tag = soup.find('script').string[90:109]
tag = '今日重庆：'+ tag 

message = MIMEText(tag, 'plain', 'utf-8')
message['From'] = Header("DayBreak", 'utf-8')
# message['To'] =  Header("nmxgzs", 'utf-8')
subject = '柠檬心工作室每日天气预报'
message['Subject'] = Header(subject, 'utf-8')
try:
		smtpObj = smtplib.SMTP() 
		smtpObj.connect(mail_host, 587)    # 25 为 SMTP 端口号
		smtpObj.login(mail_user,mail_pass)  
		smtpObj.sendmail(sender, receivers, message.as_string())
		print ("邮件发送成功")
except smtplib.SMTPException:
		print ("Error: 无法发送邮件")