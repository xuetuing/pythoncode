# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
# import datetime

# from scrapy.loader import ItemLoader
# from scrapy.loader.processors import MapCompose, TakeFirst, Join


class BolearticleItem(scrapy.Item):
	# define the fields for your item here like:
	# name = scrapy.Field()
	title = scrapy.Field()
	create_date = scrapy.Field()
	origin_url = scrapy.Field()
	trans_url = scrapy.Field()
	front_image_url = scrapy.Field()
	front_image_path = scrapy.Field()
	url_id = scrapy.Field()


'''
def add_jobbole(value):
    return value+'-bobby'

def data_convert(value):
    try:
        create_date = datetime.datetime.strptime(value, '%Y/%m/%d').date()
    except Exception as e:
        create_date = datetime.datetime.now().date()

    return create_date

def get_nums(value):
    match_re = re.match(r'.*?(\d+).*', value)
    if match_re:
        nums = match_re.group(1)
    else:
        nums = 0

    return nums

def remove_comment_tags(value):
    # 去掉tag中提取的“评论”
    if '评论' in value:
        return ''
    return value

def return_value(value):
    return value


class ArticleItemLoader(ItemLoader):
    # 自定义item_loader
    default_output_processor = TakeFirst()

class JobBoleArticleItem(scrapy.Item):
    title = scrapy.Field(
        input_processor=MapCompose(lambda x:x+'-jobbole', add_jobbole)
    )
    create_date = scrapy.Field(
        input_processor=MapCompose(data_convert)
    )
    url = scrapy.Field()
    url_object_id = scrapy.Field()
    front_image_url = scrapy.Field(
        output_processor=MapCompose(return_value)
    )
    front_image_path = scrapy.Field()
    praise_nums = scrapy.Field(
        input_processor=MapCompose(get_nums)
    )
    comment_nums = scrapy.Field(
        input_processor=MapCompose(get_nums)
    )
    fav_nums = scrapy.Field(
        input_processor=MapCompose(get_nums)
    )
    tags = scrapy.Field(
        input_processor=MapCompose(remove_comment_tags),
        output_processor=Join(',')
    )
content = scrapy.Field()
'''