import requests, json
config = {
    "appid": '',
    "secret": '',
    "openId": '',
    "template_id": ''
}
host = 'https://api.weixin.qq.com/cgi-bin'
url = host + '/token?grant_type=client_credential&appid={appid}&secret={secret}'.format(
    appid=config['appid'], secret=config['secret'])
response = requests.post(url).content.decode('utf-8')
access_token = json.loads(response)['access_token']  #获取token
#请求发送消息接口
data = {
    "access_token": access_token,
    "touser": config['openId'],
    "template_id": config['template_id'],
    "data": {
        "phrase2": {
            "value": "重庆"
        },
        "phrase3": {
            "value": "晴天"
        },
        "date1": {
            "value": "2019年10月15日"
        },
        "character_string4": {
            "value": "25~28°"
        },
        "thing5": {
            "value": "温度较低，请注意保暖哦"
        }
    }
}
url = host + '/message/subscribe/send?access_token={access_token}'.format(
    access_token=access_token)
response = requests.post(url, json=data).content.decode('utf-8')
print(json.loads(response))