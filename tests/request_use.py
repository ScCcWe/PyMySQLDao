# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: request_use.py
# author: ScCcWe
# time: 2022/4/11 3:28 下午
import requests

# wd是在网址中后面的一段
params = {
    'wd': '中国'
}

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}

# 这时我们要在这个网址中加入S
response = requests.get("http://www.baidu.com/s", params=params, headers=headers)
print("res: ", response)
print("res: ", response.status_code)
# print("res: ", response.text)
# print("res: ", response.json())
