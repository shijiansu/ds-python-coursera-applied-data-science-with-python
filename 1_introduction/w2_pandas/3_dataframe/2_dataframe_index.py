# -*- coding: UTF-8 -*-
import pandas as pd

print('\nLoading...')
df = pd.read_csv('../data/olympics.csv')
print(df.head(1))
#      0         1     2     3     4      5         6     7     8     9     10  \
# 0  NaN  # Summer  01 !  02 !  03 !  Total  # Winter  01 !  02 !  03 !  Total
#         11    12    13    14              15
# 0  # Games  01 !  02 !  03 !  Combined total

print('----------------------------------------')
df = pd.read_csv('../data/olympics.csv', index_col=0, skiprows=1)
print(df.head(1))
#                    # Summer  01 !  02 !  03 !  Total  # Winter  01 !.1  \
# Afghanistan (AFG)        13     0     0     2      2         0       0
#                    02 !.1  03 !.1  Total.1  # Games  01 !.2  02 !.2  03 !.2  \
# Afghanistan (AFG)       0       0        0       13       0       0       2
#                    Combined total
# Afghanistan (AFG)               2

print('----------------------------------------')
print(df.columns)
# Index([u'# Summer', u'01 !', u'02 !', u'03 !', u'Total', u'# Winter',
#        u'01 !.1', u'02 !.1', u'03 !.1', u'Total.1', u'# Games', u'01 !.2',
#        u'02 !.2', u'03 !.2', u'Combined total'],
#       dtype='object')

print('----------------------------------------')
for col in df.columns:
    if col[:2] == '01':
        df.rename(columns={col: 'Gold' + col[4:]}, inplace=True)
    if col[:2] == '02':
        df.rename(columns={col: 'Silver' + col[4:]}, inplace=True)
    if col[:2] == '03':
        df.rename(columns={col: 'Bronze' + col[4:]}, inplace=True)
    if col[:1] == '№':  # 虽然我在本地修改了数据文件, 但是Coursera服务器上仍是这个, 所以保留
        df.rename(columns={col: '#' + col[1:]}, inplace=True)

print(df.head(1))
#                    # Summer  Gold  Silver  Bronze  Total  # Winter  Gold.1  \
# Afghanistan (AFG)        13     0       0       2      2         0       0
#                    Silver.1  Bronze.1  Total.1  # Games  Gold.2  Silver.2  \
# Afghanistan (AFG)         0         0        0       13       0         0
#                    Bronze.2  Combined total
# Afghanistan (AFG)         2               2

print('\nQuerying...')
print('----------------------------------------')
print(df['Gold'] > 0)  # return True / False
# Afghanistan (AFG)                               False
# Algeria (ALG)                                    True
# Argentina (ARG)                                  True
# Armenia (ARM)                                    True
# Australasia (ANZ) [ANZ]                          True

print('----------------------------------------')
only_gold = df.where(df['Gold'] > 0)
print(only_gold.head(1))
#                    # Summer  Gold  Silver  Bronze  Total  # Winter  Gold.1  \
# Afghanistan (AFG)       NaN   NaN     NaN     NaN    NaN       NaN     NaN
#                    Silver.1  Bronze.1  Total.1  # Games  Gold.2  Silver.2  \
# Afghanistan (AFG)       NaN       NaN      NaN      NaN     NaN       NaN
#                    Bronze.2  Combined total
# Afghanistan (AFG)       NaN             NaN
print(only_gold['Gold'].count())  # 100 # records has Gold > 0
print(df['Gold'].count())  # 147 # all records

print('----------------------------------------')
only_gold = only_gold.dropna()
print(only_gold.head(1))

print('----------------------------------------')
only_gold = df[df['Gold'] > 0]
print(only_gold.head(1))

print('----------------------------------------')
print(len(df[(df['Gold'] > 0) | (df['Gold.1'] > 0)]))
print(df[(df['Gold.1'] > 0) & (df['Gold'] == 0)])

print('\nIndexing...')
print('----------------------------------------')
df['country'] = df.index
df = df.set_index('Gold')  # make column Gold as row's index
print(df.head(1))
#       # Summer  Silver  Bronze  Total  # Winter  Gold.1  Silver.1  Bronze.1  \
# Gold
# 0           13       0       2      2         0       0         0         0
#       Total.1  # Games  Gold.2  Silver.2  Bronze.2  Combined total  \
# Gold
# 0           0       13       0         0         2               2
#                 country
# Gold
# 0     Afghanistan (AFG)

print('----------------------------------------')
df = df.reset_index()
print(df.head(1))
#    Gold  # Summer  Silver  Bronze  Total  # Winter  Gold.1  Silver.1  \
# 0     0        13       0       2      2         0       0         0
#    Bronze.1  Total.1  # Games  Gold.2  Silver.2  Bronze.2  Combined total  \
# 0         0        0       13       0         0         2               2
#              country
# 0  Afghanistan (AFG)
