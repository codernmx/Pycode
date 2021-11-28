import smtplib, requests, json
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
from bs4 import BeautifulSoup
config = {
    # 'appcode': '',
    # 'host': "smtp.qq.com",  #设置服务器
    # 'user': "nmxgzs@foxmail.com",  #用户名
    # 'pass': "",  #口令
    # 'sender': 'nmxgzs@foxmail.com',
    # 'receivers': 'nmxgzs@foxmail.com'  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
}
# 开始请求天气接口
url = 'https://weather.cma.cn/api/weather/view?stationid=57516'
# 重庆
response = requests.get(url).content.decode('utf-8')
soup = BeautifulSoup(response, "lxml")
daily = json.loads(response)['data']['daily'][0]
now = json.loads(response)['data']['now']

high = daily['high'] #最高
low = daily['low'] #最低
dayText = daily['dayText'] #天气情况
temperature = now['temperature'] #温度
pressure = now['pressure'] #压强
humidity = now['humidity'] #湿度
# 结束
# 配置邮件体
message = MIMEText('今日重庆天气：' + str(temperature) + '摄氏度' + '天气情况：' + str(dayText), 'plain','utf-8')
message['From'] = formataddr(["Undefined", config['sender']])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
message['To'] = formataddr(["Undefined", config['receivers']])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
message['Subject'] = Header('柠檬心工作室每日天气预报', 'utf-8')
try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(config['host'], 587)  # 25 为 SMTP 端口号
    smtpObj.login(config['user'], config['pass'])
    smtpObj.sendmail(config['sender'], config['receivers'], message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("发送邮件错误")
