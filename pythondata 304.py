# -*- coding: utf-8 -*-
"""
Created on Fri May 29 16:51:44 2020

@author: user
"""

import numpy as np
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/vincenttang1227/PythonProj/master/File/304/read.csv')

data = df["data"].values
print(data)

#判斷資料型態
print(type(data))

#平均數
print('平均值:%.2f'%np.mean(data))
#中位數
print('中位數:%.2f'%np.median(data))
#標準差
print('標準差:%.2f'%np.std(data))
#變異數
print('變異數:%.2f'%np.var(data))
#極差值
print('極差值:%.2f'%np.ptp(data))