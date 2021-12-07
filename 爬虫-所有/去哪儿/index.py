import random
import xlwt
import requests
from bs4 import BeautifulSoup

url = 'https://hotel.qunar.com/napi/list'
headers = {
    "Cookie": "QN1=00008580306c3b2e3690d520; QN300=s%3Dbaidu%26%25E5%258E%25BB%25E5%2593%25AA%25E5%2584%25BF; QN99=8748; QN205=s%3Dbaidu%26%E5%8E%BB%E5%93%AA%E5%84%BF; QN277=s%3Dbaidu%26%E5%8E%BB%E5%93%AA%E5%84%BF; csrfToken=43xuWrqQ7N72HtVr57mVlBrIioE4aQKW; QN601=bd070d6968d77d28ce9008c15c21594b; QN163=0; _i=DFiEuYJfuRLDQ7mw-EfFxngzBMtw; QN48=000088002f103b2e36a85890; QN269=19BBDAD1574E11EC8C2BFA163EF4FDE0; QN667=A; HN1=v11e0e7e8849ecdd2228c4e020f9432340; HN2=quslzrsklrsrq; qunar-assist={%22show%22:false%2C%22audio%22:false%2C%22speed%22:%22middle%22%2C%22zomm%22:1%2C%22cursor%22:false%2C%22pointer%22:false%2C%22bigtext%22:false%2C%22overead%22:false%2C%22readscreen%22:false}; fid=1332ccf4-454c-4822-8a81-d6c29274b564; tabIndex=0; cityUrl=beijing_city; cityName=%25E5%258C%2597%25E4%25BA%25AC; checkInDate=2021-12-07; checkOutDate=2021-12-08; ctt_june=1638771050894##iK3wWSaNVuPwawPwasg%2BXskRa%3DPNXsETaS3waSGGXsTGXKjAXSiRVRPOERtNiK3siK3saKjsVRt%2BWKaOWKgNawPwaUvt; _vi=7ppz_3H4_pY_pvwHJMP1O7aspuTwwVnG7S1oWfV5QVUWnxAeJMrL2GuG6dAeIG8kg1jt3aIHrxUVR3SzESBZcLjWn0G6sSdDjlB3-8QXj1mAcI1qjEaUXT88k7F7qFpgZj1XBX1VSm9atgtgo32c57YI1ekBTXehH9nqUysmm12g; QN267=09859540380f6fcb5b; ctf_june=1638771050894##iK3wasgOahPwawPwasiTEDDAWsamESv%2BW2ETVK0RWRP8asETa%3DGhXK3%2BWPPAiK3siK3saKjsVRt%2BWSgsaS38WuPwaUvt; cs_june=c1bb5f2e42526eea7e1956dd7d548638b56f60d670ea8f952dd2866634be2bc9fe81855759098aeb5d7e8bb648872290afd659570d5243156166771a3c6a0d88b17c80df7eee7c02a9c1a6a5b97c117953f64101601b27485a3f8ffab766781c5a737ae180251ef5be23400b098dd8ca; QN271=579f15e0-42e5-4cd2-9c02-fcd059600632; __qt=v1%7CVTJGc2RHVmtYMTlDZ2publBPOER6SlNNUHZpN1FsaXVxQTB4QVB6V0VYc3JuOURDQ3JNVVl5UkRiTjZ0bDZFRVZJSEdpMUlncFlKQjdSc1Y3S3VxUTNRMzE3eEt2YmpaL3FIck8wWnB4dnV4SjVxU3AxS1o1WC9WR1c3d0dZNEpMaE8wdVAvV1dRZFdBckdKeVFkNDdZd1hjZERNeU4rTzk2OWlCMW4xUGhBPQ%3D%3D%7C1638876755093%7CVTJGc2RHVmtYMStiMytTaHVKYkJlcnNWMllQbE94cDN3M0svamR2cWYrWE1McldKdzc4TTJ4ZGcvNzIwb24vSXhZTmV5WFBWZExiVlloSlhkbzdSUEE9PQ%3D%3D%7CVTJGc2RHVmtYMSswbnJCVFN2ZHlCeVllcElmaDZjT0hwYTE0WlVnQUtrU1lGNW9PRWRlUVZrcXFBQUNhODgwcVJCUENVSytuVUFtMXNLMDFnNG5WVXJoMWtkQmx2WGkrV0JWOTZLRi9TZTlnV2crWnpXTWhrNFNUTGlTVmNoWjlCSFRIbjVJbWx3TkR1Z1RWQTFXR3I0cFJrbjZaRjN6aHF0OHpqczN0SGhIOFRDUE9RbGtEcy9tb01IaEN5Y2dkeXNvYlAwSTQxckF1OUttUjBMVC8zNEhwQWRicU9kakx6bFFjZjdmS1ZrRFB6WUZ5bHg2NlduZERCYm9DMmRGdmd6dTMrU21LdkJIeDNTem5SUnpKNEMvM2hrZkkzY2MvUCtNcG5jM2dDRmR2UkZPUys5Z0wrbVJxKzRpVUhKdDFNZ3FFM3JDRmJYbVFNVFJCb1hkTStCSUZ3T2JoZzhscWRTbWQ4amhvbkhWSmpDWExWd2w5R0V1QnNEWUJXM0ptejJBVXorRGFWSWxGZGFaMnZOTUE1VERwQzFKVmlaeXpLM3hHdlV3SlZzc0ZQQWJqeUpBL2RpQUxGNmR6NDNEdzN2R2lBclpwOHc3YXJFV0pGRG05aDJrWHJlaS9pY0ZXTzN4ZU90QVJiM1VaRGJLS1dlUng5NFRRemJoU3JaTkxxTXRTZWJ6ZGNkVmhxL2YwZ2hRbnl3bVY0b1M4WjhBek44R3E4NDQyUHVMa2l3SnBLOTRqOVcwT2ZmNkp4c2FoYzliRWVWYXlBdTlNYzNWekVZNW83VU1vQzZLeWJzY2lSbTBPclVsbzlUZjNXQ1pUNDFyY3AvMW5ONWpxbVp0ZHpzNDMzVXZwbDJFY0lOUzRvRWxObForN1JLSmhlbDVqM0NIbkpqa1hsK1E9",
    "accept": 'application/json, text/plain, */*',
    "accept-encoding": 'gzip, deflate, br',
    "accept-language": 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    "content-length": '1434',
    "content-type": 'application/json;charset=UTF-8',
    "origin": 'https://hotel.qunar.com',
    "referer": 'https://hotel.qunar.com/cn/nanchang/s00key23223139?fromDate=2021-12-07&toDate=2021-12-08',
    # sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="96", "Microsoft Edge";v="96"
    "sec-ch-ua-mobile": '?0',
    "sec-ch-ua-platform": "Windows",
    "sec-fetch-dest": 'empty',
    "sec-fetch-mode": 'cors',
    "sec-fetch-site": 'same-origin',
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43'
}
data = {"b": {"bizVersion": "17", "cityUrl": "beijing_city", "cityName": "北京", "fromDate": "2021-12-07",
              "toDate": "2021-12-08", "q": "", "qFrom": 3, "start": 40, "num": 20, "minPrice": 0, "maxPrice": -1,
              "level": "", "sort": 0, "cityType": 1, "fromForLog": 1, "uuid": "", "userName": "", "userId": "",
              "searchType": 0, "hourlyRoom": False, "locationAreaFilter": [], "comprehensiveFilter": [],
              "vtoken": "pclist-v2-990029ee9222f65a9e3ea02e4ce4a9ae", "channelId": 1},
        "Bella": "1638771050894##226c407a1d78e82a0495bc6e7505e5d132148443##iKohiK3wgMkMf-i0gUPwaUPsXuPwaMHxoIkLq5GAcMGwqMWxcuPwEUPwaUPwXwPwa5TQjOWxcI10aS30a=D0aS3waKvAiK3siK3sWK2=XKWIWPPsVKfIXKv+EhPwawPwasDOastmWsP+WKgAWK30aS30a2a0aSisyI0wcIkNiK3wiKWTiK3wVRk2aR3nfIDwVRvwWR3sf9D=WKv8jskHWIG2aS3OV9j0aS30a2a0aSi=y-ELfuPwaUPsXuPwaUkGWukTEukhEukGVukTWUPmWUkGWUPNWwPmWukGWukhXuPNWw=0EKP0VDP0X230EKP0VKa0XPD0EKP0VRX0X2j0EK20VRP0VK30EKP0X2D0VKg0aS30a2a0aSilf-0+c+i2gwPwaUPsXuPwaUPwXwkGWuPmXwPNWwkGWhkhXukTXwkGWuPmEukhXUkGWuPNawkTXukGWuPmWhkhEUkGVuPmWuPNaUkGWukhXuPNWwkGVukTaUPmWhkGVhkTEukTaUPwaUPwXwPwaME0gOWwy-T=y9FbiK3wiKWTiK3wiPPAiKHRiK2+iPP=iPiTiPGRaKPAVKa0EKP0XPP0XSj0EK20VRP0VK30EKP0X2D0VKg0EKP0XSt0XPP0EKj0VR30XKt0EK20XK30VRX0EKt0XPP0XK30EPj0X2a0VDa0EKP0VDP0X230EKP0VKa0XPD0EKP0VRX0X2j0EK20VRP0VK30EKP0X2D0VKg0aS30a2a0aSipc+W=iK3wiKWTiK3wyIF=f98bg-kbj-3bjOFeiK3wiKiRiK3wgOWwy-T=P+iSiK3wiKWTiKkhiK3wgMASgOEMq5GAcMGwqMWxcuPwaUPwXwPwa5iej+W2fUNno9NHgUNScO=0aS30WPX0W=Xt##uPjZQd8B-ON0AC8ydt9Th##b"}
# data = {}
# res = requests.post(url, headers=headers, data=data).content
res = requests.post(url, headers=headers, data=data).status_code
# soup = BeautifulSoup(res, "lxml")
# name = soup.select(".name")
print(res)
