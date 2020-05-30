# -*- coding: utf-8 -*-
"""
Created on Fri May 29 22:30:50 2020

@author: user
"""

import matplotlib as mpl
mpl.use('Agg')
set_seed = 123

import numpy as np
import matplotlib.pyplot as plt

sample_1 = np.random.RandomState(set_seed).normal(loc = 1,scale=.5,size=1000)
sample_2 = np.random.RandomState(set_seed).standard_t(df = 10, size=1000)

bins = np.linspace(-3,3,100)

#第一個子圖
plt.subplot(2,2,1)
plt.hist(sample_1,bins=bins,alpha=0.5,label='samples 1')
plt.hist(sample_2,bins=bins,alpha=0.5,label='samples 2')

#在左上角圖例upper left放置legend

plt.legend(loc='upper left')

#第二個子圖
plt.subplot(1,2,2)
plt.scatter(sample_1,sample_2,alpha=0.2)



plt.savefig('chart.png')
plt.close()