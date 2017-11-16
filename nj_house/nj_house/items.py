# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field


class NjHouseItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    house=Field()
    total_price = Field()
    unit_price = Field()
    house_room = Field()
    house_area= Field()
