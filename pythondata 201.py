# -*- coding: utf-8 -*-
"""
Created on Thu May 28 21:54:58 2020

@author: user
"""

import requests
import re

url = 'http://tqc.codejudger.com:3000/target/5201.html'

htmlfile = requests.get(url)

if htmlfile.status_code == 200:
    x = input('請輸入欲想搜尋的字串 : ')
    name = re.findall(x,htmlfile.text)
    if x in htmlfile.text:
        print(x,'搜尋成功')
        print(x,'出現 %d 次'%len(name))
    else:
        print(x,'搜尋失敗')
        print(x,'出現0次')
        
else:
    print('網頁無法載入')        
