import jsonpath as jsonpath
import requests
import re
import json
import urllib
from urllib import parse
import sys
import you_get
import time

video_id = input('请输入视频id：')
url = 'https://www.douyin.com/video/' + video_id

print(url)
# url = 'https://www.douyin.com/user/MS4wLjABAAAAs3m7rmH8RItBoDeKb_FckdRzq2-M_cvbwp8bZUfjWB8?relation=0&vid=7267109392296824098'
headers = {
    'cookie': 'douyin.com; __ac_nonce=063d749310021f8bd394b; __ac_signature=_02B4Z6wo00f01R8urHgAAIDBnyxWOmwmfMUfDqjAACQfd6; ttwid=1%7CtRZY98IpvYfhjM-VRDQHgX3mgPcfWwWxylxnwwC7fFk%7C0%7C9af2c384c7d2b4e10ec0497fce797af996c72dd3868ec040595de36132c01ad0; home_can_add_dy_2_desktop=%220%22; passport_csrf_token=ee0cbadbf97ac430daac207c46997ca1; passport_csrf_token_default=ee0cbadbf97ac430daac207c46997ca1; strategyABtestKey=%221675053365.079%22; s_v_web_id=verify_ldibiwgl_ycqaypzT_aJxd_4ZEW_9iGD_XkAPFGlhzwd3; AB_LOGIN_GUIDE_TIMESTAMP=%221675053363589%22; msToken=L3xfxnCP4kW9_qabjW3S1cud_5DmI99tIEOw1_lJDMgdp1GJ9KQd6HWXKepYY-7iLlj4SR_V02zL3lYO6FVnXoPPVNneC5bD9cEnYN4nNpXzaNmvq7oA; ttcid=a598309ef5f3442b95f1d979574083f925; tt_scid=Px0Q21O38QIdeziR7nBXUqfZYJaS4qKakt5Zkfio72r9U4XaJdOYTb37LsjIrRLQca96; msToken=xibNm7RgEpzX8c6UaAgkzAOHMr5TcWNmNbfFR1vD-3uNUhtRXEqVQrmPIV6iDsnsA3WhMCTIOGDtST_F9GEyq8In6Dj7ug-RXsQ6dWDIjzE3OXKr5dlj',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}


def download_video(url, path, name):
    sys.argv = ['you-get', '-o', path, url, '-O', name]
    you_get.main()


try:
    resp = requests.get(url=url, headers=headers)
    obj = re.compile(r"<span><span><span><span>(?P<title>.*?)</span></span></span></span>", re.S)
    info = re.findall('<script id="RENDER_DATA" type="application/json">(.*?)</script', resp.text)[0]
    html_data = urllib.parse.unquote(info)
    html_data = json.loads(html_data)
    video_url = video_url = 'https:' + jsonpath.jsonpath(html_data, '$..src')[0]
    print(video_url)
    timeStr = int(time.time() * 1000)
    download_video(video_url, 'videos', str(timeStr))
except:
    print('报错了~~，请重试')

#
#
# import jsonpath as jsonpath
# import requests
# import re
# import json
# import urllib
# from urllib import parse
# import os
# from pprint import pprint
#
# """
#     常规找视频资源：到Network --> Media里面抓包，就能得到地址
#     然后在Media里面拿到地址，去全局搜索URL来源
# """
#
# # url = 'https://www.douyin.com/video/7194051743330618682'
# url = 'https://www.douyin.com/video/7267109392296824098'
#
# headers = {
#     'cookie': 'douyin.com; __ac_nonce=063d749310021f8bd394b; __ac_signature=_02B4Z6wo00f01R8urHgAAIDBnyxWOmwmfMUfDqjAACQfd6; ttwid=1%7CtRZY98IpvYfhjM-VRDQHgX3mgPcfWwWxylxnwwC7fFk%7C0%7C9af2c384c7d2b4e10ec0497fce797af996c72dd3868ec040595de36132c01ad0; home_can_add_dy_2_desktop=%220%22; passport_csrf_token=ee0cbadbf97ac430daac207c46997ca1; passport_csrf_token_default=ee0cbadbf97ac430daac207c46997ca1; strategyABtestKey=%221675053365.079%22; s_v_web_id=verify_ldibiwgl_ycqaypzT_aJxd_4ZEW_9iGD_XkAPFGlhzwd3; AB_LOGIN_GUIDE_TIMESTAMP=%221675053363589%22; msToken=L3xfxnCP4kW9_qabjW3S1cud_5DmI99tIEOw1_lJDMgdp1GJ9KQd6HWXKepYY-7iLlj4SR_V02zL3lYO6FVnXoPPVNneC5bD9cEnYN4nNpXzaNmvq7oA; ttcid=a598309ef5f3442b95f1d979574083f925; tt_scid=Px0Q21O38QIdeziR7nBXUqfZYJaS4qKakt5Zkfio72r9U4XaJdOYTb37LsjIrRLQca96; msToken=xibNm7RgEpzX8c6UaAgkzAOHMr5TcWNmNbfFR1vD-3uNUhtRXEqVQrmPIV6iDsnsA3WhMCTIOGDtST_F9GEyq8In6Dj7ug-RXsQ6dWDIjzE3OXKr5dlj',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
# }
# resp = requests.get(url=url, headers=headers)
# # resp = urllib.parse.unquote(resp.text)
# # print(resp.text)
#
#
# # 最新的解决方法，新导入一个包：import jsonpath
# # 把video_url更换为：video_url = 'https:' + jsonpath.jsonpath(html_data, '$..src')[0]
# # 这样就能无视那个标签了
# # 正则抓标题
# obj = re.compile(r"<span><span><span><span>(?P<title>.*?)</span></span></span></span>", re.S)
#
# # print(resp.text)
# # title = obj.search(resp.text).group("title")
# title = url
# # print(title)
#
# # 正则抓视频信息
# info = re.findall('<script id="RENDER_DATA" type="application/json">(.*?)</script', resp.text)[0]
# # print(info)
#
# # url解码
# html_data = urllib.parse.unquote(info)
# html_data = json.loads(html_data)
# # pprint(html_data['0'])  # 让字典更加美观
#
# # 字典取值，拿视频播放链接
# video_url = video_url = 'https:' + jsonpath.jsonpath(html_data, '$..src')[0]
# print(video_url)
#
#
#
#
# # 获取视频二进制数据
# video_content = resp = requests.get(url=video_url, headers=headers).content
#
# # 保存视频
# if not os.path.exists('./videos'):
#     os.mkdir('./videos')
# with open('./videos/' + title + '.mp4', mode='wb') as f:
#     f.write(video_content)
