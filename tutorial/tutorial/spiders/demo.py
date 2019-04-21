import scrapy
from tutorial.items import TutorialItem

class Cnblog_Spider(scrapy.Spider):

    name = "cnblog"
    allowed_domains = ["cnblog.com"]
    start_urls = [
     'https://www.cnblogs.com/',
    ]

    def parse(self, response):

        item = TutorialItem()

        item['title'] = response.xpath('//a[@class="titlelnk"]/text()').extract()
        item['link'] = response.xpath('//a[@class="titlelnk"]/@href').extract()

        yield item