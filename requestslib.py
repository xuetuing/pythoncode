#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
'''
r = requests.get('http://cuiqingcai.com')
print type(r)
print r.status_code
print r.encoding
#print r.text
print r.cookies

r = requests.post("http://httpbin.org/post")
r = requests.put("http://httpbin.org/put")
r = requests.delete("http://httpbin.org/delete")
r = requests.head("http://httpbin.org/get")
r = requests.options("http://httpbin.org/get")
'''
'''
#the get request
payload = {'key1':'value1','key2':'value2'}
r = requests.get("http://cuiqingcai.com/",params = payload)
print r.url
'''
'''
#get for JSON file ,json()
import requests

r = requests.get("a.json")
print r.text
print r.json()
'''
'''
# get raw socket
r = requests.get('https://github.com/timeline.json', stream=True)
r.raw
<requests.packages.urllib3.response.HTTPResponse object at 0x101194810>
r.raw.read(10)
'\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\x03'
'''
'''
# add headers
import requests

payload = {'key1': 'value1', 'key2': 'value2'}
headers = {'content-type': 'application/json'}
r = requests.get("http://httpbin.org/get", params=payload, headers=headers)
print r.url
'''
'''
#post request
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=payload)
print r.text
'''
'''
#sometime,need to submit info,(not form format,but JSON format),use json.dumps()
import json

url = 'http://httpbin.org/post'
payload = {'some': 'data'}
r = requests.post(url, data=json.dumps(payload))
print r.text
'''
'''
# upload file , use 'file' param
import requests

url = 'http://httpbin.org/post'
files = {'file': open('test.txt', 'rb')}
r = requests.post(url, files=files)
print r.text
'''
'''
# requests supports stream upload, need to provide a class file object for request
with open('massive-body') as f:
	requests.post('http://some.url/streamed', data=f)
'''
'''
#if a response include cookies, we can use cookies var to get it,and use cookies var to send cookies info to server
url = 'http://example.com'
r = requests.get(url)
print r.cookies
print r.cookies['example_cookie_name']

send cookies info:
url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
print r.text
'''
'''
#configure timeout var
requests.get('http://github.com', timeout=0.001)
'''
'''
# Session,

s = requests.Session()
s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get("http://httpbin.org/cookies")
print(r.text)          #twice req, the first to setup cookies,second to get cookies

# we can configure Session globally
s = requests.Session()
s.headers.update({'x-test': 'true'})
r = s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})
print r.text   # two headers var was uploaded
# if upload header var with get req,global configure will be covered
r = s.get('http://httpbin.org/headers', headers={'x-test': None})
'''
'''
#SSL certificate
r = requests.get('https://kyfw.12306.cn/otn/', verify=True)
print r.text
#if we want to Skip validation
r = requests.get('https://kyfw.12306.cn/otn/', verify=False)
print r.text
'''
'''
# using proxy 
proxies = {
  "https": "http://41.118.132.69:4433"
}
r = requests.post("http://httpbin.org/post", proxies=proxies)
print r.text
# also can use HTTP_PROXY and HTTPS_PROXY var to config 
export HTTP_PROXY="http://10.10.1.10:3128"
export HTTPS_PROXY="http://10.10.1.10:1080"
'''