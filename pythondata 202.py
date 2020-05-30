# -*- coding: utf-8 -*-
"""
Created on Thu May 28 22:02:36 2020

@author: user
"""
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup 

file = open('write.csv','w',encoding='utf-8')

csv_write = csv.writer(file)

htmlfile = 'file:read202.html'
html = urlopen(htmlfile)

bsOj4 =  BeautifulSoup(html,'lxml')

count = 0
for single_tr in bsOj4.find('table',{'class':'DataTable2'}).findAll('tr'):
    if count == 0:
        cell = single_tr.findAll('th')
        
    else:
        cell = single_tr.findAll('td')
    F0 = cell[0].text
    F1 = cell[1].text
    data = [[F0,F1]]
    count += 1
    csv_write.writerows(data)    
file.close()    
#其他作法
##import pandas as pd
##import csv

##data = pd.read_html('read202.html',encoding='utf-8') 

##with open('write.csv','w',encoding='utf-8') as fp:
  ##  for i in range(len(data[1][0])):
    ##    csv.writer(fp).writerow([data[1][0][i],data[1][1][i]])
