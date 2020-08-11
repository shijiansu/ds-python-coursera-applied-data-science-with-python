# -*- coding: UTF-8 -*-
import pandas as pd

purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})
df = pd.DataFrame([purchase_1, purchase_2, purchase_3],
                  index=['Store 1', 'Store 1', 'Store 2'])
print(df)
#          Cost Item Purchased   Name
# Store 1  22.5       Dog Food  Chris
# Store 1   2.5   Kitty Litter  Kevyn
# Store 2   5.0      Bird Seed  Vinod

print('')
print(df.loc['Store 2'])
# Cost                      5
# Item Purchased    Bird Seed
# Name                  Vinod
# Name: Store 2, dtype: object

print('')
print(type(df.loc['Store 2']))
# <class 'pandas.core.series.Series'>

print('')
print(df.loc['Store 1'])
#          Cost Item Purchased   Name
# Store 1  22.5       Dog Food  Chris
# Store 1   2.5   Kitty Litter  Kevyn

print('')
print(df.loc['Store 1', 'Cost'])  # 这里第二个就成为列的第一个index, 应该是由左向右依次
# Store 1    22.5
# Store 1     2.5
# Name: Cost, dtype: float64

print('')
print(df.loc['Store 1']['Cost'])
# Store 1    22.5
# Store 1     2.5
# Name: Cost, dtype: float64

print('')
print(df.T)
#                  Store 1       Store 1    Store 2
# Cost                22.5           2.5          5
# Item Purchased  Dog Food  Kitty Litter  Bird Seed
# Name               Chris         Kevyn      Vinod

print('')
print(df.T.loc['Cost'])
# Store 1    22.5
# Store 1     2.5
# Store 2       5
# Name: Cost, dtype: object

print('')
print(df['Cost'])
# Store 1    22.5
# Store 1     2.5
# Store 2     5.0
# Name: Cost, dtype: float64

print('')
print(df.loc[:, ['Name', 'Cost']])  # 原来也可以做切片, 不过列名是多一个[]
#           Name  Cost
# Store 1  Chris  22.5
# Store 1  Kevyn   2.5
# Store 2  Vinod   5.0

print('')
print(df.drop('Store 1'))  # 删除某行
#          Cost Item Purchased   Name
# Store 2   5.0      Bird Seed  Vinod

print('----------------------------------------')
# copy
copy_df = df.copy()
copy_df = copy_df.drop('Store 1')  # 删除某行
print(copy_df)
#          Cost Item Purchased   Name
# Store 2   5.0      Bird Seed  Vinod

print('')
# copy_df.drop?
del copy_df['Name']  # 删除某列
print(copy_df)
#          Cost Item Purchased
# Store 2   5.0      Bird Seed

print('')
df['Location'] = None  # 新增列
print(df)
#          Cost Item Purchased   Name Location
# Store 1  22.5       Dog Food  Chris     None
# Store 1   2.5   Kitty Litter  Kevyn     None
# Store 2   5.0      Bird Seed  Vinod     None

print('')
costs = df['Cost']
print(costs)
# Store 1    22.5
# Store 1     2.5
# Store 2     5.0
# Name: Cost, dtype: float64

print('')
costs += 2
print(costs)
# Store 1    24.5
# Store 1     4.5
# Store 2     7.0
# Name: Cost, dtype: float64

print('')
print(df)
#          Cost Item Purchased   Name Location
# Store 1  24.5       Dog Food  Chris     None
# Store 1   4.5   Kitty Litter  Kevyn     None
# Store 2   7.0      Bird Seed  Vinod     None
