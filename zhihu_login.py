#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-15 10:30:09
# @Author  : xuetu


import requests

try:
    import cookielib
except:
    import http.cookiejar as cookielib

import re
import time
import json

session = requests.session()
session.cookies = cookielib.LWPCookieJar(filename='cookies.txt')
try:
    session.cookies.load(ignore_discard=True)
except:
    print('cookies reload faill!')
def get_xsrf():
    # 获取xsrf code
    response = session.get('https://www.zhihu.com', headers=header)
    # print(response.text)
    match_obj = re.match('[\s\S]*name="_xsrf" value="(.*?)"', response.text)
    if match_obj:
        return match_obj.group(1)
    else:
        return ''


def get_captcha():
    # 验证码URL是按照时间戳的方式命名的
    captcha_url = 'https://www.zhihu.com/captcha.gif?r=%d&type=login&lang=cn' % (int(time.time() * 1000))
    response = session.get(captcha_url, headers=header)
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

def get_index():
    response = session.get("https://www.zhihu.com/inbox",headers=header)
    with open("index.html","wb") as f:
        f.write(response.text.encode('utf-8'))
        f.close()
    print('ok')

def is_login():
    inbox_url = 'https://www.zhihu.com/inbox'
    response = session.get(inbox_url,headers=header)
    if response.statu_code != 200:
        return False
    else:
        return True
    
def zhihu_login(account, password):
    # 知乎登录
    if re.match('1\d{10}', account):
        print('手机号码登录')
        post_url = 'https://www.zhihu.com/login/phone_num'
        post_data = {
            'captcha_type': 'cn',
            '_xsrf': get_xsrf(),  #get_xsrf()无用处
            'phone_num': account,
            'password': password,
            'captcha': get_captcha(),
        }

        response_text = session.post(post_url, data=post_data, headers=header)
        session.cookies.save()
        response_text = json.loads(response_text.text)
        if 'msg' in response_text and response_text['msg'] == '登录成功':
            print('登录成功！')
        else:
            print('登录失败')


if __name__ == '__main__':
    agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE'
    header = {
        'HOST': 'www.zhihu.com',
        'Referer': 'https://www.zhihu.com',
        'User-agent': agent,
    }
    account = '18224509954' 
    pwd = 'tj141664'
    #zhihu_login(account, pwd)
    get_index()
