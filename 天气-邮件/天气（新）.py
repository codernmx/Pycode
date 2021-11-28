import requests
import json
from bs4 import BeautifulSoup
#ssr配置代理
url = 'https://weather.cma.cn/api/weather/view?stationid=57516'
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

print(high)
print(low)
print(dayText)
print(temperature)
print(pressure)
print(humidity)
# print(now)