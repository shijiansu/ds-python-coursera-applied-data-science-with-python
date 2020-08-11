#!/usr/bin/python
# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

# 数据
Y = np.random.normal(loc=0.0, scale=1.0, size=10000)
X = np.random.random(size=10000)

# 例子 1:
plt.figure()
_ = plt.hist2d(X, Y, bins=25)
plt.show()

# 例子 2:
plt.figure()
_ = plt.hist2d(X, Y, bins=100)
# add a colorbar legend
plt.colorbar()
plt.show()
