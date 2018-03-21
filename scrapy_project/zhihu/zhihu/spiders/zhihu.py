# -*- coding: utf-8 -*-
import scrapy
import re
import requests
import json
import time
#import http.cookiejar as cookielib

class ZhihuSpider(scrapy.Spider):
	name = 'zhihu'
	allowed_domains = ['www.zhihu.com']
	start_urls = ['http://www.zhihu.com/']
	session = requests.session()
	agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE'
	header = {
		'HOST': 'www.zhihu.com',
		'Referer': 'https://www.zhihu.com',
		'User-agent': agent,
	}
	def parse(self, response):
		print('ok,ok')

	def start_requests(self):
		return [scrapy.Request("https://www.zhihu.com",headers=self.header,callback=self.zhihu_login)]
		
	def zhihu_login(self,response):
		account = '18224509954'
		password = 'tj141664'
		post_url = 'https://www.zhihu.com/login/phone_num'
		captcha = self.get_captcha()

		post_data = {
			'captcha_type': 'cn',
			'_xsrf': '', #get_xsrf()无用处
			'phone_num': account,
			'password': password,
			'captcha': captcha,
		}
		return [scrapy.FormRequest(post_url,formdata=post_data,headers=self.header,callback=self.check_login)]
		# response_text = self.session.post(post_url, data=post_data, headers=self.header)
		# #session.cookies.save()

	def check_login(self,response):	
		response_text = json.loads(response.text)
		if 'msg' in response_text and response_text['msg'] == '登录成功':
			print('登录成功！')
			for url in self.start_urls:
				yield scrapy.Request(url,dont_filter=True,headers=self.header)
		else:
			print('登录失败')


	def get_captcha(self):
		# 验证码URL是按照时间戳的方式命名的
		captcha_url = 'https://www.zhihu.com/captcha.gif?r=%d&type=login&lang=cn' % (int(time.time() * 1000))
		response = self.session.get(captcha_url, headers=self.header)
		# 保存验证码到当前目录
		with open('/home/hacker/pythonts/captcha.gif', 'wb') as f:
			f.write(response.content)
			f.close()

		# 自动打开刚获取的验证码
		from PIL import Image
		try:
			img = Image.open('/home/hacker/pythonts/captcha.gif')
			img.show()
			img.close()
		except:
			pass

		captcha = {
			'img_size': [200, 44],
			'input_points': [],
		}
		points = [[22.796875, 22], [42.796875, 22], [63.796875, 21], [84.796875, 20], [107.796875, 20], [129.796875, 22],
				[150.796875, 22]]
		seq = input('请输入倒立字的位置\n>')
		for i in seq:
			captcha['input_points'].append(points[int(i) - 1])
		return json.dumps(captcha)