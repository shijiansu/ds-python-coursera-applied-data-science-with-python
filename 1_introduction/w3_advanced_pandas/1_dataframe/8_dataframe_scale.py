# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np

df = pd.DataFrame(['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D'],
                  index=['excellent', 'excellent', 'excellent', 'good', 'good', 'good', 'ok', 'ok', 'ok', 'poor',
                         'poor'])
df.rename(columns={0: 'Grades'}, inplace=True)
print(df)
#           Grades
# excellent     A+
# excellent      A
# excellent     A-
# good          B+
# good           B
# good          B-
# ok            C+
# ok             C
# ok            C-
# poor          D+
# poor           D

print('----------------------------------------')
print(df['Grades'].astype('category').head())
# excellent    A+
# excellent     A
# excellent    A-
# good         B+
# good          B
# Name: Grades, dtype: category
# Categories (11, object): [A, A+, A-, B, ..., C+, C-, D, D+]

print('----------------------------------------')
grades = df['Grades'].astype('category',
                             categories=['D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+'],
                             ordered=True)
print(grades.head(1))
# excellent    A+
# Name: Grades, dtype: category
# Categories (11, object): [D < D+ < C- < C ... B+ < A- < A < A+]

print('----------------------------------------')
print(grades > 'C')
# excellent     True
# excellent     True
# excellent     True
# good          True
# good          True
# good          True
# ok            True
# ok           False
# ok           False
# poor         False
# poor         False
# Name: Grades, dtype: bool

print('----------------------------------------')
df = pd.read_csv('data/census.csv')
df = df[df['SUMLEV'] == 50]
df = df.set_index('STNAME').groupby(level=0)['CENSUS2010POP'].agg({'avg': np.average})
print(pd.cut(df['avg'], 10))
# STNAME
# Alabama                  (11706.0871, 75333.413]
# Alaska                   (11706.0871, 75333.413]
# Arizona                 (390320.176, 453317.529]
