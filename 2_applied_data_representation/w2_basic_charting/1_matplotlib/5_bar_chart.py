#!/usr/bin/python
# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt

import numpy as np
from random import randint

# 数据
linear_data = np.array([1, 2, 3, 4, 5, 6, 7, 8])
exponential_data = linear_data ** 2
xvals = range(len(linear_data))
new_xvals = []

# plot another set of bars, adjusting the new xvals to make up for the first set of bars plotted
for item in xvals:
    new_xvals.append(item + 0.3)

# 例子 1:
plt.figure()
plt.bar(xvals, linear_data, width=0.3)
plt.show()

# 例子 2:
plt.figure()
plt.bar(new_xvals, exponential_data, width=0.3, color='red')
plt.show()

# 例子 3:
linear_err = [randint(0, 15) for x in range(len(linear_data))]
# This will plot a new set of bars with errorbars using the list of random error values
plt.bar(xvals, linear_data, width=0.3, yerr=linear_err)
plt.show()

# 例子 4:
# stacked bar charts are also possible
plt.figure()
plt.bar(xvals, linear_data, width=0.3, color='b')
plt.bar(xvals, exponential_data, width=0.3, bottom=linear_data, color='r')
plt.show()

# 例子 5:
# or use barh for horizontal bar charts
plt.figure()
plt.barh(xvals, linear_data, height=0.3, color='b')
plt.barh(xvals, exponential_data, height=0.3, left=linear_data, color='r')
plt.show()
