# -*- coding: UTF-8 -*-
import numpy as np
import pandas as pd

df = pd.read_csv('data/census.csv')
df = df[df['SUMLEV'] == 50]
print(df.head(1))

print('----------------------------------------')

for state in df['STNAME'].unique():
    avg = np.average(df.where(df['STNAME'] == state).dropna()['CENSUS2010POP'])
    print('Counties in state ' + state + ' have an average population of ' + str(avg))

df = df.set_index('STNAME')

print('----------------------------------------')


def fun(item):
    if item[0] < 'M':
        return 0
    if item[0] < 'Q':
        return 1
    return 2


for group, frame in df.groupby(fun):
    print('There are ' + str(len(frame)) + ' records in group ' + str(group) + ' for processing.')
    # There are 1177 records in group 0 for processing.
    # There are 1134 records in group 1 for processing.
    # There are 831 records in group 2 for processing.
