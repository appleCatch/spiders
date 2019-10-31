#!/usr/bin/python3
# -*- coding:utf-8 -*-

import codecs, json

file_name = '/home/nj-s2-fanzejun/PycharmProjects/zhipinSpider/job_position.json'

with codecs.open(file_name, 'r', encoding='utf-8', buffering=True) as f:
    json_data = json.load(f)

# print(json_data)

# 使用相关作图软件分析数据