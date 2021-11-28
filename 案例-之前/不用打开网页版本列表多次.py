import urllib.request
urllist=[
		'https://blog.csdn.net/qq_31754591/article/details/111809145',
		'https://blog.csdn.net/qq_31754591/article/details/111811190',
		'https://blog.csdn.net/qq_31754591/article/details/111823107',
		'https://blog.csdn.net/qq_31754591/article/details/111772887',
		'https://blog.csdn.net/qq_31754591/article/details/111808308',
		'https://blog.csdn.net/qq_31754591/article/details/111825374',
		'https://blog.csdn.net/qq_31754591/article/details/111839337',
		'https://blog.csdn.net/qq_31754591/article/details/111902139',
		'https://blog.csdn.net/qq_31754591/article/details/111937652',
		'https://blog.csdn.net/qq_31754591/article/details/111995965',
		'https://blog.csdn.net/qq_31754591/article/details/112025655',
		'https://blog.csdn.net/qq_31754591/article/details/112105798',
		'https://blog.csdn.net/qq_31754591/article/details/112106312',
		'https://blog.csdn.net/qq_31754591/article/details/112116334',
		'https://blog.csdn.net/qq_31754591/article/details/112124069',
		'https://blog.csdn.net/qq_31754591/article/details/112161308',
		'https://blog.csdn.net/qq_31754591/article/details/112230425',
		'https://blog.csdn.net/qq_31754591/article/details/112250894',
		'https://blog.csdn.net/qq_31754591/article/details/110790412',
		'https://user.qzone.qq.com/249287892',
]
for url in urllist:
		req=urllib.request.Request(url)
		resp=urllib.request.urlopen(req)
		data=resp.read().decode('utf-8')
		print("当前访问"+ url +"成功")
