# -*- coding: utf-8 -*-
"""
Created on Fri May 29 21:39:25 2020

@author: user
"""

import matplotlib as mpl
mpl.use("Agg")

import matplotlib.pyplot as plt

#4個月份
labels = ['Jun','Jul','Aug','Sep']
sizes = [20,30,40,10]

#圓餅圖顏色
colors = ['yellowgreen','gold','lightskyblue','lightcoral']

#長條圖位置
plt.subplot(1,2,1)
xtick = range(1,len(labels)+1)

#長條圖以labels為X軸，sizes為Y軸，各長條顏色為藍色

plt.xticks(xtick,labels)
plt.bar(xtick,sizes,color='blue')

#圓餅圖位置
plt.subplot(1,2,2)

# 圓餅圖以labels為圖標，sizes為各項所占百分比
# 圓餅圖colors為各項顏色，突顯「Aug」
# 圓餅圖顯示各項百分比到小數點第1位

explode = (0,0,0.1,0)

plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%')

#長寬比為1:1
plt.axis('equal')

plt.savefig('chart.png')
plt.close()



