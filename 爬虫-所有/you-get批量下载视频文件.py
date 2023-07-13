import sys
import you_get
import time
def download_video (url, path,name):
sys.argv = ['you-get', '-o', path, url,'-O',name]
# -o 指定path -O 指定文件名
you_get.main()

if __name__ == '__main__':
# 要下载视频的链接
url = 'https://sf1-cdn-tos.huoshanstatic.com/obj/media-fe/xgplayer_doc_video/mp4/xgplayer-demo-360p.mp4'
# 视频的保存地址
path = 'test'
timeStr = int(time.time()*1000)
download_video(url,path,str(timeStr))
