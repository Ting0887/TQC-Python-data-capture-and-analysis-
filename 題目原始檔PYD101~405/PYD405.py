# -*- coding: utf-8 -*-
"""
Created on Sun May 31 10:58:22 2020

@author: user
"""

# --開始--批改評分使用，請勿變動
import matplotlib as mpl
mpl.use('Agg')
set_seed = 123
# --結束--批改評分使用，請勿變動

# 載入 numpy 模組並縮寫為 np
import ___ as ___
# 載入 matplotlib.pyplot 並縮寫為 plt
import ___ as ___

samples_1 = np.random.RandomState(set_seed).normal(loc=1, scale=.5, size=1000)
samples_2 = np.random.RandomState(set_seed).standard_t(df=10, size=1000)
bins = np.linspace(___,___,___)

# 第一個子圖
plt.subplot(___,___,___)
plt.hist(_____, bins=____, alpha=____, label=______)
plt.hist(_____, bins=____, alpha=____, label=______)
# 在左上角 upper left 放置圖例 legend
plt.______(loc='______')

# 第二個子圖
plt.subplot(___,___,___)
plt.scatter(_____,_____, alpha=____)

plt.savefig(____)
plt.close()
