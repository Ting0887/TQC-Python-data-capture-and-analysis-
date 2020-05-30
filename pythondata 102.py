# -*- coding: utf-8 -*-
"""
Created on Thu May 28 17:20:57 2020

@author: user
"""

import xml.etree.ElementTree as ET
import csv

tree = ET.parse("read102.xml")

root = tree.getroot()

file = open('write.csv','w',encoding='utf-8')

csv_w = csv.writer(file)

for row in root:
    ubike = []
    sno = row.find('sno').text
    ubike.append(sno)
    
    sna = row.find('sna').text
    ubike.append(sna)
    
    tot = row.find('tot').text
    ubike.append(tot)
    csv_w.writerow(ubike)
    
file.close()    