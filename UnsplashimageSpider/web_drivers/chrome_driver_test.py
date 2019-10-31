#!/usr/bin/python3
# -*- coding:utf-8 -*-

from selenium import webdriver
import time

browser = webdriver.Chrome(executable_path='/opt/drivers/chromedriver')

time.sleep(3)

browser.get('https://www.baidu.com')

time.sleep(5)