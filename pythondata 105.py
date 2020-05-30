# -*- coding: utf-8 -*-
"""
Created on Thu May 28 21:17:36 2020

@author: user
"""

import sqlite3

conn = sqlite3.connect('read105.db')

cursor = conn.cursor()

cursor.execute('Select * From employee')

for row in cursor:
    print(row)
    
conn.close()    