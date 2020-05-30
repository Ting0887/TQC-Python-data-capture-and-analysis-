# -*- coding: utf-8 -*-
"""
Created on Fri May 29 16:22:58 2020

@author: user
"""

import pandas as pd

datas = [[9, 203674, 13.2, 18894],
         [11.7, 180785, 12.3, 54894],
         [10.1, 127802, 14.7, 18563],
         [11.8, 28604, 14.9, 21963],
         [13.2, 600, 13.1, 900],
         [6.9, 38071, 9.6, 3555],
         [12.1, 35660, 10.6, 9005],
         [12, 15000, 13, 12000],
         [11.7, 48770, 9.1, 14370],
         [9.84, 6100, 11.89, 8980]]

indexs = ["三重市", "台中市", "台北一", "台北二", "台東市",
          "板橋區", "高雄市", "嘉義市", "鳳山區", "豐原區"]
columns = ["西瓜價", "西瓜量", "香瓜價", "香瓜量"]

print('西瓜與香瓜之拍價行情價量表')
df = pd.DataFrame(datas ,columns = columns , index = indexs)
print(df)
print()

print('以西瓜價遞減排序')
df1 = df.sort_values(by = '西瓜價',ascending = False)
print(df1['西瓜價'])
print()

print('台北一市場的行情')
df2 = df.loc["台北一",:]
print(df2)
print()

df3 = df.rename(index = {"三重市":"三重區"},columns = {"香瓜價":"洋香瓜價","香瓜量":"洋香瓜量"})
print('全體市價行情')
print(df3)

#indexs[0] = '三重區'
#df.index = indexs
#columns[2] = '洋香瓜價'
#columns[3] = '洋香瓜量'
#df.columns = columns
#print('全體市場行情')
#print(df)





