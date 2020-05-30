# -*- coding: utf-8 -*-
"""
Created on Thu May 28 17:46:13 2020

@author: user
"""

import json
import yaml

file = open('read103.json',encoding='utf-8')

data = json.load(file)

f = open('write.yaml','w',encoding='utf-8')

yaml.dump(data,f,default_flow_style=False,allow_unicode=True)