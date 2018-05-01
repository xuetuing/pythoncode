from scrapy.selector import Selector
from urllib.parse import urljoin

class HtmlParser(object):
	""" class for parse Html """
	def parse(self,response):
		print("parse the response from %s" % response.url)
		urls = self.get_new_urls(response)
		data = self.get_data(response)
		return urls,data

	def get_new_urls(self, response):
		"""get naw urls """
		urls = set()
		selector = Selector(response).css(".pagination li")
		#next_url = selector.xpath('//a[@aria-label="Next"]/@href').extract()
		for item in selector:
			url = item.css("a::attr(href)").extract_first()
			if url == '#':
				continue
			else:		
				url = urljoin(response.url,url)
				urls.add(url)
		return urls

	def get_data(self, response):
		"""get data """
		data = {}
		datas = []
		selector = Selector(response).css(".position-relative .row .course")
		for item in selector:
			url = item.css("a::attr(href)").extract_first()
			data['url'] = urljoin(response.url,url)
			data['cour_name']  = item.css(".course-name::text").extract_first()
			data['desc'] = item.css(".course-desc::text").extract_first()
			datas.append(data.copy())
		return datas

        
    
