#!/usr/bin/python
# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 数据
np.random.seed(123)

df = pd.DataFrame({'A': np.random.randn(365).cumsum(0),
                   'B': np.random.randn(365).cumsum(0) + 20,
                   'C': np.random.randn(365).cumsum(0) - 20},
                  index=pd.date_range('1/1/2017', periods=365))
print(df.head())

# 例子 1:
df.plot()
plt.show()

# 例子 2:
df.plot('A','B', kind = 'scatter')
plt.show()

# 例子 3:
# create a scatter plot of columns 'A' and 'C', with changing color (c) and size (s) based on column 'B'
df.plot.scatter('A', 'C', c='B', s=df['B'], colormap='viridis')
plt.show()

# 例子 4:
ax = df.plot.scatter('A', 'C', c='B', s=df['B'], colormap='viridis')
ax.set_aspect('equal')
plt.show()

# 例子 5:
df.plot.box()
plt.show()

# 例子 6:
df.plot.hist(alpha=0.7)
plt.show()

# 例子 7:
df.plot.kde()
plt.show()
