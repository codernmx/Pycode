import smtplib,urllib, urllib.request,ssl,json
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host="smtp.qq.com"  #设置服务器
mail_user="nmxgzs@foxmail.com"    #用户名
mail_pass="nwnerbeymwhjdiaj"   #口令 
sender = 'nmxgzs@foxmail.com'
receivers = 'nmxgzs@foxmail.com,2953136852@qq.com' # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# 开始请求天气接口
host = 'https://ali-weather.showapi.com'
path = '/area-to-weather'
method = 'GET'
appcode = '76447eef09864d72a68231ae528721cb'
querys = 'area=%E9%87%8D%E5%BA%86&needMoreDay=0&needAlarm=0&need3HourForcast=0&needIndex=0'
url = host + path + '?' + querys
request = urllib.request.Request(url)
request.add_header('Authorization', 'APPCODE ' + appcode)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
response = urllib.request.urlopen(request, context=ctx)
content = json.loads(response.read())
tem = content['showapi_res_body']['now']['temperature']
tems = content['showapi_res_body']['now']['weather']
# 结束


# 配置邮件体
tag ='今日重庆天气：' + tem +'摄氏度' +'天气情况：' + tems
message = MIMEText(tag, 'plain', 'utf-8')
message['From'] = Header("DayBreak", 'utf-8')
message['To'] =  Header("nmxgzs@foxmail.com", 'utf-8')
subject = '柠檬心工作室每日天气预报'
message['Subject'] = Header(subject, 'utf-8')
try:
		smtpObj = smtplib.SMTP() 
		smtpObj.connect(mail_host, 587)    # 25 为 SMTP 端口号
		smtpObj.login(mail_user,mail_pass)  
		smtpObj.sendmail(sender, receivers, message.as_string())
		print ("邮件发送成功")
except smtplib.SMTPException:
		print ("发送邮件错误")