# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from zhihu.items import LgjobItem
from zhihu.utils.common import get_md5

class LagouSpider(CrawlSpider):
	name = 'lagou'
	allowed_domains = ['www.lagou.com']
	start_urls = ['https://www.lagou.com/']
	header = {
		"User-agent": 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
	}
	rules = (
		Rule(LinkExtractor(allow=r'jobs/\d+.html'), callback='parse_job', follow=True),
	)
	# custom_setting for redirect 
	custom_settings = {
		"COOKIES_ENABLED": False,
		"DOWNLOAD_DELAY": 1,
		'DEFAULT_REQUEST_HEADERS': {
			'Accept': 'application/json, text/javascript, */*; q=0.01',
			'Accept-Encoding': 'gzip, deflate, br',
			'Accept-Language': 'zh-CN,zh;q=0.8',
			'Connection': 'keep-alive',
			'Cookie': '_ga=GA1.2.127740001.1521724564; user_trace_token=20180322211606-2df6c614-2dd3-11e8-9654-525400f775ce; LGUID=20180322211606-2df6cb49-2dd3-11e8-9654-525400f775ce; index_location_city=%E5%85%A8%E5%9B%BD; WEBTJ-ID=20180324201304-16257ed33aa17f-07c84aab8c361f-454c062c-1049088-16257ed33ab461; _gid=GA1.2.291503696.1521893587; JSESSIONID=ABAAABAAAGFABEF4B6E7824D4539A2567CCF94174F84E9A; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1521724564,1521724570,1521893587,1521893593; TG-TRACK-CODE=index_search; SEARCH_ID=35514b8096924be8b0afa9a21a4a0649; X_MIDDLE_TOKEN=7010ccaa4c9d7c33e96a85534ff7bd1f; X_HTTP_TOKEN=0daffa6ee9c32220dbdd9408c4ac715b; LGSID=20180324225823-cc94fffe-2f73-11e8-b62c-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Futrack%2FtrackMid.html%3Ff%3Dhttps%253A%252F%252Fpassport.lagou.com%252Flogin%252Flogin.html%253Fmsg%253Dvalidation%2526uStatus%253D2%2526clientIp%253D121.231.224.44%26t%3D1521903440%26_ti%3D1%253E; PRE_LAND=https%3A%2F%2Fpassport.lagou.com%2Flogin%2Flogin.html%3Fmsg%3Dvalidation%26uStatus%3D2%26clientIp%3D121.231.224.44; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1521903867; LGRID=20180324230430-a76214a5-2f74-11e8-9d2c-525400f775ce',
			'Host': 'www.lagou.com',
			'Origin': 'https://www.lagou.com',
			'Referer': 'https://www.lagou.com/',
			"User-agent": 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
			}
		}
	def parse_job(self,response):
		#job_item = LgjobItem()
		#job_item["title"] = response.css(".job-name::attr(title)").extract()
		item_loader = ItemLoader(item=LgjobItem(),response=response)
		# here should the word 'item',not 'Item'	
		item_loader.add_css("title",".job-name::attr(title)")
		item_loader.add_value("url_id",get_md5(response.url))
		item_loader.add_xpath("exper",'//*[@class="job_request"]/p/span[3]/text()')
		item_loader.add_xpath("address",'//*[@class="job_request"]/p/span[2]/text()')
		item_loader.add_css("company",".job-name .company::text")
		item_loader.add_css("salary",".salary::text")
		item_loader.add_css("pub_time",".publish_time::text")

		job_item = item_loader.load_item()
		return job_item

	def parse_item(self, response):
		pass