# -*- coding: UTF-8 -*-
import numpy as np
import pandas as pd
import time as tm

sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports)
print(s)
# Archery           Bhutan
# Golf            Scotland
# Sumo               Japan
# Taekwondo    South Korea
# dtype: object
print(s.iloc[3])  # 'South Korea'
print(s.loc['Golf'])  # 'Scotland'
print(s[3])  # 'South Korea'
print(s['Golf'])  # 'Scotland'

print('----------------------------------------')
sports = {99: 'Bhutan',
          100: 'Scotland',
          101: 'Japan',
          102: 'South Korea'}
s = pd.Series(sports)
print(s)
# 99          Bhutan
# 100       Scotland
# 101          Japan
# 102    South Korea
# dtype: object

print('----------------------------------------')
s = pd.Series([100.00, 120.00, 101.00, 3.00])
print(s)
# 0    100.0
# 1    120.0
# 2    101.0
# 3      3.0
# dtype: float64

print('----------------------------------------')
# aggregation
print('Sum')
s = pd.Series([100.00, 120.00, 101.00, 3.00])
total = 0

# 求和方式1
for item in s:
    total += item
print(total)  # 324.0

# 求和方式2
total = np.sum(s)
print(total)  # 324.0

print('----------------------------------------')
# 大Series测试性能
print('Sum - Big Series')
s = pd.Series(np.random.randint(0, 1000, 10000))
summary = 0

start = tm.time()
for item in s:
    summary += item
print('Time cost - forloop:{}'.format(str(tm.time() - start) + ' s'))
# Time cost - forloop:0.00200009346008 s

start = tm.time()
summary = np.sum(s)
print('Time cost - sum:{}'.format(str(tm.time() - start) + ' s'))
# Time cost - sum:0.0 s

print('----------------------------------------')
# broadcasting
s = pd.Series([100.00, 120.00, 101.00, 3.00])
s += 2
print(s.head())
# 0    102.0
# 1    122.0
# 2    103.0
# 3      5.0
# dtype: float64

print('----------------------------------------')
# 大Series测试性能
print('Add - Big Series')
s = pd.Series(np.random.randint(0, 1000, 10000))
start = tm.time()
for label, value in s.iteritems():
    s.loc[label] = value + 2
print('Time cost - loc/index:{}'.format(str(tm.time() - start) + ' s'))
# Time cost - loc/index:0.962000131607 s

s = pd.Series(np.random.randint(0, 1000, 10000))
start = tm.time()
for label, value in s.iteritems():
    s.set_value(label, value + 2)
print('Time cost - set_value:{}'.format(str(tm.time() - start) + ' s'))
# Time cost - set_value:0.039999961853 s

s = pd.Series(np.random.randint(0, 1000, 10000))
start = tm.time()
s += 2
print('Time cost - broadcasting:{}'.format(str(tm.time() - start) + ' s'))
# Time cost - broadcasting:0.0 s

print('----------------------------------------')
s = pd.Series([1, 2, 3])
print(s)
# 0    1
# 1    2
# 2    3
# dtype: int64

s.loc['Animal'] = 'Bears'
print(s)
# 0             1
# 1             2
# 2             3
# Animal    Bears
# dtype: object

print('----------------------------------------')
original_sports = pd.Series({'Archery': 'Bhutan',
                             'Golf': 'Scotland',
                             'Sumo': 'Japan',
                             'Taekwondo': 'South Korea'})
cricket_loving_countries = pd.Series(['Australia', 'Barbados', 'Pakistan', 'England'],
                                     index=['Cricket', 'Cricket', 'Cricket', 'Cricket'])
all_countries = original_sports.append(cricket_loving_countries)

print(original_sports)
# Archery           Bhutan
# Golf            Scotland
# Sumo               Japan
# Taekwondo    South Korea
# dtype: object

print('')
print(cricket_loving_countries)
# Cricket    Australia
# Cricket     Barbados
# Cricket     Pakistan
# Cricket      England
# dtype: object

print('')
print(all_countries)
# Archery           Bhutan
# Golf            Scotland
# Sumo               Japan
# Taekwondo    South Korea
# Cricket        Australia
# Cricket         Barbados
# Cricket         Pakistan
# Cricket          England
# dtype: object

print('')
print(all_countries.loc['Cricket'])  # 定位到index
# Cricket    Australia
# Cricket     Barbados
# Cricket     Pakistan
# Cricket      England
# dtype: object
