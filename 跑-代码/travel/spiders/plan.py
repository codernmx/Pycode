import scrapy
from items import TravelItem

class PlanSpider(scrapy.Spider):
    name = 'plan'
    #allowed_domains = ['www.baidu.com']
    start_urls = ['https://travel.qunar.com/travelbook/list/23-jiangxi-298196/hot_heat/1.htm']

    url = 'https://travel.qunar.com/travelbook/list/23-jiangxi-298196/hot_heat/%d.htm'
    page_num = 2

    def parse(self, response):
        #tr_list = response.xpath("//ul[@class='b_strategy_list']")
        tr_list = response.xpath("/html/body/div[3]/div/div[2]/ul")
        for tr in tr_list:
            item = TravelItem()
            #标题、出发时间、天数、人均费用、人物、玩法
            item["title"] = tr.xpath("./h2/a/text()").extract_first()
            item["date"] = tr.xpath("./p[1]/span[1]/span[2]/text()").extract_first()
            item["days"] = tr.xpath("./p[1]/span[1]/span[3]/text()").extract_first()

            item["fee"] = tr.xpath("./p[1]/span[1]/span[5]/text()").extract_first()
            item["people"] = tr.xpath("./p[1]/span[1]/span[6]/text()").extract_first()
            item["trip"] = tr.xpath("./p[1]/span[1]/span[7]/text()").extract_first()

            fee = tr.xpath("./p[1]/span[1]/span[5]/text()").extract_first()
            people = tr.xpath("./p[1]/span[1]/span[6]/text()").extract_first()
            trip = tr.xpath("./p[1]/span[1]/span[7]/text()").extract_first()

#            print(fee,people,trip)

            if(fee):
                item["fee"] = fee
            else:
                item["fee"] = ""

            if(people):
                item["people"] = people
            else:
                item["people"]= ""


            if(trip):
                item["trip"] = trip
            else:
                item["trip"] = ""

            #获取阅读数，点赞数，评论数
            item["icon_view"] = tr.xpath("./p[1]/span[2]/span[1]/text()").extract_first()
            item["icon_love"] = tr.xpath("./p[1]/span[2]/span[3]/text()").extract_first()
            item["icon_comment"] = tr.xpath("./p[1]/span[2]/span[3]/text()").extract_first()

            detail_url = 'https://travel.qunar.com' + tr.xpath("./h2/a/@href").extract_first()

            yield scrapy.Request(url=detail_url,callback=self.parse_detail,meta={'item':item})
        if self.page_num <= 5:
            next_url = format(self.url % self.page_num)
            self.page_num += 1
            yield scrapy.Request(url=next_url,callback=self.parse)

#            next_url = 'https://travel.qunar.com/travelbook/list/23-jiangxi-298196/hot_heat/{}.htm'.format(page)
#            yield reponse.follow(next_url)
    def parse_detail(self,response):
        item = response.meta['item']
        place = response.xpath("//div[@class='b_crumb']/p[@class='b_crumb_cont']/a[2]/text()").extract_first()
        item['city'] = place.split('旅游')[0]
        yield item
            
