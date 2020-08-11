# -*- coding: UTF-8 -*-
import pandas as pd

df = pd.read_csv('data/census.csv')
print(df.head(1))
print('')

df = (df.where(df['SUMLEV'] == 50)
      .dropna()
      .set_index(['STNAME', 'CTYNAME'])
      .rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'}))

# Same as:
# df = df[df['SUMLEV']==50]
# df = df.dropna()
# df.set_index(['STNAME','CTYNAME'], inplace=True)
# df.rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'})
print(df.head(1))
