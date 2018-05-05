import codecs
import time

class Storage(object):
	""" store data from html """
	def __init__(self):
		self.fipath = 'courses_{0}.html'.format(time.strftime("%d_%H_%M_%S",time.localtime()))
		self.outhtml_head()
		self.datas = []

	def data_saved(self, datas):
		if  datas is None:
			return
		self.datas.extend(datas)
		print(len(self.datas))
		if len(self.datas) > 10:
			self.outhtml_body()

	def outhtml_head(self):
		fi = codecs.open(self.fipath,"w",encoding="utf-8")
		fi.write("<html>")
		fi.write("<body>")
		fi.write("<table>")   
		fi.close()         

	def outhtml_body(self):
		fi = codecs.open(self.fipath,"a",encoding="utf-8")
		for data in self.datas:
			fi.write("<tr>")
			fi.write("<td>%s</td>" % data["url"])
			fi.write("<td>%s</td>" % data["cour_name"])
			fi.write("<td>%s</td>" % data["desc"])
			fi.write("</tr>")
			self.datas.remove(data)
		fi.close()

	def outhtml_end(self):
		fi = codecs.open(self.fipath,"a",encoding="utf-8")
		fi.write("</table>")
		fi.write("</body>")
		fi.write("</html>")
		fi.close()   
