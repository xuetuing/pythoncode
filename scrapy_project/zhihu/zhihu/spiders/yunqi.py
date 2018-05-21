# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from zhihu.items import YunQiBkListItem,YunQiBkDetailItem

class YunQiBook(CrawlSpider):
	name = 'yunqi'
	allowed_domains = ['yunqi.qq.com']
	start_urls = ['http://yunqi.qq.com/bk']
	header = {
		"User-agent": 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
	}
	rules = (
		Rule(LinkExtractor(allow=r'/bk/so2/n\d{2}p\d+'), callback='parse_booklist', follow=True),
	)
	# custom_setting for redirect 
	def parse_booklist(self,response):		
		books = response.css("#detailedBookList .book")
		for book in books:
			item_loader = ItemLoader(item=YunQiBkListItem(),response=book)
			item_loader.add_css("novel_image_url","img::attr(src)")
			item_loader.add_css("novel_id",".book_info h3 a::attr(id)")
			item_loader.add_css("novel_name",".book_info h3 > a::text")
			item_loader.add_css("novellink",".book_info h3 > a::attr(href)") #'>'select the child 'a' of 'h3'
			au_cls = book.css("dd > a::text").extract()
			item_loader.add_value("Author",au_cls[0])
			item_loader.add_value("classify",au_cls[1])
			supwrlist = book.css("dd::text").extract()
			item_loader.add_css("status",supwrlist[0])
			item_loader.add_css("update_time",supwrlist[1])
			item_loader.add_css("words",supwrlist[2])
			item_loader.add_css("resume",supwrlist[3])

			bklistitem = item_loader.load_item()
			yield bklistitem
			yield scrapy.Request(bklistitem['novellink'],callback='parse_bookdetail',meta={'novel_id':bklistitem['novel_id']})
	
	def parse_bookdetail(self, response):
		item_loader = ItemLoader(item=YunQiBkDetailItem(),response=response)
		num = response.css(".num td::text").extract()
		item_loader.add_value("novelallclick",num[0][4:].strip())
		item_loader.add_value("novelallpopular",num[1][4:].strip())
		item_loader.add_value("weekpopular",num[2][4:].strip())
		#item_loader.add_css("novelcomments","#novelInfo_commentCount::text")