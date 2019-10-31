# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json

def local_dict(item):
    map = {}
    map['date'] = item['_date']
    map['time'] = item['_time']
    map['week'] = item['_week']
    map['company'] = item['_company']
    map['city'] = item['_city']
    map['address'] = item['_addr']
    map['location'] = item['_location']
    map['url'] = item['_url']
    return map
class ZhipinspiderPipeline(object):

    def __init__(self):
        self.json_file = open('job_position.json', 'wb+')
        self.json_file.write('[\n'.encode('utf-8'))

    # 实现关闭方法, 关闭相关资源
    def close_spider(self, spider):
        print('---------------关闭文件-------------')
        # 后退两个字符,去掉最后一行记录的换行符和逗号
        self.json_file.seek(-2, 1)
        self.json_file.write('\n]'.encode('utf-8'))
        self.json_file.close()

    def process_item(self, item, spider):
        # 将item转换为json字符串
        text = json.dumps(local_dict(item), ensure_ascii=False) + ',\n'
        print('final text is ', text)
        self.json_file.write(text.encode('utf-8'))
