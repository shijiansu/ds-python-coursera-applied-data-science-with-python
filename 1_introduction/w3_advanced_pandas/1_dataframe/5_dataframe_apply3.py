# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np

df = pd.read_csv('data/census.csv')
print(df.head(1))
print('')

rows = ['POPESTIMATE2010',
        'POPESTIMATE2011',
        'POPESTIMATE2012',
        'POPESTIMATE2013',
        'POPESTIMATE2014',
        'POPESTIMATE2015']

df = df.apply(lambda x: np.max(x[rows]), axis=1)

print(df.head(1))
# 0    4858979
# dtype: int64
