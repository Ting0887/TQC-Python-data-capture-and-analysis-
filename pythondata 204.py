# -*- coding: utf-8 -*-
"""
Created on Thu May 28 23:32:11 2020

@author: user
"""
import json
import requests

url = 'http://tqc.codejudger.com:3000/target/5204.json'

res = requests.get(url)

data = json.loads(res.text)
#print(data)

print('新北市大專院校名單：\n')

for record in data:
    if record['type']=='大專院校':
        print('名稱 : %s'% record['name'])
        print('地址： %s'% record['address'])
        print('聯絡電話： %s'% record['tel'])
        print('網站： %s'% record['website'])
        print('資料更新時間： %s'% record['update_date'])
        print()