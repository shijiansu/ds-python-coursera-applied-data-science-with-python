# -*- coding: UTF-8 -*-
from __future__ import division
import numpy as np

d = np.random.binomial(1, 0.5)
print(d)
# 0

d = np.random.binomial(1000, 0.5) / 1000
print(d)
# 0.51

chance_of_tornado = 0.01 / 100
d = np.random.binomial(100000, chance_of_tornado)
print(d)
# 12

print('----------------------------------------')
chance_of_tornado = 0.01
tornado_events = np.random.binomial(1, chance_of_tornado, 1000000)
two_days_in_a_row = 0
for j in range(1, len(tornado_events) - 1):
    if tornado_events[j] == 1 and tornado_events[j - 1] == 1:
        two_days_in_a_row += 1

print('{} tornadoes back to back in {} years'.format(two_days_in_a_row, 1000000 / 365))
# 115 tornadoes back to back in 2739.7260274 years

print('----------------------------------------')
d = np.random.uniform(0, 1)
print(d)
# 0.471860353766

d = np.random.normal(0.75)
print(d)
# -0.0955424780214

print('----------------------------------------')
# standard deviation
distribution = np.random.normal(0.75, size=1000)
s = np.sqrt(np.sum((np.mean(distribution) - distribution) ** 2) / len(distribution))
print(s)
# 0.99620559072

s = np.std(distribution)
print(s)
# 0.99620559072
