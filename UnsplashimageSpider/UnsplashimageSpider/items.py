# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class UnsplashimagespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 图片id
    image_id = scrapy.Field()
    # 下载连接
    download = scrapy.Field()
