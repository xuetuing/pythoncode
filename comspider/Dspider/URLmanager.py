import hashlib
import pickle
from utils import get_md5

class Urlmanager(object):
    """manager URL for spider """
    def __init__(self):
        self.new_urls = self.load_process("new_urls.txt")
        self.old_urls = self.load_process("old_urls.txt")
        
    def has_new_url(self):
        if self.new_urls:
            print("there are new_urls :" )
            print(self.new_urls)
            return True
        else:
            return False
        
    def get_new_url(self):
        new_url = self.new_urls.pop()
        url_md5 = get_md5(new_url)[8:-8]
        self.old_urls.add(url_md5)
        return new_url

    def add_new_url(self, url):
        if url is None:
            return
        url_md5 = get_md5(url)[8:-8]
        if url not in self.new_urls and url_md5 not in self.old_urls:
            self.new_urls.add(url)
        
    def add_new_urls(self, urls):
        if urls is None:
            return
        else:
            for url in urls:
                self.add_new_url(url)
        
    def new_urls_size(self):
        return len(self.new_urls)

    def old_urls_size(self):
        return len(self.old_urls)

    def load_process(self, path):
        print("从文件加载进度：%s" % path)
        try:
            with open(path,"rb") as f:
                temp = pickle.load(f)
                return temp
        except:
                print("无进度文件，创建：%s" % path)
        return set()

    def save_process(self, path,data):
        with  open(path,"wb") as f:
            pickle.dumps(data,f)