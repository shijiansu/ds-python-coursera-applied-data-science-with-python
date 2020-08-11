# -*- coding: UTF-8 -*-
import pandas as pd

df = pd.read_csv('../data/log.csv')
print(df.head(3))
#          time    user       video  playback position paused  volume
# 0  1469974424  cheryl  intro.html                  5  False    10.0
# 1  1469974454  cheryl  intro.html                  6    NaN     NaN
# 2  1469974544  cheryl  intro.html                  9    NaN     NaN

print('----------------------------------------')
df = df.set_index('time')
df = df.sort_index()
print(df.head(3))
#               user          video  playback position paused  volume
# time
# 1469974454  cheryl     intro.html                  6    NaN     NaN
# 1469974424  cheryl     intro.html                  5  False    10.0
# 1469974424     sue  advanced.html                 23  False    10.0

print('----------------------------------------')
df = df.reset_index()
df = df.set_index(['time', 'user'])
print(df.head(3))
#                            video  playback position paused  volume
# time       user
# 1469974424 cheryl     intro.html                  5  False    10.0
#            sue     advanced.html                 23  False    10.0
# 1469974454 cheryl     intro.html                  6    NaN     NaN

print('----------------------------------------')
# df.fillna?
# method : {'backfill', 'bfill', 'pad', 'ffill', None}, default None
#     Method to use for filling holes in reindexed Series
#     pad / ffill: propagate last valid observation forward to next valid
#     backfill / bfill: use NEXT valid observation to fill gap
df = df.fillna(method='ffill')
print(df.head(3))
#                            video  playback position paused  volume
# time       user
# 1469974424 cheryl     intro.html                  5  False    10.0
#            sue     advanced.html                 23  False    10.0
# 1469974454 cheryl     intro.html                  6  False    10.0
