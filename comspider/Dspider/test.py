from multiprocessing import Process,Queue
from URLmanager import Urlmanager
import time

def url_manager_proc(url_q,conn_q,root_url):
        url_manager = Urlmanager()
        url_manager.add_new_url(root_url)
        while (url_manager.has_new_url()):
            new_url = url_manager.get_new_url()
            url_q.put(new_url)
            print("old_url= ",url_manager.old_urls_size())
            if url_manager.old_urls_size() >=200:
                url_q.put("end")
            try:
                if not conn_q.empty():
                    urls = conn_q.get()                    
                    url_manager.add_new_urls(urls)
            except BaseException as e:
                time.sleep(1)

if __name__ == '__main__':
    url_q = Queue()
    conn_q = Queue()
    #root_url = 'https://www.shiyanlou.com/courses/'

    url_manager = Process(target=url_manager_proc,args=(url_q,conn_q,"https://www.shiyanlou.com/courses/",))
    url_manager.start()
    url_manager.join()
    a = url_q.get()
    print(a)