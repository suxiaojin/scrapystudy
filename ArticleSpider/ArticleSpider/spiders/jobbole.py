# -*- coding: utf-8 -*-
import re
from scrapy.http import Request
from scrapy import Spider


class JobboleSpider(Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/']

    def parse(self, response):
        title=response.xpath('//div[@class="entry-header"]/h1/text()').extract_first()
        create_date=response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()').extract()[0].strip()
        praise_nums=response.xpath('//span[contains(@class,"vote-post-up")]/h10/text()').extract()[0]
        fav_nums=response.xpath('//span[contains(@class,"bookmark-btn")]/text()').extract()[0]
        match_re=re.match(".*?(\d+).*",fav_nums)
        if match_re:
            fav_nums=match_re.groups(1)

        comment_nums=response.xpath('//a[@href="#article-comment"]/span/text()').extract()[0]
        match_re=re.match(".*?(\d+).*",comment_nums)
        if match_re:
            comment_nums=match_re.groups(1)

        content=response.xpath("//div[@class='entry']").extract()[0]
        tag_list = response.xpath("//p[@class='entry-meta-hide-on-mobile']/a/text()").extract()
        tag_list = [element for element in tag_list if not element.strip().endswith("评论")]
        tags = ",".join(tag_list)