# -*- coding: UTF-8 -*-
import numpy as np
import pandas as pd

df = pd.read_csv('data/census.csv')
df = df[df['SUMLEV'] == 50]

print(df.groupby('STNAME').agg({'CENSUS2010POP': np.average}))
#                       CENSUS2010POP
# STNAME
# Alabama                71339.343284
# Alaska                 24490.724138
# Arizona               426134.466667
# Arkansas               38878.906667
# California            642309.586207
# Colorado               78581.187500

print('----------------------------------------')
print(type(df.groupby(level=0)['POPESTIMATE2010', 'POPESTIMATE2011']))
# <class 'pandas.core.groupby.DataFrameGroupBy'>

print('----------------------------------------')
print(type(df.groupby(level=0)['POPESTIMATE2010']))
# <class 'pandas.core.groupby.SeriesGroupBy'>

print('----------------------------------------')
df1 = (df.set_index('STNAME').groupby(level=0)['CENSUS2010POP']
       .agg({'avg': np.average, 'sum': np.sum}))
print(df1.head(10))
#                            sum            avg
# STNAME
# Alabama                4779736   71339.343284
# Alaska                  710231   24490.724138
# Arizona                6392017  426134.466667
# Arkansas               2915918   38878.906667
# California            37253956  642309.586207
# Colorado               5029196   78581.187500
# Connecticut            3574097  446762.125000
# Delaware                897934  299311.333333
# District of Columbia    601723  601723.000000
# Florida               18801310  280616.567164

print('----------------------------------------')
df2 = (df.set_index('STNAME').groupby(level=0)['POPESTIMATE2010', 'POPESTIMATE2011']
       .agg({'avg': np.average, 'sum': np.sum}))
print(df2.head(10))
#                                  sum                             avg  \
#                      POPESTIMATE2010 POPESTIMATE2011 POPESTIMATE2010
# STNAME
# Alabama                      4785161         4801108    71420.313433
# Alaska                        714021          722720    24621.413793
# Arizona                      6408208         6468732   427213.866667
# Arkansas                     2922394         2938538    38965.253333
# California                  37334079        37700034   643691.017241
# Colorado                     5048254         5119480    78878.968750
# Connecticut                  3579717         3589759   447464.625000
# Delaware                      899791          907916   299930.333333
# District of Columbia          605126          620472   605126.000000
# Florida                     18849890        19105533   281341.641791
#
#
#                      POPESTIMATE2011
# STNAME
# Alabama                 71658.328358
# Alaska                  24921.379310
# Arizona                431248.800000
# Arkansas                39180.506667
# California             650000.586207
# Colorado                79991.875000
# Connecticut            448719.875000
# Delaware               302638.666667
# District of Columbia   620472.000000
# Florida                285157.208955

print('----------------------------------------')
df3 = (df.set_index('STNAME').groupby(level=0)['POPESTIMATE2010', 'POPESTIMATE2011']
       .agg({'POPESTIMATE2010': np.average, 'POPESTIMATE2011': np.sum}))

print(df3.head(10))
#                       POPESTIMATE2011  POPESTIMATE2010
# STNAME
# Alabama                       4801108     71420.313433
# Alaska                         722720     24621.413793
# Arizona                       6468732    427213.866667
# Arkansas                      2938538     38965.253333
# California                   37700034    643691.017241
# Colorado                      5119480     78878.968750
# Connecticut                   3589759    447464.625000
# Delaware                       907916    299930.333333
# District of Columbia           620472    605126.000000
# Florida                      19105533    281341.641791
