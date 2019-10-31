# -*- coding: utf-8 -*-
import scrapy, json
from UnsplashimageSpider.items import UnsplashimagespiderItem

class UnsplashImageSpider(scrapy.Spider):
    name = 'unsplash_image'
    allowed_domains = ['unsplash.com']
    start_urls = ['https://unsplash.com/napi/photos?page=1&per_page=12']

    def __init__(self):
        super().__init__(self)
        self.page_index = 1

    def parse(self, response):
        photo_list = json.loads(response.text)
        for photo in photo_list:
            item = UnsplashimagespiderItem()
            item['image_id'] = str(photo['id'])
            item['download'] = photo['links']['download']
            yield item

        self.page_index += 1
        # 对爬取的总页数进行限制
        if self.page_index < 5:
            # 获取新的连接
            new_links = 'https://unsplash.com/napi/photos?page=' + str(self.page_index) + '&per_page=12'
            yield scrapy.Request(new_links, callback=self.parse)
