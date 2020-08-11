#!/usr/bin/python
# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt

import numpy as np
import pandas as pd

# 数据
# 相当于X
linear_data = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# 相当于Y
exponential_data = linear_data ** 2

# 例子 1:
plt.figure()
# plot the linear data and the exponential data
plt.plot(linear_data, '-o', exponential_data, '-o')
plt.show()

# 例子 2:
# plot another series with a dashed red line
plt.plot([22, 44, 55], '--r')

plt.xlabel('Some data')
plt.ylabel('Some other data')
plt.title('A title')
# add a legend with legend entries (because we didn't have labels when we plotted the data series)
plt.legend(['Baseline', 'Competition', 'Us'])
plt.show()

# 例子 3:
# fill the area between the linear data and exponential data
plt.gca().fill_between(range(len(linear_data)),
                       linear_data, exponential_data,
                       facecolor='blue',
                       alpha=0.25)
plt.show()

# 例子 4:
plt.figure()
observation_dates = np.arange('2017-01-01', '2017-01-09', dtype='datetime64[D]')
observation_dates = list(map(pd.to_datetime, observation_dates))  # convert the map to a list to get rid of the error
plt.plot(observation_dates, linear_data, '-o', observation_dates, exponential_data, '-o')

x = plt.gca().xaxis
# rotate the tick labels for the x axis
for item in x.get_ticklabels():
    item.set_rotation(45)

# adjust the subplot so the text doesn't run off the image
plt.subplots_adjust(bottom=0.25)

ax = plt.gca()
ax.set_xlabel('Date')
ax.set_ylabel('Units')
ax.set_title('Exponential vs. Linear performance')

# you can add mathematical expressions in any text element
ax.set_title("Exponential ($x^2$) vs. Linear ($x$) performance")

plt.show()
