# -*- coding: utf-8 -*-
"""
Created on Thu May 28 22:28:50 2020

@author: user
"""
import requests
from bs4 import BeautifulSoup


url = 'http://tqc.codejudger.com:3000/target/5203.html'

html = requests.get(url)

objsoup = BeautifulSoup(html.text,'lxml')

dataTag = objsoup.select('.contents_box02')

balls = dataTag[2].find_all('div',{'class':'ball_tx ball_yellow'})

print('大樂透開獎 : ')
print('-------------')

print('開出順序 :',end =' ')
for i in range(6):
    print(balls[i].text,end = ' ')
    
    
print('\n大小順序 :',end =' ')
for i in range(6,len(balls)):
    print(balls[i].text,end = ' ')

print('\n特別號  ：',end = ' ')
redball = dataTag[2].find_all('div',{'class':'ball_red'})
print(redball[0].text,end =' ')    
    
