# -*- coding: utf-8 -*-
"""
Created on Fri May 29 20:48:54 2020

@author: user
"""
import matplotlib as mpl
mpl.use('Agg')

import matplotlib.pyplot as plt

data1 = [1, 4, 9, 16, 25, 36, 49, 64]
data2 = [1, 2, 3, 6, 9, 15, 24, 39]
seq = [1, 2, 3, 4, 5, 6, 7, 8]

#數據及線條設定
#plt.plot(seq,data1,'--b.',seq,data2,'--r.')
plt.plot(seq,data1,'b--.',seq,data2,'r--.')

#X軸刻度
plt.axis([0,8,0,70])

#圖表標題
plt.title("Figure",fontsize=24)

#X軸標題
plt.xlabel("x-Value",fontsize=16)

#Y軸標題
plt.ylabel("y-Value",fontsize=16)

#輸出圖片檔案
plt.savefig('chart.png')
plt.close()