# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class TravelPipeline:
    def process_item(self, item, spider):
        return item
#    def process_item(self, item, spider):
#        title = item['title']
#        date = item['date']
#        days = item['days']
#        fee = item['fee']
#        people = item['people']
#        trip = item['trip']
#        icon_view = item['icon_view']
#        icon_love = item['icon_love']
#        icon_comment = item['icon_comment']
#        fp = open('./gonglue.txt','w',encoding = 'utf-8')
#        self.fp.write(title+date+fee+days+trip+people+icon_view+icon_love+icon_comment)
#        print('Done!')
#        return item
#    def open_spider(self,spider):
#        print('开始爬取...')
#        self.fp = open('./gonglue.txt','w',encoding = 'utf-8')
#
#    def close_spider(self,spider):
#        print('爬取结束！')
#        self.fp.close()