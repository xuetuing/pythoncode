import requests
class HtmlDownloader(object):
    """ Html download"""
    def download(self, url):
        header = {}
        if url is None:
            return None
        req = requests.get(url,headers=header)
        if req.status_code == 200:
            req.encoding = 'UTF-8'
            return req
        return None
        