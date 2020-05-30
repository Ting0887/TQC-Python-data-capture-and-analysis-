# -*- coding: utf-8 -*-
"""
Created on Thu May 28 21:04:08 2020

@author: user
"""

import json

data = {}

data['people'] = []

data['people'].append({'id': '1','name': 'Peter','country': 'Taiwan'})
data['people'].append({'id': '2','name': 'Jack','country': 'USA'})
data['people'].append({'id': '3','name': 'Cindy','country': 'Japan'})

file = open('write.json','w',encoding='utf-8')
json.dump(data,file)
