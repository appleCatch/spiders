# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# https://www.yjbys.com/zhaopinhui/
class ZhipinspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    _date = scrapy.Field()
    _time = scrapy.Field()
    _week = scrapy.Field()
    _company = scrapy.Field()
    _city = scrapy.Field()
    _addr = scrapy.Field()
    _location = scrapy.Field()
    _url = scrapy.Field()
