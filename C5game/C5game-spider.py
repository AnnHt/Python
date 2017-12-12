# https://www.c5game.com/dota.html

# 功能 ：爬取C5game上面饰品的价格

import scrapy

class MySpider(scrapy.Spider):
    name = "myspider"
    start_url = ["https://www.c5game.com/dota.html"]

    def parse(self,response):
        if "c5game" in response.url:
            from scrapy.shell import inspect_response
            inspect_response(response,self)

