#!/usr/bin/python
# -*- coding:utf-8 -*-

# pip install seaborn


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 数据
np.random.seed(1234)

v1 = pd.Series(np.random.normal(0, 10, 1000), name='v1')
v2 = pd.Series(2 * v1 + np.random.normal(60, 15, 1000), name='v2')

# 例子 1:
plt.figure()
plt.hist(v1, alpha=0.7, bins=np.arange(-50, 150, 5), label='v1');
plt.hist(v2, alpha=0.7, bins=np.arange(-50, 150, 5), label='v2');
plt.legend();
plt.show()

# 例子 2:
# plot a kernel density estimation over a stacked barchart
plt.figure()
plt.hist([v1, v2], histtype='barstacked', normed=True);
v3 = np.concatenate((v1, v2))
sns.kdeplot(v3);
plt.show()

# 例子 3:
plt.figure()
# we can pass keyword arguments for each individual component of the plot
sns.distplot(v3, hist_kws={'color': 'Teal'}, kde_kws={'color': 'Navy'});
plt.show()

# 例子 4:
sns.jointplot(v1, v2, alpha=0.4);
plt.show()

# 例子 5:
grid = sns.jointplot(v1, v2, alpha=0.4);
grid.ax_joint.set_aspect('equal')
plt.show()

# 例子 6:
sns.jointplot(v1, v2, kind='hex');
plt.show()

# 例子 7:
# set the seaborn style for all the following plots
sns.set_style('white')
sns.jointplot(v1, v2, kind='kde', space=0);
plt.show()
