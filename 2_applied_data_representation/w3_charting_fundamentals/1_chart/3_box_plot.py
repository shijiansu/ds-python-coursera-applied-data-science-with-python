#!/usr/bin/python
# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import mpl_toolkits.axes_grid1.inset_locator as mpl_il

# 数据
normal_sample = np.random.normal(loc=0.0, scale=1.0, size=10000)
random_sample = np.random.random(size=10000)
gamma_sample = np.random.gamma(2, size=10000)

df = pd.DataFrame({'normal': normal_sample,
                   'random': random_sample,
                   'gamma': gamma_sample})
df.describe()


plt.figure()
# create a boxplot of the normal data, assign the output to a variable to supress output
_ = plt.boxplot(df['normal'], whis='range')
plt.show()

# 例子 2:
# clear the current figure
plt.clf()
# plot boxplots for all three of df's columns
_ = plt.boxplot([df['normal'], df['random'], df['gamma']], whis='range')
plt.figure()
_ = plt.hist(df['gamma'], bins=100)
plt.show()

# 例子 3:
plt.figure()
plt.boxplot([df['normal'], df['random'], df['gamma']], whis='range')
# overlay axis on top of another
ax2 = mpl_il.inset_axes(plt.gca(), width='60%', height='40%', loc=2)
ax2.hist(df['gamma'], bins=100)
ax2.margins(x=0.5)
plt.show()

# 例子 4:
# switch the y axis ticks for ax2 to the right side
ax2.yaxis.tick_right()
# if `whis` argument isn't passed, boxplot defaults to showing 1.5*interquartile (IQR) whiskers with outliers
plt.figure()
_ = plt.boxplot([ df['normal'], df['random'], df['gamma'] ] )
plt.show()
