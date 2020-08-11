# -*- coding: UTF-8 -*-
from __future__ import division
import pandas as pd

# The following code loads the olympics dataset (olympics.csv), which was derrived from the Wikipedia entry
# on All Time Olympic Games Medals, and does some basic data cleaning.
# The columns are organized as # of Summer games, Summer medals, # of Winter games, Winter medals,
# total # number of games, total # of medals. Use this dataset to answer the questions below.
df = pd.read_csv('../data/olympics.csv', index_col=0, skiprows=1)
for col in df.columns:
    if col[:2] == '01':
        df.rename(columns={col: 'Gold' + col[4:]}, inplace=True)
    if col[:2] == '02':
        df.rename(columns={col: 'Silver' + col[4:]}, inplace=True)
    if col[:2] == '03':
        df.rename(columns={col: 'Bronze' + col[4:]}, inplace=True)
    if col[:1] == '№':  # 虽然我在本地修改了数据文件, 但是Coursera服务器上仍是这个, 所以保留
        df.rename(columns={col: '#' + col[1:]}, inplace=True)

names_ids = df.index.str.split('(')  # split the index by '('

df.index = names_ids.str[0]  # the [0] element is the country name (new index)
df['ID'] = names_ids.str[1].str[:3]  # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')
print(df.head(1))
#               # Summer  Gold  Silver  Bronze  Total  # Winter  Gold.1  \
# Afghanistan         13     0       0       2      2         0       0
#               Silver.1  Bronze.1  Total.1  # Games  Gold.2  Silver.2  \
# Afghanistan          0         0        0       13       0         0
#               Bronze.2  Combined total   ID
# Afghanistan          2               2  AFG


# Question 0 (Example)
# ----------------------------------------
# Quiz Question: What is the first country in df?
# This function should return a Series.
def answer_zero():
    return df.iloc[0]


print('\nQuestion 0')
print(answer_zero())


# # Summer           13
# Gold                0
# Silver              0
# Bronze              2
# Total               2
# # Winter            0
# Gold.1              0
# Silver.1            0
# Bronze.1            0
# Total.1             0
# # Games            13
# Gold.2              0
# Silver.2            0
# Bronze.2            2
# Combined total      2
# ID                AFG
# Name: Afghanistan, dtype: object


# Question 1
# ----------------------------------------
# Quiz Question: Which country has won the most gold medals in summer games?
# This function should return a single string value.
def answer_one1():
    # Here the index has the country name
    # Only one returns
    return df[df['Gold'] == df['Gold'].max()].index.index[0]


def answer_one2():
    # Here the index has the country name
    return df.sort_index(axis=0, by='Gold', ascending=False).index[0]


def answer_one():
    # Directly return index name
    return df['Gold'].argmax()


print('\nQuestion 1')
print(answer_one())  # United States


# Question 2
# ----------------------------------------
# Quiz Question: Which country had the biggest difference between their summer and winter gold medal counts?
# This function should return a single string value.
def answer_two2():
    biggest_diff = abs(df['Gold'] - df['Gold.1']).max()
    # Here the index has the country name
    return df[abs(df['Gold'] - df['Gold.1']) == biggest_diff].index[0]


def answer_two():
    df['Gold_Diff'] = abs(df['Gold'] - df['Gold.1'])
    return df['Gold_Diff'].argmax()


print('\nQuestion 2')
print(answer_two())  # United States


# Question 3
# ----------------------------------------
# Quiz Question: Which country has the biggest difference between their summer gold medal
# counts and winter gold medal counts relative to their total gold medal count?
# Summer Gold−Winter GoldTotal Gold
# Only include countries that have won at least 1 gold in both summer and winter.
# This function should return a single string value.
def answer_three():
    df2 = pd.DataFrame()
    df2['Gold'] = df['Gold']
    df2['Gold.1'] = df['Gold.1']
    df2 = df2[(df2['Gold'] > 0) & (df2['Gold.1'] > 0)]
    df2['Gold_diff_r'] = (df['Gold'] - df['Gold.1']) / df['Gold.2']
    return df2['Gold_diff_r'].argmax()


print('\nQuestion 3')
print(answer_three())  # Bulgaria


# Question 4
# ----------------------------------------
# Quiz Question: Write a function to update the dataframe to include a new column called "Points"
# which is a weighted value where each gold medal counts for 3 points, silver medals for 2 points,
# and bronze mdeals for 1 point. The function should return only the column (a Series object) which you created.
# This function should return a Series named Points of length 146
def answer_four():
    point = df['Gold.2'] * 3 + df['Silver.2'] * 2 + df['Bronze.2']
    return point


print('\nQuestion 4')
print(len(answer_four()))  # 146
