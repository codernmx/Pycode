import urllib.request,sys
import urllib.parse


url = 'https://www.runoob.com/?s='  # 菜鸟教程搜索页面
keyword = 'Python 教程'
key_code = urllib.request.quote(keyword)  # 对请求进行编码
url_all = url+key_code
header = {
    'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}   #头部信息
request = urllib.request.Request(url_all,headers=header)
request.encoding = 'gb2312'

reponse = urllib.request.urlopen(request).read()
print(reponse)