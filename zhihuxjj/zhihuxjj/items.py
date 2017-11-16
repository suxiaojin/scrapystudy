# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item,Field


class ZhihuxjjItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    user_name=Field()
    sex = Field()
    user_sign = Field()
    user_url = Field()
    user_avatar = Field()
    user_add = Field()

