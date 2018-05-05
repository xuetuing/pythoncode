import hashlib

def get_md5(url):
	md5 = hashlib.md5()
	md5.update(url.encode('utf8'))
	return md5.hexdigest()