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

        for url in relation_url:
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