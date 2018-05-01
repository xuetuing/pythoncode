import requests
class HtmlDownloader(object):
    """ Html download"""
    def download(self, post_url):
        header = {}
        req = requests.get(post_url,headers=header)
        if req.status_code == 200:
            req.encoding = 'UTF-8'
            return req
        else:
            print("request failed!")
        