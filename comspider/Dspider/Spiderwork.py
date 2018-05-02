from Dspider.HtmlDownloader import HtmlDownloader
from Dspider.HtmlParser import HtmlParser
from multiprocessing.managers import BaseManager

class SpiderWork(object):
    """ dispatcher of spider """
    def __init__(self):
        BaseManager.register("get_url_queue")
        BaseManager.register("get_result_queue")
        server_addr = '127.0.0.1'
        print("Connect to %s..." % server_addr)
        self.m = BaseManager(address=(server_addr,8001),authkey='shiyanlou')
        self.m.connect()
        self.task = self.m.get_url_queue()
        self.result = self.m.get_result_queue()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()

    def crawler(self):
        while(True):
            try:
                if not self.task.empty():
                new_url = self.task.get()
                if new_url == 'end':
                    print("接收结束通知！")
                    self.result.put('new_urls':'end','data':'end')
                    return
                response = self.downloader.download(new_url)
                new_urls,datas = self.parser.parse(response)
                self.result.put('new_urls':new_urls,'data':datas)
            except EOFError,e:
                print("connection failed!")
                return
            except Exception,e:
                print(e)
                print("crawl failed!")

if __name__ == '__main__':
    Spider = SpiderWork()
    Spider.crawler()
