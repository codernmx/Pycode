# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TravelItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    date = scrapy.Field()
    days = scrapy.Field()
    fee = scrapy.Field()
    people = scrapy.Field()
    trip = scrapy.Field()
    icon_view = scrapy.Field()
    icon_love = scrapy.Field()
    icon_comment = scrapy.Field()
    city = scrapy.Field()
