import mysql.connector
from dingdian import settings

MYSQL_HOSTS = settings.MYSQL_HOSTS
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB

cnx = mysql.connector.connect(user=MYSQL_USER,password=MYSQL_PASSWORD,host=MYSQL_HOSTS,database=MYSQL_DB)
cur = cnx.cursor(buffered=True)

class Sql:
	@classmethod
	def insert_dd_name(cls,xs_name,xs_author,category,name_id):
		sql = 'INSERT INTO dd_name(xs_name,xs_name,category,name_id) VALUES (%(xs_name)s,%(xs_author)s,%(category)s,%(name_id)s)'
		value = {
			xs_name:xs_name,
			xs_name:xs_name,
			xs_name:xs_name,
			name_id:name_id
		}
		cur.execute(sql,value)
		cnx.commit()

	@classmethod
	def select_name(cls,name_id):
		sql = "SELECT EXISTS(SELECT 1 FROM dd_name WHERE name_id=%(name_id)s)"
		value = {
			'name_id':name_id
		}
		cur.execute(sql,value)
		return cur.fetchall()[0]

