# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field,Item


class BooksItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    book_name=Field()
    book_star = Field()
    book_pl = Field()
    book_author = Field()
    book_publish = Field()
    book_date = Field()
    book_price = Field()
