# -*- coding: UTF-8 -*-
import numpy as np
import pandas as pd

# Timestamp
print(pd.Timestamp('9/1/2016 10:05AM'))
# 2016-09-01 10:05:00

# Period
print(pd.Period('1/2016'))
# 2016-01

print(pd.Period('3/5/2016'))
# 2016-03-05

print('----------------------------------------')
# DatetimeIndex
t1 = pd.Series(list('abc'), [pd.Timestamp('2016-09-01'), pd.Timestamp('2016-09-02'), pd.Timestamp('2016-09-03')])
print(t1)
# 2016-09-01    a
# 2016-09-02    b
# 2016-09-03    c
# dtype: object

print(type(t1.index))
# <class 'pandas.tseries.index.DatetimeIndex'>

print('----------------------------------------')
# PeriodIndex
t2 = pd.Series(list('def'), [pd.Period('2016-09'), pd.Period('2016-10'), pd.Period('2016-11')])
print(t2)
# 2016-09    d
# 2016-10    e
# 2016-11    f
# Freq: M, dtype: object

print(type(t2.index))
# <class 'pandas.tseries.period.PeriodIndex'>

print('----------------------------------------')
# Converting to Datetime
d1 = ['2 June 2013', 'Aug 29, 2014', '2015-06-26', '7/12/16']
ts3 = pd.DataFrame(np.random.randint(10, 100, (4, 2)), index=d1, columns=list('ab'))
print(ts3)
#                a   b
# 2 June 2013   36  96
# Aug 29, 2014  35  77
# 2015-06-26    95  44
# 7/12/16       60  27

ts3.index = pd.to_datetime(ts3.index)
print(ts3)
#              a   b
# 2013-06-02  36  96
# 2014-08-29  35  77
# 2015-06-26  95  44
# 2016-07-12  60  27

print('----------------------------------------')
print(pd.to_datetime('4.7.12', dayfirst=True))
# 2012-07-04 00:00:00

# Timedeltas
print(pd.Timestamp('9/3/2016') - pd.Timestamp('9/1/2016'))
# 2 days 00:00:00

print(pd.Timestamp('9/2/2016 8:10AM') + pd.Timedelta('12D 3H'))
# 2016-09-14 11:10:00
