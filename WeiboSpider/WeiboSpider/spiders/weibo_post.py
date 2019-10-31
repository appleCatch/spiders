# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
import time


class WeiboPostSpider(scrapy.Spider):
    name = 'weibo_post'
    allowed_domains = ['weibo.com']
    start_urls = ['http://weibo.com/']

    hearders = {
        'Referer':'https://weibo.com/login',
        'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'
    }

    def __init__(self):
        super().__init__(self)
        self.login_cookies = []

    def get_cookies(self):
        '''使用selenium登录,并获取cookies信息'''
        browser = webdriver.Chrome(executable_path='/opt/drivers/chromedriver')
        browser.maximize_window()
        time.sleep(3)
        browser.get('https://weibo.com/login')
        # 获取用户名文本框
        elem_user = browser.find_element_by_xpath('//input[@id="loginname"]')
        elem_user.send_keys('fanzejun001@sina.com')
        # 获取密码文本框
        elem_pwd = browser.find_element_by_xpath('//input[@type="password"]')
        elem_pwd.send_keys('fan11235813*')
        # 获取提交按钮
        commit_btn = browser.find_element_by_xpath('//a[@node-type="submitBtn"]')
        commit_btn.click()
        time.sleep(10)
        if '新鲜事' in browser.title:
            self.login_cookies = browser.get_cookies()
        else:
            print('登录失败')

    def start_requests(self):
        self.get_cookies()
        print('======================', self.login_cookies)
        # 使用cookie访问登录后的内容
        return [scrapy.Request('https://weibo.com/u/1325194734/home',
                               headers=WeiboPostSpider.hearders,
                               cookies=self.login_cookies,
                               callback=self.parse)]

    def parse(self, response):
        print('****************parser......')
        pass
