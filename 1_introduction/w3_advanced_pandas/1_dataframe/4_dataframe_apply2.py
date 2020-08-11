# -*- coding: UTF-8 -*-
import numpy as np
import pandas as pd

df = pd.read_csv('data/census.csv')
print(df.head(1))
print('')


def min_max(row):
    data = row[['POPESTIMATE2010',
                'POPESTIMATE2011',
                'POPESTIMATE2012',
                'POPESTIMATE2013',
                'POPESTIMATE2014',
                'POPESTIMATE2015']]
    row['max'] = np.max(data)
    row['min'] = np.min(data)
    return row[['max', 'min']]


df = df.apply(min_max, axis=1)

print(df.head(1))
#        max      min
# 0  4858979  4785161
