# -*- coding: UTF-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dates = pd.date_range('10-01-2016', periods=9, freq='2W-SUN')
print(dates)
# DatetimeIndex(['2016-10-02', '2016-10-16', '2016-10-30', '2016-11-13',
#                '2016-11-27', '2016-12-11', '2016-12-25', '2017-01-08',
#                '2017-01-22'],
#               dtype='datetime64[ns]', freq='2W-SUN')

print('----------------------------------------')
df = pd.DataFrame({'Count 1': 100 + np.random.randint(-5, 10, 9).cumsum(),
                   'Count 2': 120 + np.random.randint(-5, 10, 9)}, index=dates)
print(df)
#             Count 1  Count 2
# 2016-10-02      101      120
# 2016-10-16       96      120
# 2016-10-30      103      117
# 2016-11-13      101      120
# 2016-11-27      102      116
# 2016-12-11      107      127
# 2016-12-25      111      128
# 2017-01-08      119      126
# 2017-01-22      120      116

print('----------------------------------------')
print(df.index.weekday_name)
# ['Sunday' 'Sunday' 'Sunday' 'Sunday' 'Sunday' 'Sunday' 'Sunday' 'Sunday' 'Sunday']

print('----------------------------------------')
print(df.diff())
#             Count 1  Count 2
# 2016-10-02      NaN      NaN
# 2016-10-16     -5.0      0.0
# 2016-10-30      7.0     -3.0
# 2016-11-13     -2.0      3.0
# 2016-11-27      1.0     -4.0
# 2016-12-11      5.0     11.0
# 2016-12-25      4.0      1.0
# 2017-01-08      8.0     -2.0
# 2017-01-22      1.0    -10.0

print('----------------------------------------')
print(df.resample('M').mean())
#             Count 1  Count 2
# 2016-10-31    100.0    119.0
# 2016-11-30    101.5    118.0
# 2016-12-31    109.0    127.5
# 2017-01-31    119.5    121.0

print('----------------------------------------')
print(df['2017'])
#             Count 1  Count 2
# 2017-01-08      119      126
# 2017-01-22      120      116

print(df['2016-12'])
#             Count 1  Count 2
# 2016-12-11      107      127
# 2016-12-25      111      128

print(df['2016-12':])
#             Count 1  Count 2
# 2016-12-11      107      127
# 2016-12-25      111      128
# 2017-01-08      119      126
# 2017-01-22      120      116

print('----------------------------------------')
print(df.asfreq('W', method='ffill'))
#             Count 1  Count 2
# 2016-10-02      101      120
# 2016-10-09      101      120
# 2016-10-16       96      120
# 2016-10-23       96      120
# 2016-10-30      103      117
# 2016-11-06      103      117
# 2016-11-13      101      120
# 2016-11-20      101      120
# 2016-11-27      102      116
# 2016-12-04      102      116
# 2016-12-11      107      127
# 2016-12-18      107      127
# 2016-12-25      111      128
# 2017-01-01      111      128
# 2017-01-08      119      126
# 2017-01-15      119      126
# 2017-01-22      120      116

print('----------------------------------------')
df.plot()
plt.show()
