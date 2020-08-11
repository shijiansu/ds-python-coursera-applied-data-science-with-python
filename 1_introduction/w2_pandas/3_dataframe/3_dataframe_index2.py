# -*- coding: UTF-8 -*-
import pandas as pd

print('\nIndexing...')
print('----------------------------------------')
df = pd.read_csv('../data/census.csv')
print(len(df))  # 3193

print(df['SUMLEV'].unique())  # [40 50]

df = df[df['SUMLEV'] == 50]
print(len(df))  # 3142

print('----------------------------------------')
columns_to_keep = ['STNAME',
                   'CTYNAME',
                   'BIRTHS2010',
                   'BIRTHS2011',
                   'BIRTHS2012',
                   'BIRTHS2013',
                   'BIRTHS2014',
                   'BIRTHS2015',
                   'POPESTIMATE2010',
                   'POPESTIMATE2011',
                   'POPESTIMATE2012',
                   'POPESTIMATE2013',
                   'POPESTIMATE2014',
                   'POPESTIMATE2015']
df = df[columns_to_keep]  # 只留下上述列
print(df.head(1))
#     STNAME         CTYNAME  BIRTHS2010  BIRTHS2011  BIRTHS2012  BIRTHS2013  \
# 1  Alabama  Autauga County         151         636         615         574
#    BIRTHS2014  BIRTHS2015  POPESTIMATE2010  POPESTIMATE2011  POPESTIMATE2012  \
# 1         623         600            54660            55253            55175
#    POPESTIMATE2013  POPESTIMATE2014  POPESTIMATE2015
# 1            55038            55290            55347

print('----------------------------------------')
# 这里是将下列两个列的值作为行索引
df = df.set_index(['STNAME', 'CTYNAME'])
print(df.head(1))
#                         BIRTHS2010  BIRTHS2011  BIRTHS2012  BIRTHS2013  \
# STNAME  CTYNAME
# Alabama Autauga County         151         636         615         574
#                         BIRTHS2014  BIRTHS2015  POPESTIMATE2010  \
# STNAME  CTYNAME
# Alabama Autauga County         623         600            54660
#                         POPESTIMATE2011  POPESTIMATE2012  POPESTIMATE2013  \
# STNAME  CTYNAME
# Alabama Autauga County            55253            55175            55038
#                         POPESTIMATE2014  POPESTIMATE2015
# STNAME  CTYNAME
# Alabama Autauga County            55290            55347

print('----------------------------------------')
# 将行索引, STNAME = 'Michigan', CTYNAME = 'Washtenaw County'对应的行输出
print(df.loc['Michigan', 'Washtenaw County'])
# BIRTHS2010            977
# BIRTHS2011           3826
# BIRTHS2012           3780
# BIRTHS2013           3662
# BIRTHS2014           3683
# BIRTHS2015           3709
# POPESTIMATE2010    345563
# POPESTIMATE2011    349048
# POPESTIMATE2012    351213
# POPESTIMATE2013    354289
# POPESTIMATE2014    357029
# POPESTIMATE2015    358880
# Name: (Michigan, Washtenaw County), dtype: int64

print('----------------------------------------')
# 对应行索引的行输出
print(df.loc[[('Michigan', 'Washtenaw County'), ('Michigan', 'Wayne County')]])
#                           BIRTHS2010  BIRTHS2011  BIRTHS2012  BIRTHS2013  \
# STNAME   CTYNAME
# Michigan Washtenaw County         977        3826        3780        3662
#          Wayne County            5918       23819       23270       23377
#                            BIRTHS2014  BIRTHS2015  POPESTIMATE2010  \
# STNAME   CTYNAME
# Michigan Washtenaw County        3683        3709           345563
#          Wayne County           23607       23586          1815199
#                            POPESTIMATE2011  POPESTIMATE2012  POPESTIMATE2013  \
# STNAME   CTYNAME
# Michigan Washtenaw County           349048           351213           354289
#          Wayne County              1801273          1792514          1775713
#                            POPESTIMATE2014  POPESTIMATE2015
# STNAME   CTYNAME
# Michigan Washtenaw County           357029           358880
#          Wayne County              1766008          1759335
