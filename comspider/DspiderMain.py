from Dspider.HtmlDownloader import HtmlDownloader
from Dspider.HtmlParser import HtmlParser
from Dspider.Store import Storage
from Dspider.URLmanager import Urlmanager

class SpisderMain(object):
    """ dispatcher of spider """
    def __init__(self):
        self.manager = Urlmanager()
        self.htmldownloader = HtmlDownloader()
        self.htmlparser = HtmlParser()
        self.storage = Storage()

    def crawler(self, root_url):
        self.manager.add_new_url(root_url)
        while self.manager.has_new_url() and self.manager.old_urls_size() <= 100 :
            new_url = self.manager.get_new_url()
            response = self.htmldownloader.download(new_url)
            new_urls,datas = self.htmlparser.parse(response)
            self.manager.add_new_urls(new_urls)
            self.storage.data_saved(datas)
        self.storage.outhtml()

if __name__ == '__main__':
    root_url = "https://www.shiyanlou.com/courses/?category=all&course_type=all&fee=all&tag=Python&page=1"
    Spider = SpisderMain()
    Spider.crawler(root_url)
