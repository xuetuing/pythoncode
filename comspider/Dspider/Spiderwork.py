from work.HtmlDownloader import HtmlDownloader
from work.HtmlParser import HtmlParser
from multiprocessing.managers import BaseManager

class SpiderWork(object):
    """ dispatcher of spider """
    def __init__(self):
        BaseManager.register("get_task_queue")
        BaseManager.register("get_result_queue")
        server_addr = '192.168.1.4'
        print("Connect to %s..." % server_addr)
        self.m = BaseManager(address=(server_addr,8001),authkey=b'shiyanlou')
        self.m.connect()
        self.task = self.m.get_task_queue()
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
                    self.result.put({'new_urls':'end','data':'end'})
                    return
                response = self.downloader.download(new_url)
                new_urls,datas = self.parser.parse(response)
                self.result.put({'new_urls':new_urls,'data':datas})
            except EOFError as e:
                print("connection failed!")
                return
            except Exception as e:
                print(e)
                print("crawl failed!")

if __name__ == '__main__':
    Spider = SpiderWork()
    Spider.crawler()
