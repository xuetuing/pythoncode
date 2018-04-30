from comspider.HtmlDownloader import HtmlDownloader
from comspider.HtmlParser import HtmlParser
from comspider.Store import Storage
from comspider.URLmanager import Urlmanager

class SpisderMain(object):
    """ dispatcher of spider """
    def __init__(self):
        self.manager = Urlmanager()
        self.htmldownloader = HtmlDownloader()
        self.htmlparser = HtmlParser()
        self.storage = Storage()

    def crawler(self, root_url):
        self.manager.add_new_url(root_url)
        while self.manager.has_new_url() and self.manager.old_urls_size <= 100 :
            new_url = self.manager.get_new_url()
            response = self.htmldownloader.download(new_url)
            new_urls,data = self.htmlparser.parse(response)
            self.manager.add_new_urls(new_urls)
            self.storage.data_saved(data)
        self.storage.outhtml()

if __name__ == '__main__':
    root_url = "https://www.shiyanlou.com/courses/?category=all&course_type=all&fee=all&tag=Python&page=1"
    Spider = SpisderMain()
    Spider.crawler(root_url)
