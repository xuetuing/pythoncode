import hashlib

def get_md5(url):
    m = hashlib.md5()
    md5 = m.update(url)
    return md5.hexdigest()