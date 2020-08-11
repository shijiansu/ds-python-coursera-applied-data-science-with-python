# -*- coding: UTF-8 -*-
import numpy as np

# Creating Arrays
print('----------------------------------------')
mylist = [1, 2, 3]
x = np.array(mylist)
print(x)
# [1 2 3]

y = np.array([4, 5, 6])
print(y)
# [4 5 6]

m = np.array([[7, 8, 9], [10, 11, 12]])
print(m)
# [[ 7  8  9]
#  [10 11 12]]

print(m.shape)
# (2L, 3L)

print('----------------------------------------')
n = np.arange(0, 30, 2)  # start at 0 count up by 2, stop before 30
print(n)
# [ 0  2  4  6  8 10 12 14 16 18 20 22 24 26 28]
n = n.reshape(3, 5)  # reshape array to be 3x5
print(n)
# [[ 0  2  4  6  8]
#  [10 12 14 16 18]
#  [20 22 24 26 28]]

o = np.linspace(0, 4, 9)  # return 9 evenly spaced values from 0 to 4
print(o)
# [ 0.   0.5  1.   1.5  2.   2.5  3.   3.5  4. ]
o.resize(3, 3)
print(o)
# [[ 0.   0.5  1. ]
#  [ 1.5  2.   2.5]
#  [ 3.   3.5  4. ]]

print('----------------------------------------')
print(np.ones((3, 2)))
# [[ 1.  1.]
#  [ 1.  1.]
#  [ 1.  1.]]
print(np.zeros((2, 3)))
# [[ 0.  0.  0.]
#  [ 0.  0.  0.]]
print(np.eye(3))
# [[ 1.  0.  0.]
#  [ 0.  1.  0.]
#  [ 0.  0.  1.]]
print(np.diag(y))
# [[4 0 0]
#  [0 5 0]
#  [0 0 6]]
print(np.array([1, 2, 3] * 3))
# [1 2 3 1 2 3 1 2 3]
print(np.repeat([1, 2, 3], 3))
# [1 1 1 2 2 2 3 3 3]

# Combining Arrays
print('----------------------------------------')
p = np.ones([2, 3], int)
print(p)
# [[1 1 1]
#  [1 1 1]]
print(np.vstack([p, 2 * p]))
# [[1 1 1]
#  [1 1 1]
#  [2 2 2]
#  [2 2 2]]
print(np.hstack([p, 2 * p]))
# [[1 1 1 2 2 2]
#  [1 1 1 2 2 2]]
