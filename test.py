#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-21 10:55:01
# @Author  : xuetu

import requests
import json

url = 'https://www.lagou.com/jobs/list_python%20?labelWords=&fromSearch=true&suginput='
post_url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&isSchoolJob=0'

header = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36", 
    'Referer': url
}
item = []
for n in range(1,2):
    form_data = {
    'first': False,
    'pn': n,
    'kd': 'python'
}
    res = requests.get(post_url,data=form_data,headers=header)
    res_text = json.loads(res.text)
    result = res_text['content']['positionResult']['result']
    for i in range(14):
        print(result[i]['companyShortName'])
