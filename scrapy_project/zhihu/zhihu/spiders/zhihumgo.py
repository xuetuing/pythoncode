# -*- coding: utf-8 -*-
import scrapy
from zhihu.items import UserInfoItem,RelationItem


class ZhihumgoSpider(scrapy.Spider):
	name = 'zhihumgo'
	allowed_domains = ['www.zhihu.com']
	start_urls = ['https://www.zhihu.com/people/excited-vczh/activities']
	header = {}
	def start_requests(self):
		return [scrapy.Request('http://www.zhihu.com/',headers=header,callback=self.zhihu_login)]
	
	def zhihu_login(self, response):
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
		return [scrapy.FormRequest(post_url,formdata=post_data,headers=self.header,callback=self.after_login)]
		
	def after_login(self, response):
		response_text = json.loads(response.text)
		if 'msg' in response_text and response_text['msg'] == '登录成功':
			print('登录成功！')
			for url in self.start_urls:
				yield scrapy.Request(url,callback=parse_item,dont_filter=True,headers=self.header)
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

	def parse_user_info(self, response):
		item_loader = ItemLoader(item=UserInfoItem(),response=response)
		if 'people' in response.url:
			item_loader.add_css("","")
			item_loader.add_value("",)
			item_loader.add_xpath("",'')
			user_ider name address user_image_url prefession work_exper education resume followees_num
			follower_num
			userinfoitem = item_loader.load_item()
			yield userinfoitem
		
			if not relation_url:
				print("relation_url is empty.")
				return
			for url in relation_url:
				if 'following' in url:
					relation_type = 'following'
				else:
					relation_type = 'follower'
				scrapy.Request(url,user_ider=,relation_type=relation_type,callback=self.parse_relation)
		else:
			return
	def parse_relation(self,response):
		item_loader = ItemLoader(item=RelationItem,response=response)
		# if not relation_id:
		# 	for id in relation_id:
		# 		relation_id.append(id)
		relation_type = response.meta['relation_type']
		item_loader.add_value('user_ider',response.meta['user_ider'])
		item_loader.add_value('relation_type',response.meta['relation_type'])
		relation_url = response.css('')
		relation_id = [xx for url in relation_url:]
		item_loader.add_css('relation_id',relation_id)

		relationitem = item_loader.load_item()	
		yield relationitem	

		# next_page = response.css('')		
		# if next_page:
		# 	scrapy.Request(next_page,....,callback=self.parse_next_relation)
		# followees_num = response.css()
		# followers_num = response.css()
		# if relation_type = "following" and followers_num is not None:
		# 	for i in follower_num:
		# 		yield scrapy.Request(url,user_ider=,relation_type=,callback=self.parse_next_relation)
		# elif followees_num is not None:
		# 	for i in followees_num:
		# 		yield scrapy.Request(url,user_ider=,relation_type=,callback=self.parse_next_relation)

		for url in relation_url:
			if 'people' in url:
				scrapy.Request(url,headers=header,callback=self.parse_user_info)
		
		next_page = response.css('')		
		if next_page:
			yield scrapy.Request(url,user_ider=,relation_type=,callback=self.parse_relation)

	# def parse_next_relation(self,response):
	# 	item_loader = ItemLoader(item=RelationItem,response=response)
	# 	# if not relation_id:
	# 	# 	for id in relation_id:
	# 	# 		relation_id.append(id)
	# 	item_loader.add_value('user_ider',response.meta['user_ider'])
	# 	item_loader.add_value('relation_type',response.meta['relation_type'])
	# 	relation_url = response.css('')
	# 	relation_id = [xx for url in relation_url:]
	# 	item_loader.add_css('relation_id',relation_id)

	# 	relationitem = item_loader.load_item()	
	# 	yield relationitem	

	# 	for url in relation_url:
	# 		scrapy.Request(url,headers=header,callback=self.parse_user_info)