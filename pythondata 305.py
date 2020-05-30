# -*- coding: utf-8 -*-
"""
Created on Fri May 29 17:06:58 2020

@author: user
"""

import pandas as pd

df1 = pd.read_csv('https://raw.githubusercontent.com/vincenttang1227/PythonProj/master/File/305/read.csv',encoding='utf-8',sep=',',header = 0)

#以遞減順序顯示居住縣市的病例人數
df_county = df1.groupby("居住縣市")["居住縣市"].count()
print(df_county.sort_values(ascending=False))
#顯示感染病例人數最多的５個國家，並按照遞減順序顯示
df_country = df1.groupby("感染國家")["感染國家"].count()
print(df_country.sort_values(ascending=False).head(5))
#顯示台北市各區病例人數
df_taipei = df1[df1.居住縣市 == "台北市"]
print(df_taipei.groupby("居住鄉鎮")["居住鄉鎮"].count())
#顯示台北市最近病例的日期
print(df_taipei.發病日.max())



