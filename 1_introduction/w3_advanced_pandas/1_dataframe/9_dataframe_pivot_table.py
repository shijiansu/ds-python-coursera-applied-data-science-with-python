# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np

# http://open.canada.ca/data/en/dataset/98f1a129-f628-4ce4-b24d-6f16bf24dd64
df = pd.read_csv('data/cars.csv')

print(df.head(1))

print('----------------------------------------')
print(df.pivot_table(values='(kW)', index='YEAR', columns='Make', aggfunc=np.mean))
# Make    BMW  CHEVROLET   FORD   KIA  MITSUBISHI  NISSAN  SMART       TESLA
# YEAR
# 2012    NaN        NaN    NaN   NaN        49.0    80.0    NaN         NaN
# 2013    NaN        NaN  107.0   NaN        49.0    80.0   35.0  280.000000
# 2014    NaN      104.0  107.0   NaN        49.0    80.0   35.0  268.333333
# 2015  125.0      104.0  107.0  81.0        49.0    80.0   35.0  320.666667
# 2016  125.0      104.0  107.0  81.0        49.0    80.0   35.0  409.700000

print('----------------------------------------')
print(df.pivot_table(values='(kW)', index='YEAR', columns='Make', aggfunc=[np.mean, np.min], margins=True))
