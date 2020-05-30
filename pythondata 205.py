# -*- coding: utf-8 -*-
"""
Created on Thu May 28 23:52:23 2020

@author: user
"""
import requests
import json

url = 'http://tqc.codejudger.com:3000/target/5205.json'

res = requests.get(url)

data = json.loads(res.text)

#print(data)

print('Content-Length:',res.headers['Content-Length'])

print('新北市PM2.5相關資料：')

for record in data:
    if record['County'] == '新北市':
        print('%s:'%record['SiteName'])
        print('\tAQI:%s'%record['AQI'])
        print('\tPM2.5:%s'%record['PM2.5'])
        print('\tPM10:%s'%record['PM10'])
        print('\t資料更新時間：%s'%record['PublishTime'])