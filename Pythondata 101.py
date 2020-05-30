# -*- coding: utf-8 -*-
"""
Created on Thu May 28 16:34:52 2020

@author: user
"""
import json
import csv

file = open('read101.json',encoding='utf-8')

data = json.load(file)

f = open('write.csv','w',encoding='utf-8')

write_csv = csv.writer(f)

for item in data:
    write_csv.writerow([item["title"],item["showUnit"],item["startDate"],item["endDate"]])

    
    