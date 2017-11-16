# -*- coding: utf-8 -*-
import scrapy
from nj_house.items import NjHouseItem
import re

class LjHouseSpider(scrapy.Spider):
    name = 'lj_house'
    allowed_domains = ['nj.lianjia.com/ershoufang/']
    start_urls = ['http://nj.lianjia.com/ershoufang/']

    def parse(self, response):
        clears=response.css('.sellListContent li')
        for c in clears:
            item=NjHouseItem()
            try:
                house=c.css('.houseInfo a::text').extract_first()
                house_text=c.css('.houseInfo::text').extract_first()
                house_info_list=[e for e in re.split('\|',house_text) if len(e) > 1]
                house_room=house_info_list[0].strip()
                house_area=''.join(re.findall(r'[\d+\.]',house_info_list[1]))
                total_price=c.css('.totalPrice span::text').extract_first()
                unit_price=c.css('.unitPrice san::text').extract_first()
                unit_price=re.findall('\d+',unit_price[0])

                item['house']=house
                item['total_price']=float(total_price)
                item['unit_price']=int(unit_price)
                item['house_area']=float(house_area)
                item['house_room']=house_room

                yield item
            except Exception as e:
                print e,house_info_list



