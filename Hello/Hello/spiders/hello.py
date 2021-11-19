import scrapy
from urllib.parse import urlencode
from scrapy import Spider, Request,FormRequest
from ..items import HelloItem
import json
from selenium import webdriver
from scrapy.http import HtmlResponse
from ..items import HelloItem

class HelloSpider(scrapy.Spider):
    name = 'hello'
    def __init__(self):
        self.page=0

    def start_requests(self):
        baseurl = "https://www.vcg.com/creative-image/chengshifengguang/"
        meta={"selenium":True}
        yield Request(baseurl,callback=self.parse,meta=meta)

    def parse(self,response):
        self.page=self.page+1
        a=HelloItem()
        img_urls=response.css("#imageContent .galleryItem img::attr(data-src)").extract()
        for img_url in img_urls:
            a["url"]="https:"+img_url
            yield a
        if self.page<=200:
            next_page="https://www.vcg.com/creative-image/chengshifengguang/?page=%s" % self.page
            yield Request(url=next_page,callback=self.parse)




