class Urlmanager(object):
    """manager URL for spider """
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()
        
    def has_new_url(self):
        if self.new_urls:
            print("there are new_urls :" )
            print(self.new_urls)
            return True
        else:
            return False
        
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    def add_new_url(self, url):
        if url is None:
            return
        elif url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
        else:
            return
        
    def add_new_urls(self, urls):
        if urls is None:
            return
        else:
            for url in urls:
                self.add_new_url(url)
        
    def new_urls_size(self ):
        return len(self.new_urls)

    def old_urls_size(self ):
        return len(self.old_urls)