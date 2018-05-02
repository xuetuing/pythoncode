from queue import Queue
from multiprocessing.managers import BaseManager
from URLmanager import Urlmanager
import time
from Store import Storage

class NodeManager(object):
    """ control node """
    def start_manager(self,url_q,result_q):
        BaseManager.register("get_task_queue",callable=lambda:url_q)
        BaseManager.register("get_result_queue",callable=lambda:result_q)
        manager = BaseManager(address=('',8001),authkey='shiyanlou')
        return manager

    def url_manager_proc(self,conn_q,url_q,root_url):
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
            except BaseException,e:
                time.sleep(1)

    def result_solve_proc(self, result_q,conn_q,store_q):
        while(True):
            try:
                if not result_q.empty():
                    content = result_q.get()
                    if content["new_urls"] == "end":
                        print("store_q接收通知，然后结束！")
                        store_q.put("end")
                        return
                    conn_q.put(content["new_urls"])
                    store_q.put(content["data"])
            except:
                time.sleep(1)

    def store_proc(self, store_q):
        output = Storage()
        try:
            if not store_q.empty():
                data = store_q.get()
                if data == "end":
                    output.outhtml(filepath)
                    return
                output.data_saved(data)
        except:
            time.sleep(1)

if __name__ == '__main__':
    url_q = Queue()
    conn_q = Queue()
    result_q = Queue()
    store_q = Queue()
