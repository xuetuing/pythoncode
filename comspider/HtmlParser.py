from scrapy.selector import Selector
from urllib.parse import urljoin

class HtmlParser(object):
    """ class for parse Html """
    def parse(self,response):
        urls = self.get_new_urls(response)
        data = self.get_data(response)
        return urls,data

    def get_new_urls(self, response):
        """get naw urls """
        urls = set()
        selector = Selector(response).css(".position-relative .row .course")
        for item in selector:
            url = item.css("a::attr(href)").extract_first()
            url = urljoin(response.url,url)
            urls.add(url)        
        return urls
        
    def get_data(self, response):
        """get data """
        data = []
        selector = Selector(response).css(".position-relative .row .course")
        for item in selector:
            url = item.css("a::attr(href)").extract_first()
            cour_name = item.css(".course-name::text").extract_first()
            desc = item.css(".course-desc::text").extract_first()
            data.append((cour_name,desc,url))
        return data

        
    
