#!/usr/bin/python
# -*- coding:utf-8 -*-

# Assignment 2
# Before working on this assignment please read these instructions fully. In the submission area,
# you will notice that you can click the link to Preview the Grading for each step of the assignment.
# This is the criteria that will be used for peer grading. Please familiarize yourself with
# the criteria before beginning the assignment.
#
# An NOAA dataset has been stored in the file
# 数据源
# "data/C2A2_data/BinnedCsvs_d100/4e86d2106d0566c6ad9843d882e72791333b08be3d647dcae4f4b110.csv".
# The data for this assignment comes from a subset of
# The National Centers for Environmental Information (NCEI) Daily Global Historical Climatology Network (GHCN-Daily).
# The GHCN-Daily is comprised of daily climate records from thousands of land surface stations across the globe.
#
# Each row in the assignment datafile corresponds to a single observation.
# The following variables are provided to you:
#
# 数据格式
# "id" : station identification code
# "date" : date in YYYY-MM-DD format (e.g. 2012-01-24 = January 24, 2012)
# "element" : indicator of element type
# "TMAX" : Maximum temperature (tenths of degrees C)
# "TMIN" : Minimum temperature (tenths of degrees C)
# "value" : data value for element (tenths of degrees C)
#
# 作业要求
# For this assignment, you must:
# 1) Read the documentation and familiarize yourself with the dataset,
# then write some python code which returns a line graph of the record high and record low temperatures
# by day of the year over the period 2005-2014.
# 读取2005-2014数据
# 2) The area between the record high and record low temperatures for each day should be shaded.
# 最高和最低之间高亮
# 3) Overlay a scatter of the 2015 data for any points (highs and lows) for which
# the ten year record (2005-2014) record high or record low was broken in 2015.
# 叠加2015数据, 比较2005-2014数据, 如果最高和最低有新记录, 就显示
# 4) Watch out for leap days (i.e. February 29th),
# it is reasonable to remove these points from the dataset for the purpose of this visualization.
# 移除闰日
# 5) Make the visual nice!
# Leverage principles from the first module in this course when developing your solution.
# Consider issues such as legends, labels, and chart junk.
# 添加legends, labels, and chart junk
#
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime as datetime

# 读取数据
df = pd.read_csv('data/C2A2_data/BinnedCsvs_d100/4e86d2106d0566c6ad9843d882e72791333b08be3d647dcae4f4b110.csv')

# 清洗数据
df = df.sort_values(['Date', 'ID'])

# # 获得分拆的年和月日
df['Year'] = df['Date'].apply(lambda x: x[:4])
df['Month_Day'] = df['Date'].apply(lambda x: x[5:])
print(len(df))  # 23754

# # 移除闰日
df = df[df['Month_Day'] != '02-29']
print(len(df))  # 23741

# # 获得2005-2014数据
df_2005_2014 = df[df['Year'] != '2015']
# # 获得2015数据
df_2015 = df[df['Year'] == '2015']

# 探索数据
print('\nAll Data:')
print(df.head())
print(len(df))

print('\nYear 2005-2014:')
print(df_2005_2014.head())
print(len(df_2005_2014))

print('\nYear 2015:')
print(df_2015.head())
print(len(df_2015))

# 最大最小数据
df_2005_2014_min = df_2005_2014[df_2005_2014['Element'] == 'TMIN']
df_2005_2014_max = df_2005_2014[df_2005_2014['Element'] == 'TMAX']
df_2015_min = df_2015[df_2015['Element'] == 'TMIN']
df_2015_max = df_2015[df_2015['Element'] == 'TMAX']


# 处理数据
def get_min_max(df, type):
    return df.groupby(['Month_Day']).agg({'Data_Value': type})


# # 获得2005-2014每日的最高和最低记录
df_2005_2014_lowest = get_min_max(df_2005_2014_min, np.min)
df_2005_2014_highest = get_min_max(df_2005_2014_max, np.max)
df_2015_lowest = get_min_max(df_2015_min, np.min)
df_2015_highest = get_min_max(df_2015_max, np.max)

# 获得2015的记录 - 这里是返回数组下标的索引值
df_2015_beark_lowest = np.where(df_2015_lowest['Data_Value'] < df_2005_2014_lowest['Data_Value'])[0]
df_2015_beark_highest = np.where(df_2015_highest['Data_Value'] > df_2005_2014_highest['Data_Value'])[0]

# 显示数据
fig = plt.figure(figsize=(15, 10), frameon=False)
fig.patch.set_alpha(0)

# # 制图辅助数据 - X轴的长度
df_len = len(df_2005_2014_lowest)
# # 制图辅助数据 - Y轴的最低最高值
max_temperature = df[df['Element'] == 'TMAX']['Data_Value'].max()
min_temperature = df[df['Element'] == 'TMIN']['Data_Value'].min()

# # 2005-2014的最高和最低
plt.plot(df_2005_2014_highest.values, 'y',
         label='Record High (2005-2014)')
plt.plot(df_2005_2014_lowest.values, 'g',
         label='Record Low (2005-2014)')

# # 填充颜色
plt.gca().fill_between(range(df_len),
                       df_2005_2014_highest['Data_Value'],
                       df_2005_2014_lowest['Data_Value'],
                       facecolor='grey',
                       alpha=0.2)

# # 2015, zorder=10让点显示在层次的最上面
plt.scatter(df_2015_beark_highest, df_2015_highest.iloc[df_2015_beark_highest],
            s=10, c='r',
            zorder=10,
            label='Broken High (2015)')
plt.scatter(df_2015_beark_lowest, df_2015_lowest.iloc[df_2015_beark_lowest],
            s=10, c='b',
            zorder=10,
            label='Broken Low (2015)')

# # 图示
plt.title('Daily Climate Records Near Singapore (2005-2015)')
plt.xlabel('Month-Day of the Year')
plt.ylabel('Temperature (Tenths of Degrees C)')
plt.legend(loc=4, frameon=False, fontsize='medium')
plt.xticks(range(0, df_len, 15),
           [datetime.datetime.strptime(i, '%m-%d').strftime('%b-%d')
            for i in df_2005_2014_lowest.index[range(0, df_len, 15)]],
           rotation='60')

# # 美化 - 控制X轴和Y轴显示的范围
plt.gca().axis([0, df_len, min_temperature - 10, max_temperature + 10])
# # 美化 - 边框
plt.gca().spines['top'].set_visible(False)  # 移除图表上方的边框
plt.gca().spines['right'].set_visible(False)  # 移除图表右方的边框
plt.show()

# 保存
fig.canvas.print_png('2_assignment.png', dpi=300)
