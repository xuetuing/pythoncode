import codecs
class Storage(object):
    """ store data from html """
    def __init__(self):
        self.datas = []
    
    def data_saved(self, data):
        if data:
            self.datas.append(data)
        else:
            return

    def outhtml(self):
        if self.datas is None:
            return
        else:
            fi = codecs.open("baike.html","w",encoding="utf-8")
            fi.write("<html>")
            fi.write("<body>")
            fi.write("<table>")
            for data in self.datas:
                fi.write("<td>%s</td>" % data["url"])
                fi.write("<td>%s</td>" % data["cour_name"])
                fi.write("<td>%s</td>" % data["desc"])
            fi.write("</table>")
            fi.write("</body>")
            fi.write("</html>")
            self.datas.pop(data)
            fi.close()         
           
            
