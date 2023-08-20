from urllib import request
import re
import json


class Spider():
    url = 'https://www.huya.com/g/wzry'
    root_pattern = '(?<=var LIST_DATA =).*?](?=;)'
    headers = {
        'cookie': 'Hm_lvt_51700b6c722f5bb4cf39906a596ea41f=1564389526; __yasmid=0.40853709224889045; __yamid_tt1=0.40853709224889045; __yamid_new=C88A54814D100001D1791CD16F0019D9; _yasids=__rootsid%3DC88A54814DB0000113A7D4A71FB71BBD; PHPSESSID=vbo6lo3mjm62rmrc3hpe4o03s0; Hm_lpvt_51700b6c722f5bb4cf39906a596ea41f=1564389529; udb_passdata=3; SoundValue=0.50; alphaValue=0.80; isInLiveRoom=true',
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
    }

    @staticmethod
    def __fetch_content(self):
        '''
        执行网页访问
        '''
        req = request.Request(Spider.url, None, Spider.headers)
        r = request.urlopen(req)
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        return htmls

    def __analysis(self, htmls):
        '''
        正则匹配页面数据标签
        '''
        html = re.findall(Spider.root_pattern, htmls)
        html = html[0].strip("'")
        html = html.strip(" ")
        # json转码
        return json.loads(html)

    def __refine(self, anchors):
        '''
        精炼数据
        '''
        datas = []
        for anchor in anchors:
            data = {
                'name': anchor['nick'],
                'number': anchor['totalCount']
            }
            datas.append(data)
        return datas

    def __sort(self, anchors):
        # 数据排序
        anchors = sorted(anchors, key=self.__sort_sedd, reverse=True)
        return anchors

    def __sort_sedd(self, anchor):
        # 排序处理
        return int(anchor['number'])

    def __show(self, anchors):
        '''
        展示排行榜数据
        '''
        for anchor in anchors:
            print(anchor['name'] + '----' + anchor['number'] + '人')

    def go(self):
        '''
        入口方法
        '''
        htmls = self.__fetch_content(self)
        anchors = self.__analysis(htmls)
        anchors = self.__refine(anchors)
        anchors = self.__sort(anchors)
        self.__show(anchors)


spider = Spider()
spider.go()

