# -*- coding: UTF-8 -*-
from __future__ import division

import numpy as np

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

print(x + y)  # elementwise addition     [1 2 3] + [4 5 6] = [5  7  9]
print(x - y)  # elementwise subtraction  [1 2 3] - [4 5 6] = [-3 -3 -3]
print(x * y)  # elementwise multiplication  [1 2 3] * [4 5 6] = [4  10  18]
print(x / y)  # elementwise divison         [1 2 3] / [4 5 6] = [0.25  0.4  0.5]
print(x ** 2)  # elementwise power  [1 2 3] ^2 =  [1 4 9]

#  Dot Product
print(x.dot(y))  # dot product  1*4 + 2*5 + 3*6 = 32

# T
z = np.array([y, y ** 2])
print(len(z))  # number of rows of array # 2
print(z)
# [[ 4  5  6]
#  [16 25 36]]
print(z.shape)  # (2L, 3L)
print(z.T)
# [[ 4 16]
#  [ 5 25]
#  [ 6 36]]
print(z.T.shape)  # (3L, 2L)

# dtype
print(z.dtype)  # int32
# convert data type to float
z = z.astype('f')
print(z.dtype)  # float32
