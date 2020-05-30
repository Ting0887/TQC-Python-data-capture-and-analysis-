# -*- coding: utf-8 -*-
"""
Created on Fri May 29 16:02:53 2020

@author: user
"""
set_seed = 123

import numpy as np
#請用numpy隨機產生5-15之間，15個正整數並輸出
x = np.random.RandomState(set_seed).randint(low = 5, high = 16, size=15)
print('隨機正整數:',x)

#請將1.轉成3*5的X矩陣並輸出
print('X矩陣內容:')
matrix = x.reshape(3,5)
print(matrix)

#請輸出X矩陣的最大值
print('最大:',matrix.max())

#請輸出X矩陣的最小值
print('最小:',matrix.min())

#請輸出X矩陣的總和
print('總和:',matrix.sum())

#請輸出X矩陣四個角落的元素
print('四個角落元素:')
print(matrix[np.ix_([0,2],[0,4])])



