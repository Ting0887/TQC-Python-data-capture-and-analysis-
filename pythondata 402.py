# -*- coding: utf-8 -*-
"""
Created on Fri May 29 21:09:31 2020

@author: user
"""

import matplotlib as mpl
mpl.use('Agg')

import matplotlib.pyplot as plt
import csv

x = []
y = []

#讀取 read.csv

with open('read402.csv','r',encoding='utf-8') as csv_file:
    plots = csv.reader(csv_file,delimiter = ',')
    for row in plots:
        x.append(row[0])
        y.append(float(row[1]))
        
x_ticks = range(1, len(x) + 1)

plt.plot(x_ticks,y,label ='banana' )        
plt.xticks(x_ticks,x)

plt.xlabel("date")
plt.ylabel("NT$")
plt.ylim([15,25])

#添加圖表標題

plt.title("Market Average Price")
plt.legend()

#使用savefig()函數
plt.savefig('chart.png')
plt.close()

