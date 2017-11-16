# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from qiushibaike.items import QiushibaikeItem


class QsbkSpider(CrawlSpider):
    name = 'qsbk'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['http://qiushibaike.com/hot/']

    rules = [
        Rule(LinkExtractor(allow=r'http://www.qiushibaike.com/hot/.*?'), callback='parse_item', follow=True),
    ]

    def parse_item(self, response):

        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        for sel in response.xpath('//div[@class="article block untagged mb15"]'):
            item=QiushibaikeItem()
            item['author']=sel.xpath('.//h2/text()')[0].extract()
            item['duanzi']=sel.xpath('div[@class="content"]/text()').extract()
            yield item

