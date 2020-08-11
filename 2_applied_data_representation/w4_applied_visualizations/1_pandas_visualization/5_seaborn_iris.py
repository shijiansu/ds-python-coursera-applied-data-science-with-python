#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 数据
iris = pd.read_csv('data/iris.csv')
print(iris.head())

# 例子 1:
sns.pairplot(iris, hue='Name', diag_kind='kde', size=2);
plt.show()

# 例子 2:
plt.figure(figsize=(8,6))
plt.subplot(121)
sns.swarmplot('Name', 'PetalLength', data=iris);
plt.subplot(122)
sns.violinplot('Name', 'PetalLength', data=iris);
plt.show()
