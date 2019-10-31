# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from urllib.request import *

class UnsplashimagespiderPipeline(object):
    def process_item(self, item, spider):
        # 直接下载图片
        download_url = item['download']
        download_url += '?force=true'
        print('download url is %s' % download_url)
        try:
            with urlopen(download_url) as result:
                data = result.read()
                with open('images/' + item['image_id'] + '.jpg', 'wb+') as f:
                    f.write(data)
        except:
            print('下载图片失败, URL is %s, image_id is %s' % (download_url, item['image_id']))
        return item
