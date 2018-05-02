import requests
class HtmlDownloader(object):
    """ Html download"""
    def download(self, url_q):
        header = {}
        if not url_q.empty():
            url = url_q.get()
        else:
            return
        req = requests.get(url,headers=header)
        if req.status_code == 200:
            req.encoding = 'UTF-8'
            return req
        else:
            print("request failed!")
        