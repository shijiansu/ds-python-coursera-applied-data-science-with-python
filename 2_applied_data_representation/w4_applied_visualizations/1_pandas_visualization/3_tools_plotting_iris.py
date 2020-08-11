#!/usr/bin/python
# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

iris = pd.read_csv('data/iris.csv')
print(iris.head())
#    SepalLength  SepalWidth  PetalLength  PetalWidth         Name
# 0          5.1         3.5          1.4         0.2  Iris-setosa
# 1          4.9         3.0          1.4         0.2  Iris-setosa
# 2          4.7         3.2          1.3         0.2  Iris-setosa
# 3          4.6         3.1          1.5         0.2  Iris-setosa
# 4          5.0         3.6          1.4         0.2  Iris-setosa

# 例子 1:
pd.tools.plotting.scatter_matrix(iris)
plt.show()

# 例子 2:
plt.figure()
pd.tools.plotting.parallel_coordinates(iris, 'Name');
plt.show()
