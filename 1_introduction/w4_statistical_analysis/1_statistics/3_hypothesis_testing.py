# -*- coding: UTF-8 -*-
from __future__ import division

import pandas as pd
from scipy import stats

df = pd.read_csv('data/grades.csv')
print(len(df))
# 2315

print('----------------------------------------')
early = df[df['assignment1_submission'] <= '2015-12-31']
late = df[df['assignment1_submission'] > '2015-12-31']

print(early.mean())
# assignment1_grade    74.972741
# assignment2_grade    67.252190
# assignment3_grade    61.129050
# assignment4_grade    54.157620
# assignment5_grade    48.634643
# assignment6_grade    43.838980
# dtype: float64

print('----------------------------------------')
print(late.mean())
# assignment1_grade    74.017429
# assignment2_grade    66.370822
# assignment3_grade    60.023244
# assignment4_grade    54.058138
# assignment5_grade    48.599402
# assignment6_grade    43.844384
# dtype: float64

print('----------------------------------------')
t = stats.ttest_ind(early['assignment1_grade'], late['assignment1_grade'])
print(t)
# Ttest_indResult(statistic=1.400549944897566, pvalue=0.16148283016060577)

t = stats.ttest_ind(early['assignment2_grade'], late['assignment2_grade'])
print(t)
# Ttest_indResult(statistic=1.3239868220912567, pvalue=0.18563824610067967)

t = stats.ttest_ind(early['assignment3_grade'], late['assignment3_grade'])
print(t)
# Ttest_indResult(statistic=1.7116160037010733, pvalue=0.087101516341556676)
