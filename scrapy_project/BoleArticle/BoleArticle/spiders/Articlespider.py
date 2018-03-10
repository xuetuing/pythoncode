import scrapy
import datetime
from scrapy.http import Request
from urllib import parse

from scrapy.loader import ItemLoader
#from BoleArticle.items import BolearticleItem, ArticleItemLoader
from BoleArticle.items import BolearticleItem
from BoleArticle.utils.common import get_md5

class JobboleSpider(scrapy.Spider):
	name = 'BoleArticle'
	#allowed_domains = ['blog.jobbole.com']
	allowed_domains = ['blog.jobbole.com']
	start_urls = ['http://blog.jobbole.com/all-posts/']

	def parse(self, response):
		"""
		1. 获取文章列表页中的文章url并交给scrapy下载后进行解析
		2. 获取下一页的url并交给scrapy进行下载，下载完成后交给parse
		"""

		# 解析列表页中的所有文章url并交给scrapy下载后进行解析
		post_nodes = response.css("#archive .floated-thumb .post-thumb a")
		for post_node in post_nodes:
			img_url = post_node.css("img::attr(src)").extract_first("")
			post_url = post_node.css("::attr(href)").extract_first("")
			yield Request(url=parse.urljoin(response.url, post_url), meta={"front_image_url": img_url}, callback=self.parse_detail)

		# 提取下一页并交给scrapy进行下载
		next_url = response.css(".next.page-numbers::attr(href)").extract_first()
		if next_url:
			yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)

	def parse_detail(self, response):
		
		article_item = BolearticleItem()

		title = response.css(".entry-header h1::text").extract_first("")
		create_date = response.css("p.entry-meta-hide-on-mobile::text").extract_first("").strip().replace(" ·","")
		try:
			create_date = datetime.datetime.strptime(create_date,"%Y/%m/%d").date()
		except Exception as e:
			create_date = datetime.datetime.now().date()

		selector = response.css(".copyright-area a")
		if len(selector) != 2:
			origin_url = selector[0].css("::attr(href)").extract_first("")
			trans_url = "nothing"
		else:
			origin_url = selector[0].css("::attr(href)").extract_first("")
			trans_url = selector[1].css("::attr(href)").extract_first("")		
		front_image_url = response.meta.get("front_image_url")
		url_id = get_md5(response.url)

		article_item["title"] = title
		article_item["create_date"] = create_date
		article_item["origin_url"] = origin_url
		article_item["trans_url"] = trans_url
		article_item["url_id"] = url_id

		'''
		item_loader = ArticleItemLoader(item=JobBoleArticleItem(), response=response)
		item_loader.add_css('title', '.entry-header h1::text')
		item_loader.add_value('url', response.url)
		item_loader.add_value('url_object_id', get_md5(response.url))
		item_loader.add_css('create_date', 'p.entry-meta-hide-on-mobile::text')
		item_loader.add_value('front_image_url', response.meta.get("front_image_url", ""))
		item_loader.add_css('praise_nums', '.vote-post-up h10::text')
		item_loader.add_css('comment_nums', "a[href='#article-comment'] span::text")
		item_loader.add_css('fav_nums', '.bookmark-btn::text')
		item_loader.add_css('tags', 'p.entry-meta-hide-on-mobile a::text')
		item_loader.add_css('content', 'div.entry')
		article_item = item_loader.load_item()
		'''
		yield article_item

