# -*- coding: utf-8 -*-
"""
Created on Fri May 29 22:10:28 2020

@author: user
"""

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

#讀取學生分數
#讀取read.csv

df = pd.read_csv('read404.csv',encoding='utf-8')

scores = df["scores"].values

range_count = [0,0,0,0,0]

for score in scores:
    if score < 20:
        range_count[0] += 1
    elif score < 40:
        range_count[1] += 1
    elif score < 60:
        range_count[2] += 1
    elif score < 80:
        range_count[3] += 1
    else:
        range_count[4] += 1
        
        
#y軸標籤
index = np.arange(0,25,5)

#x軸刻度
labels = ['0~19','20~39','40~59','60~79','80~100']    

#畫出長條圖

plt.bar(index,range_count,width=2)

#設定X軸名稱
plt.xlabel('Range',fontsize = 14)

#設定Y軸名稱
plt.ylabel('Quantity',fontsize = 14)

#設定圖名稱
plt.title('Score ranges count',fontsize = 20)

#輸出圖片檔案

plt.savefig('chart.png')
plt.close()  