#!/usr/bin/python
# -*- coding:utf-8 -*-

# Assignment 3 - Building a Custom Visualization
# In this assignment you must choose one of the options presented below and submit a visual as well as your source code
# for peer grading. The details of how you solve the assignment are up to you, although your assignment
# must use matplotlib so that your peers can evaluate your work. The options differ in challenge level,
# but there are no grades associated with the challenge level you chose. However, your peers will be
# asked to ensure you at least met a minimum quality for a given technique in order to pass. Implement
# the technique fully (or exceed it!) and you should be able to earn full grades for the assignment.
#
#   Ferreira, N., Fisher, D., & Konig, A. C. (2014, April).
#   Sample-oriented task-driven visualizations: allowing users to make better, more confident decisions.
#   In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (pp. 571-580). ACM. (video)
#
# In this paper the authors describe the challenges users face when trying to make judgements about
# probabilistic data generated through samples. As an example, they look at a bar chart of
# four years of data (replicated below in Figure 1). Each year has a y-axis value,
# which is derived from a sample of a larger dataset. For instance,
# the first value might be the number votes in a given district or riding for 1992,
# with the average being around 33,000. On top of this is plotted the 95% confidence interval for the mean
# (see the boxplot lectures for more information, and the yerr parameter of barcharts).
#
# A challenge that users face is that, for a given y-axis value (e.g. 42,000),
# it is difficult to know which x-axis values are most likely to be representative,
# because the confidence levels overlap and their distributions are different
# (the lengths of the confidence interval bars are unequal).
# One of the solutions the authors propose for this problem (Figure 2c)
# is to allow users to indicate the y-axis value of interest (e.g. 42,000) and then draw a horizontal line
# and color bars based on this value. So bars might be colored red if they are definitely above
# this value (given the confidence interval), blue if they are definitely below this value,
# or white if they contain this value.
#
# Easiest option: Implement the bar coloring as described above - a color scale with only three colors,
# (e.g. blue, white, and red). Assume the user provides the y axis value of interest as a parameter or variable.
# 1) Harder option: Implement the bar coloring as described in the paper, where the color of the bar is
# actually based on the amount of data covered (e.g. a gradient ranging from dark blue for the distribution
# being certainly below this y-axis, to white if the value is certainly contained, to dark red if the value
# is certainly not contained as the distribution is above the axis).
# 2) Even Harder option: Add interactivity to the above, which allows the user to click on the
# y axis to set the value of interest. The bar colors should change with respect to what value the user has selected.
# 3) Hardest option: Allow the user to interactively set a range of y values they are interested in,
# and recolor based on this (e.g. a y-axis band, see the paper for more details).
#
# Note: The data given for this assignment is not the same as the data used in the article
# and as a result the visualizations may look a little different.
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.colors as mcol
import matplotlib.cm as cm

np.random.seed(12345)

# 正态分布
# loc : float or array_like of floats. Mean (“centre”) of the distribution. 均值
# scale : float or array_like of floats. Standard deviation (spread or “width”) of the distribution. 标准差
# size : int or tuple of ints, optional. Output shape.
# 可以看到, 其mu值是不知道的
df = pd.DataFrame([np.random.normal(32000, 200000, 3650),
                   np.random.normal(43000, 100000, 3650),
                   np.random.normal(43500, 140000, 3650),
                   np.random.normal(48000, 70000, 3650)],
                  index=[1992, 1993, 1994, 1995])

# 数据
threshold = 42000
n = df.shape[1]  # 3650列

mean = df.mean(axis=1)  # 依照行, 求列(axis=1)的均值. 由于数据带有随机性, 所以不完全等于使用np.random.normal的参数值
print('\nmean:')
print(mean)

std = df.std(axis=1)
print('\nstd:')
print(std)

yerr = -1 * std / np.sqrt(n) * stats.t.ppf(0.05 / 2, n - 1)  # 参见本目录下的公式截图 -> 这个得出来是负数, 所以除以-1
print('\nyerr:')
print(yerr)

# 颜色渐变 (百分比)
percentages = []
for m, y in zip(mean, yerr):
    highest = m + y
    lowest = m - y
    # 这个是自己总结出来的式子, 就是说
    percentage = 1 - ((threshold - lowest) / (highest - lowest))
    # 这里是处理肯定超过或者低过的情况
    if percentage > 1:
        percentage = 1
    if percentage < 0:
        percentage = 0
    percentages.append(percentage)

print('\npercentages:')
print(percentages)  # [0, 0.79153005817114697, 0.44438436907669399, 1]

# 颜色列表
cmap = mcol.LinearSegmentedColormap.from_list('myColors', ['darkblue', 'blue', 'white', 'red', 'darkred'])  # 渐变
cpick = cm.ScalarMappable(cmap=cmap)
cpick.set_array([])

# 显示数据
plt.bar(range(df.shape[0]), mean, width=0.3,
        yerr=yerr.values, ecolor='grey',
        color=cpick.to_rgba(percentages),
        align="center")
plt.axhline(y=threshold, color='grey', alpha=0.8)
plt.colorbar(cpick, orientation='horizontal')
plt.xticks(range(df.shape[0]), df.index, alpha=0.8)
plt.show()
