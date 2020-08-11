# -*- coding: UTF-8 -*-
import pandas as pd

df = pd.DataFrame([{'Name': 'Chris', 'Item Purchased': 'Sponge', 'Cost': 22.50},
                   {'Name': 'Kevyn', 'Item Purchased': 'Kitty Litter', 'Cost': 2.50},
                   {'Name': 'Filip', 'Item Purchased': 'Spoon', 'Cost': 5.00}],
                  index=['Store 1', 'Store 1', 'Store 2'])
print(df)
#          Cost Item Purchased   Name
# Store 1  22.5         Sponge  Chris
# Store 1   2.5   Kitty Litter  Kevyn
# Store 2   5.0          Spoon  Filip

print('----------------------------------------')
df['Date'] = ['December 1', 'January 1', 'mid-May']
print(df)
#          Cost Item Purchased   Name        Date
# Store 1  22.5         Sponge  Chris  December 1
# Store 1   2.5   Kitty Litter  Kevyn   January 1
# Store 2   5.0          Spoon  Filip     mid-May

print('----------------------------------------')
df['Delivered'] = True
print(df)
#          Cost Item Purchased   Name        Date Delivered
# Store 1  22.5         Sponge  Chris  December 1      True
# Store 1   2.5   Kitty Litter  Kevyn   January 1      True
# Store 2   5.0          Spoon  Filip     mid-May      True

print('----------------------------------------')
df['Feedback'] = ['Positive', None, 'Negative']
print(df)
#          Cost Item Purchased   Name        Date Delivered  Feedback
# Store 1  22.5         Sponge  Chris  December 1      True  Positive
# Store 1   2.5   Kitty Litter  Kevyn   January 1      True      None
# Store 2   5.0          Spoon  Filip     mid-May      True  Negative

print('----------------------------------------')
adf = df.reset_index()
adf['Date'] = pd.Series({0: 'December 1', 2: 'mid-May'})
print(adf)
#      index  Cost Item Purchased   Name        Date Delivered  Feedback
# 0  Store 1  22.5         Sponge  Chris  December 1      True  Positive
# 1  Store 1   2.5   Kitty Litter  Kevyn         NaN      True      None
# 2  Store 2   5.0          Spoon  Filip     mid-May      True  Negative

print('----------------------------------------')
staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR'},
                         {'Name': 'Sally', 'Role': 'Course liasion'},
                         {'Name': 'James', 'Role': 'Grader'}])
staff_df = staff_df.set_index('Name')
student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business'},
                           {'Name': 'Mike', 'School': 'Law'},
                           {'Name': 'Sally', 'School': 'Engineering'}])
student_df = student_df.set_index('Name')
print(staff_df.head())
#                  Role
# Name
# Kelly  Director of HR
# Sally  Course liasion
# James          Grader
print('')
print(student_df.head())
#             School
# Name
# James     Business
# Mike           Law
# Sally  Engineering

print('----------------------------------------')
df = pd.merge(staff_df, student_df, how='outer', left_index=True, right_index=True)
print(df)
#                  Role       School
# Name
# James          Grader     Business
# Kelly  Director of HR          NaN
# Mike              NaN          Law
# Sally  Course liasion  Engineering

print('----------------------------------------')
df = pd.merge(staff_df, student_df, how='inner', left_index=True, right_index=True)
print(df)
#                  Role       School
# Name
# James          Grader     Business
# Sally  Course liasion  Engineering

print('----------------------------------------')
df = pd.merge(staff_df, student_df, how='left', left_index=True, right_index=True)
print(df)
#                  Role       School
# Name
# Kelly  Director of HR          NaN
# Sally  Course liasion  Engineering
# James          Grader     Business

print('----------------------------------------')
df = pd.merge(staff_df, student_df, how='right', left_index=True, right_index=True)
print(df)
#                  Role       School
# Name
# James          Grader     Business
# Mike              NaN          Law
# Sally  Course liasion  Engineering

print('----------------------------------------')
staff_df = staff_df.reset_index()
student_df = student_df.reset_index()
df = pd.merge(staff_df, student_df, how='left', left_on='Name', right_on='Name')
print(df)
#     Name            Role       School
# 0  Kelly  Director of HR          NaN
# 1  Sally  Course liasion  Engineering
# 2  James          Grader     Business

print('----------------------------------------')
staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR', 'Location': 'State Street'},
                         {'Name': 'Sally', 'Role': 'Course liasion', 'Location': 'Washington Avenue'},
                         {'Name': 'James', 'Role': 'Grader', 'Location': 'Washington Avenue'}])
student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business', 'Location': '1024 Billiard Avenue'},
                           {'Name': 'Mike', 'School': 'Law', 'Location': 'Fraternity House #22'},
                           {'Name': 'Sally', 'School': 'Engineering', 'Location': '512 Wilson Crescent'}])
df = pd.merge(staff_df, student_df, how='left', left_on='Name', right_on='Name')
print(df)
#           Location_x   Name            Role            Location_y       School
# 0       State Street  Kelly  Director of HR                   NaN          NaN
# 1  Washington Avenue  Sally  Course liasion   512 Wilson Crescent  Engineering
# 2  Washington Avenue  James          Grader  1024 Billiard Avenue     Business

print('----------------------------------------')
staff_df = pd.DataFrame([{'First Name': 'Kelly', 'Last Name': 'Desjardins', 'Role': 'Director of HR'},
                         {'First Name': 'Sally', 'Last Name': 'Brooks', 'Role': 'Course liasion'},
                         {'First Name': 'James', 'Last Name': 'Wilde', 'Role': 'Grader'}])
student_df = pd.DataFrame([{'First Name': 'James', 'Last Name': 'Hammond', 'School': 'Business'},
                           {'First Name': 'Mike', 'Last Name': 'Smith', 'School': 'Law'},
                           {'First Name': 'Sally', 'Last Name': 'Brooks', 'School': 'Engineering'}])
print(staff_df)
#   First Name   Last Name            Role
# 0      Kelly  Desjardins  Director of HR
# 1      Sally      Brooks  Course liasion
# 2      James       Wilde          Grader
print('')
print(student_df)
#   First Name Last Name       School
# 0      James   Hammond     Business
# 1       Mike     Smith          Law
# 2      Sally    Brooks  Engineering

print('----------------------------------------')
df = pd.merge(staff_df, student_df, how='inner', left_on=['First Name', 'Last Name'],
              right_on=['First Name', 'Last Name'])
print(df)
#   First Name Last Name            Role       School
# 0      Sally    Brooks  Course liasion  Engineering
