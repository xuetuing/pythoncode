import hashlib

def get_md5(url):
	m = hashlib.md5()
	md5 = m.update(url.encode('utf8'))
	return md5.hexdigest()