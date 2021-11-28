import urllib.request
import time


def cycle():
		urllist = [
				'111809145',
				'111811190',
				'111823107',
				'111772887',
				'111808308',
				'111825374',
				'111839337',
				'111902139',
				'111937652',
				'111995965',
				'112025655',
				'112105798',
				'112106312',
				'112116334',
				'112124069',
				'112161308',
				'112230425',
				'112250894',
				'110790412',
				'112264526',
				'112269131',
				'112269205',
				'112269240',
				'112287344',
				'112287733',
				'112297407',
				'112298474',
				'112298529',
				'112299457',
				'112341356',
				'112352938',
				'112366090',
				'112391045',
				'112393571',
		]
		count = 0
		baseUrl = 'https://blog.csdn.net/qq_31754591/article/details/'
		for url in urllist:
				req = urllib.request.Request(baseUrl + url)
				resp = urllib.request.urlopen(req)
				# data读取页面吧
				data = resp.read().decode('utf-8')
				count = count+1
				print("当前访问",baseUrl+url,count)


def sleeptime(hour, min, sec):
		return hour * 3600 + min * 60 + sec


second = sleeptime(0, 0, 3600)
while 1 == 1:
		cycle()
		time.sleep(second)
# 这是隔180秒执行一次
