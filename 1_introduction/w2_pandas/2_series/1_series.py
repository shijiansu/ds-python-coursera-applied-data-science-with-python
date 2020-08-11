# -*- coding: UTF-8 -*-
import numpy as np
import pandas as pd

# pd.Series?

animals = ['Tiger', 'Bear', 'Moose']
print(pd.Series(animals))
# 0    Tiger
# 1     Bear
# 2    Moose
# dtype: object

print(pd.Series(animals).append('aaaa'))


numbers = [1, 2, 3]
print(pd.Series(numbers))
# 0    1
# 1    2
# 2    3
# dtype: int64

animals = ['Tiger', 'Bear', None]
print(pd.Series(animals))
# 0    Tiger
# 1     Bear
# 2     None
# dtype: object

numbers = [1, 2, None]
print(pd.Series(numbers))
# 0    1.0
# 1    2.0
# 2    NaN
# dtype: float64

print('----------------------------------------')
print(np.nan is None)
# False
print(np.nan == np.nan)
# False
print(np.isnan(np.nan))
# True

print('----------------------------------------')
# convert list to series
animals = ['Tiger', 'Bear', 'Moose']
s = pd.Series(animals, index=['India', 'America', 'Canada'])
print(s)
# India      Tiger
# America     Bear
# Canada     Moose
# dtype: object

print('----------------------------------------')
# convert map to series
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

print('----------------------------------------')
print(s.index)
# Index(['Archery', 'Golf', 'Sumo', 'Taekwondo'], dtype='object')

print('----------------------------------------')
# convert map to series - replace indexes
sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports, index=['Golf', 'Sumo', 'Hockey'])
print(s)
# Golf      Scotland
# Sumo         Japan
# Hockey         NaN
# dtype: object
