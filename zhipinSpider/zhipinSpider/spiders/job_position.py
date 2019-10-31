# -*- coding: utf-8 -*-
import scrapy
from zhipinSpider.items import ZhipinspiderItem

class JobPositionSpider(scrapy.Spider):
    name = 'job_position'
    allowed_domains = ['yjbys.com']
    start_urls = ['https://www.yjbys.com/zhaopinhui/']

    # scrapy 被动调用的方法
    def parse(self, response):
        for job_primary in response.xpath('//div[@class="zphList"]'):
            item = ZhipinspiderItem()
            date_time = job_primary.xpath('./div[@class="zph_left"]')
            date = date_time.xpath('./div[@class="time"]')
            now = date.xpath('./font[@class="now"]/text()').extract_first()
            tomorrow = date.xpath('./font[@class="tomorrow"]/text()').extract_first()
            day = date.xpath('./text()').extract_first()
            print('day is ', day)
            # 一定存在
            week = date.xpath('./font[@class="day"]/text()').extract_first()
            print('week is ', week)
            time = date_time.xpath('./div[@class="sj"]/text()').extract_first()
            print('time is ', time)
            # 提取详细信息
            a_label = job_primary.xpath('./a')
            city = a_label.xpath('./div[@class="city"]/font/text()').extract_first()
            print('city is ', city)
            location = a_label.xpath('./div[@class="city"]/span/text()').extract_first()
            print('location is ', location)
            addr = a_label.xpath('./div[@class="area Hy"]/font/text()').extract_first()
            print('address is ', addr)
            company = a_label.xpath('./div[@class="company"]/span/text()').extract_first()
            print('company is ', company)
            url = a_label.xpath('./@href').extract_first()
            print('url is ', url)
            item['_addr'] = addr
            item['_location'] = location
            item['_url'] = url
            item['_city'] = city
            item['_company'] = company
            item['_week'] = week
            item['_time'] = time
            item['_date'] = day if day else None
            yield item
        # 获取完成后, 获取下一页的连接
        new_links = response.xpath('//div[@class="pages"]/a/@href').extract()
        current_page = response.xpath('//div[@class="pages"]/span/text()').extract_first()
        print('==============', current_page)
        if new_links and len(new_links) > 0:
            last_page = new_links[-1]
            print('*********************', last_page)
            if current_page and current_page != '末页':
                yield scrapy.Request("https://www.yjbys.com" + last_page, callback=self.parse)