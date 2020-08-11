# -*- coding: UTF-8 -*-
from __future__ import division

import re

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# 思路分析:
# # 问题: 这里是要求各个国家的GDP和Energy Supply之类的情况.
# # 数据源:
# ## Energy Indicators.xls: 国家及地区名: Energy Supply和Energy Supply每人;
# ## world_bank.csv: 国家及地区名: 历年GDP;
# ## scimagojr-3.xlsx: 国家及地区名: Citations相关数据;
# # 关键点:
# # 由于3个数据源之间的主键(Country Name)不一样, 所以需要对其做基本的数据清洗.
# # 数据清洗只是需要按题目要求, 实际上, 下列Top 15 Rank的国家最为重要, 因为Question 3~13都是基本围绕Top 15.
# # 清洗后, 相join得出最终需要处理的数据源.

# Question 1
# ----------------------------------------
# Quiz Question: Load the energy data from the file Energy Indicators.xls, which is a list of indicators
# of energy supply and renewable electricity production from the United Nations for the year 2013,
# and should be put into a DataFrame with the variable name of energy.
#
# Keep in mind that this is an Excel file, and not a comma separated values file. Also,
# make sure to exclude the footer and header information from the datafile. The first two columns are unneccessary,
# so you should get rid of them, and you should change the column labels so that the columns are:
# ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable]
#
# Convert Energy Supply to gigajoules (there are 1,000,000 gigajoules in a petajoule).
# For all countries which have missing data (e.g. data with "...") make sure this is reflected as np.NaN values.
# Rename the following list of countries (for use in later questions):
# "Republic of Korea": "South Korea",
# "United States of America": "United States",
# "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
# "China, Hong Kong Special Administrative Region": "Hong Kong"
# There are also several countries with parenthesis in their name. Be sure to remove these,
# e.g. 'Bolivia (Plurinational State of)' should be 'Bolivia'.
#
# Next, load the GDP data from the file world_bank.csv, which is a csv containing countries' GDP from 1960 to 2015
# from World Bank. Call this DataFrame GDP.
#
# Make sure to skip the header, and rename the following list of countries:
# "Korea, Rep.": "South Korea",
# "Iran, Islamic Rep.": "Iran",
# "Hong Kong SAR, China": "Hong Kong"
#
# Finally, load the Sciamgo Journal and Country Rank data for Energy Engineering and Power Technology from the file
# scimagojr-3.xlsx, which ranks countries based on their journal contributions in the aforementioned area.
# Call this DataFrame ScimEn.
# Join the three datasets: GDP, Energy, and ScimEn into a new dataset (using the intersection of country names).
# Use only the last 10 years (2006-2015) of GDP data and only the top 15 countries
# by Scimagojr 'Rank' (Rank 1 through 15).
#
# The index of this DataFrame should be the name of the country, and the columns should be
# ['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index',
# 'Energy Supply', 'Energy Supply per Capita', '% Renewable',
#  '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015'].
# This function should return a DataFrame with 20 columns and 15 entries.
def get_energy(_debug=False):
    if _debug: print('\nget_energy()')

    # Load data
    # 1. skip header and footer; 2. NaN data is '...'
    df1 = pd.read_excel("data/Energy Indicators.xls", skiprows=17, skipfooter=38, na_values="...")
    if _debug: print('Type: {}'.format(type(df1)))  # dataframe

    # Correct column names
    df1 = df1.drop(df1.columns[[0, 1]], axis=1)  # remove useless columns
    df1.rename(columns={df1.columns[0]: 'Country'}, inplace=True)
    df1.rename(columns={df1.columns[1]: 'Energy Supply'}, inplace=True)
    df1.rename(columns={df1.columns[2]: 'Energy Supply per Capita'}, inplace=True)
    df1.rename(columns={df1.columns[3]: '% Renewable'}, inplace=True)

    if _debug: print('df1 Columns: {}'.format(df1.columns))

    # Clean data
    rename_country1 = {
        "Republic of Korea": "South Korea",
        "United States of America": "United States",
        "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
        "China, Hong Kong Special Administrative Region": "Hong Kong"}

    df1['Energy Supply'] *= 1000000

    # 理论上DataFrame不应该做循环处理 -> 用apply, 参考assignment 4, question 1
    country = pd.Series(len(df1))  # to set value
    for i in range(len(df1)):
        row = df1.loc[i, :]

        # Rename country name:
        # Step 1: remove number. e.g. Greenland7 -> Greenland
        country[i] = re.sub("\d", "", row['Country'])  # 正则表达式替换

        # Step 2: remove (), break the row and only keep index=0
        country[i] = country[i].split(' (')[0]

        # Step 3: replace name by rename_country
        if country[i] in rename_country1.keys():
            country[i] = rename_country1.get(country[i])
            if _debug: print('{} -> {}'.format(row['Country'], country[i]))
    df1['Country'] = country

    df1.set_index('Country', inplace=True)
    if _debug:
        print('df1 Columns: {}'.format(df1.columns))
        print('\nHong Kong:\n{}'.format(df1.loc['Hong Kong']))
        # print(list(df1.index))
    return df1


def get_gdp(_debug=False):
    if _debug: print('\nget_gdp()')
    # Load data
    df2 = pd.read_csv('data/world_bank.csv', skiprows=4, encoding="utf8")
    if _debug: print('df2 Columns: {}'.format(df2.columns))

    # Only needs country name and last 10 years data
    df2 = df2[['Country Name', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014',
               '2015']]  # Here is [[]]
    df2.rename(columns={'Country Name': 'Country'}, inplace=True)
    if _debug: print('df2 Columns: {}'.format(df2.columns))

    # Clean data
    rename_country2 = {"Korea, Rep.": "South Korea",
                       "Iran, Islamic Rep.": "Iran",
                       "Hong Kong SAR, China": "Hong Kong"}

    country = pd.Series(len(df2))  # to set value
    for i in range(len(df2)):
        row = df2.iloc[i, :]
        # replace name by rename_country
        country[i] = row['Country']
        if country[i] in rename_country2.keys():
            country[i] = rename_country2.get(country[i])
            if _debug: print('{} -> {}'.format(row['Country'], country[i]))
    df2['Country'] = country

    df2.set_index('Country', inplace=True)
    if _debug:
        print('df2 Columns: {}'.format(df2.columns))
        print('South Korea:\n{}'.format(df2.loc['South Korea']))
        # print(list(df2.index))
    return df2


def get_rank(_debug=False):
    if _debug: print('\nget_rank()')

    # Load data
    df3 = pd.read_excel("data/scimagojr-3.xlsx")

    if _debug: print('df3 Columns: {}'.format(df3.columns))

    df3.set_index('Country', inplace=True)
    if _debug:
        print('df3 Columns: {}'.format(df3.columns))
        # print(list(df3.index))
    return df3


def answer_one(_debug=False):
    energy = get_energy(_debug)
    GDP = get_gdp(_debug)
    ScimEn = get_rank(_debug)
    ScimEn = ScimEn[ScimEn['Rank'] < 16]  # top 15

    # left join by the index
    df = pd.merge(ScimEn, energy, how='inner', left_index=True, right_index=True)
    df = pd.merge(df, GDP, how='inner', left_index=True, right_index=True)

    if _debug:
        print('\nanswer_one()')
        print('df Length: {}'.format(len(df)))
        print('df Columns: {}'.format(df.columns))
        print('Compare: {}'.format(df.columns == ['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations',
                                         'Citations per document', 'H index', 'Energy Supply',
                                         'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008',
                                         '2009', '2010', '2011', '2012', '2013', '2014', '2015']))
        # print(df)
    return df


print('\nQuestion 1')
df = answer_one(True)
print('\ncountry:\n{}'.format(df))
print('\ndtypes:\n{}'.format(df.dtypes))
print('\nshape: {}'.format(df.shape))
# shape: (15, 20)

# Question 2
# ----------------------------------------
# Quiz Question: The previous question joined three datasets then reduced this to just the top 15 entries.
# When you joined the datasets, but before you reduced this to the top 15 items, how many entries did you lose?
# This function should return a single number.
# 其实这一题和Top 15无关, 直接求全集和子集之间的差便可.
def answer_two():
    energy = get_energy()
    GDP = get_gdp()
    ScimEn = get_rank()
    print('Length: energy={}, GDP={}, ScimEn={}'.format(len(energy), len(GDP), len(ScimEn)))
    # Length: energy = 227, GDP = 264, ScimEn = 191

    # outer join by index
    df_inner = pd.merge(energy, GDP, how='inner', left_index=True, right_index=True)
    df_inner = pd.merge(df_inner, ScimEn, how='inner', left_index=True, right_index=True)

    df_outer = pd.merge(energy, GDP, how='outer', left_index=True, right_index=True)
    df_outer = pd.merge(df_outer, ScimEn, how='outer', left_index=True, right_index=True)

    # print(list(df_outer.index))
    return df_outer.shape[0] - df_inner.shape[0]


print('\nQuestion 2')
print(answer_two())  # 156


# Question 3
# ----------------------------------------
# Quiz Question: What are the top 15 countries for average GDP over the last 10 years?
# This function should return a Series named avgGDP with 15 countries and their average GDP sorted in descending order.
def answer_three():
    Top15 = answer_one()
    years = ['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
    # axis = 1针对每行分组, 求上述列的mean, 即求各个国家各自的2006-2015的平均值
    return Top15[years].mean(axis=1).sort_values(ascending=False)


print('\nQuestion 3')
print(answer_three())


# Country
# United States         1.536434e+13
# China                 6.348609e+12
# Japan                 5.542208e+12
# Germany               3.493025e+12
# France                2.681725e+12
# United Kingdom        2.487907e+12
# Brazil                2.189794e+12
# Italy                 2.120175e+12
# India                 1.769297e+12
# Canada                1.660647e+12
# Russian Federation    1.565459e+12
# Spain                 1.418078e+12
# Australia             1.164043e+12
# South Korea           1.106715e+12
# Iran                  4.441558e+11

# Question 4
# ----------------------------------------
# Quiz Question: By how much had the GDP changed over the 10 year span for the country with the 6th largest average GDP?
# This function should return a single number.
def answer_four():
    Top15_avg = answer_three()
    Top6_country = Top15_avg.index[5]  # index start at 0
    print(Top6_country)  # United Kingdom

    Top15 = answer_one()
    Top6 = Top15.loc[Top6_country]
    diff = Top6['2015'] - Top6['2006']
    print(type(diff))  # <type 'numpy.float64'>
    return diff


print('\nQuestion 4')
print(answer_four())  # 246702696075.0


# Question 5
# ----------------------------------------
# Quiz Question: What is the mean energy supply per capita?
# This function should return a single number.
def answer_five():
    Top15 = answer_one()
    return Top15['Energy Supply per Capita'].mean(axis=0)


print('\nQuestion 5')
print(answer_five())  # 157.6


# Question 6
# ----------------------------------------
# Quiz Question: What country has the maximum % Renewable and what is the percentage?
# This function should return a tuple with the name of the country and the percentage.
def answer_six():
    Top15 = answer_one()
    max_country = Top15['% Renewable'].argmax()
    country = Top15.loc[max_country]
    return max_country, country['% Renewable']


print('\nQuestion 6')
print(answer_six())  # (u'Brazil', 69.648030000000006)


# Question 7
# ----------------------------------------
# Quiz Question: Create a new column that is the ratio of Self-Citations to Total Citations. What is the maximum
# value for this new column, and what country has the highest ratio?
# This function should return a tuple with the name of the country and the ratio.
def answer_seven():
    Top15 = answer_one()
    Top15['Ratio'] = Top15['Self-citations'] / Top15['Citations']
    max_country = Top15['Ratio'].argmax()
    country = Top15.loc[max_country]
    return max_country, country['Ratio']


print('\nQuestion 7')
print(answer_seven())  # (u'China', 0.39377339829858382)


# Question 8
# ----------------------------------------
# Quiz Question: Create a column that estimates the population using Energy Supply and Energy Supply per capita.
# What is the third most populous country according to this estimate?
# This function should return a single string value.
def answer_eight():
    Top15 = answer_one()
    Top15['Population'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    return Top15['Population'].sort_values(ascending=False).index[2]


print('\nQuestion 8')
print(answer_eight())  # United States


# Question 9
# ----------------------------------------
# Quiz Question: Create a column that estimates the number of citable documents per person.
# What is the correlation between the number of citable documents per capita and the energy supply per capita?
# Use the .corr() method, (Pearson's correlation).
# This function should return a single number.
def answer_nine():
    Top15 = answer_one()
    Top15['Population'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citable documents per Capita'] = Top15['Citable documents'] / Top15['Population']
    return Top15['Citable documents per Capita'].corr(Top15['Energy Supply per Capita'])


print('\nQuestion 9')
print(answer_nine())  # 0.794001043544


def answer_nine_plot():
    Top15 = answer_one()
    Top15['Population'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citable documents per Capita'] = Top15['Citable documents'] / Top15['Population']
    Top15.plot(x='Citable documents per Capita', y='Energy Supply per Capita', kind='scatter', xlim=[0, 0.0006])
    plt.show()


answer_nine_plot()


# Question 10
# ----------------------------------------
# Quiz Question: Create a new column with a 1 if the country's % Renewable value is at or above the median for all
# countries in the top 15, and a 0 if the country's % Renewable value is below the median.
# This function should return a series named HighRenew whose index is the country name sorted in ascending order of rank.
def answer_ten():
    Top15 = answer_one()
    median = Top15['% Renewable'].median()  # 17.02028
    Top15['HighRenew'] = [1 if x >= median else 0 for x in Top15['% Renewable']]
    return Top15['HighRenew']


print('\nQuestion 10')
print(answer_ten())


# Country
# Australia             0
# Brazil                1
# Canada                1
# China                 1
# Germany               1
# Spain                 1
# France                1
# United Kingdom        0
# India                 0
# Iran                  0
# Italy                 1
# Japan                 0
# South Korea           0
# Russian Federation    1
# United States         0
# Name: HighRenew, dtype: int64
print(answer_ten().shape)
# (15L,)

# Question 11
# ----------------------------------------
# Quiz Question: Use the following dictionary to group the Countries by Continent, then create a dateframe that
# displays the sample size (the number of countries in each continent bin), and the sum, mean,
# and std deviation for the estimated population of each country.
# ContinentDict  = {'China':'Asia',
#                   'United States':'North America',
#                   'Japan':'Asia',
#                   'United Kingdom':'Europe',
#                   'Russian Federation':'Europe',
#                   'Canada':'North America',
#                   'Germany':'Europe',
#                   'India':'Asia',
#                   'France':'Europe',
#                   'South Korea':'Asia',
#                   'Italy':'Europe',
#                   'Spain':'Europe',
#                   'Iran':'Asia',
#                   'Australia':'Australia',
#                   'Brazil':'South America'}
# This function should return a DataFrame with index named Continent ['Asia', 'Australia', 'Europe', 'North America',
# 'South America'] and columns ['size', 'sum', 'mean', 'std']
def answer_eleven():
    Top15 = answer_one()
    ContinentDict = {'China': 'Asia',
                     'United States': 'North America',
                     'Japan': 'Asia',
                     'United Kingdom': 'Europe',
                     'Russian Federation': 'Europe',
                     'Canada': 'North America',
                     'Germany': 'Europe',
                     'India': 'Asia',
                     'France': 'Europe',
                     'South Korea': 'Asia',
                     'Italy': 'Europe',
                     'Spain': 'Europe',
                     'Iran': 'Asia',
                     'Australia': 'Australia',
                     'Brazil': 'South America'}
    Top15['Continent'] = [ContinentDict[x] for x in Top15.index]

    # init
    continents = sorted(set(ContinentDict.values()))
    columns = ['size', 'sum', 'mean', 'std']
    df = pd.DataFrame([pd.Series() * len(continents)], index=continents, columns=columns)

    # population
    Top15['Population'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']

    print(Top15['Population'])

    # 按每一个洲处理
    for c in continents:
        population_of_country_in_continent = Top15[Top15['Continent'] == c]['Population']
        df.set_value(c, ['size'], population_of_country_in_continent.count())
        df.set_value(c, ['sum'], population_of_country_in_continent.sum())
        df.set_value(c, ['mean'], population_of_country_in_continent.mean())
        df.set_value(c, ['std'], population_of_country_in_continent.std())
    return df


print('\nQuestion 11')
print(answer_eleven())


#                size           sum          mean           std
# Asia            5.0  2.898666e+09  5.797333e+08  6.790979e+08
# Australia       1.0  2.331602e+07  2.331602e+07           NaN
# Europe          6.0  4.579297e+08  7.632161e+07  3.464767e+07
# North America   2.0  3.528552e+08  1.764276e+08  1.996696e+08
# South America   1.0  2.059153e+08  2.059153e+08           NaN

# Question 12
# ----------------------------------------
# Quiz Question: Cut % Renewable into 5 bins. Group Top15 by the Continent, as well as these new % Renewable bins.
# How many countries are in each of these groups?
# This function should return a Series with a MultiIndex of Continent, then the bins for % Renewable.
# Do not include groups with no countries.
def answer_twelve():
    Top15 = answer_one()

    # % Renewable bin
    Top15['bins for % Renewable'] = pd.cut(Top15['% Renewable'], 5)

    # continent
    ContinentDict = {'China': 'Asia',
                     'United States': 'North America',
                     'Japan': 'Asia',
                     'United Kingdom': 'Europe',
                     'Russian Federation': 'Europe',
                     'Canada': 'North America',
                     'Germany': 'Europe',
                     'India': 'Asia',
                     'France': 'Europe',
                     'South Korea': 'Asia',
                     'Italy': 'Europe',
                     'Spain': 'Europe',
                     'Iran': 'Asia',
                     'Australia': 'Australia',
                     'Brazil': 'South America'}
    Top15['Continent'] = [ContinentDict[x] for x in Top15.index]

    Top15 = Top15.reset_index()
    df = Top15.groupby(['Continent', 'bins for % Renewable']).agg({'Country': np.count_nonzero})
    # print(df)
    #                                     Country
    # Continent     bins for % Renewable
    # Asia          (2.212, 15.753]             4
    #               (15.753, 29.227]            1
    # Australia     (2.212, 15.753]             1
    # Europe        (2.212, 15.753]             1
    #               (15.753, 29.227]            3
    #               (29.227, 42.701]            2
    # North America (2.212, 15.753]             1
    #               (56.174, 69.648]            1
    # South America (56.174, 69.648]            1
    return df.T.iloc[0]  # convert dataframe vector to series


print('\nQuestion 12')
print(answer_twelve())


# Continent      bins for % Renewable
# Asia           (2.212, 15.753]         4
#                (15.753, 29.227]        1
# Australia      (2.212, 15.753]         1
# Europe         (2.212, 15.753]         1
#                (15.753, 29.227]        3
#                (29.227, 42.701]        2
# North America  (2.212, 15.753]         1
#                (56.174, 69.648]        1
# South America  (56.174, 69.648]        1
# Name: Country, dtype: int64

# Question 13
# ----------------------------------------
# Quiz Question: Convert the Population Estimate series to a string with thousands separator (using commas).
# Use all significant digits (do not round the results).
# e.g. 12345678.90 -> 12,345,678.90
# This function should return a Series PopEst whose index is the country name and whose values are
# the population estimate string.
def answer_thirteen():
    Top15 = answer_one()
    Top15['Population'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    return Top15['Population'].apply(lambda x: "{:,}".format(x))


print('\nQuestion 13')
print(answer_thirteen())


# Country
# Australia               23,316,017.316
# Brazil                 205,915,254.237
# Canada                 35,239,864.8649
# China                 1,367,645,161.29
# Germany                80,369,696.9697
# Spain                  46,443,396.2264
# France                 63,837,349.3976
# United Kingdom         63,870,967.7419
# India                 1,276,730,769.23
# Iran                   77,075,630.2521
# Italy                  59,908,256.8807
# Japan                  127,409,395.973
# South Korea            49,805,429.8643
# Russian Federation       143,500,000.0
# United States          317,615,384.615

def plot_optional():
    Top15 = answer_one()
    ax = Top15.plot(x='Rank', y='% Renewable', kind='scatter',
                    c=['#e41a1c', '#377eb8', '#e41a1c', '#4daf4a', '#4daf4a', '#377eb8', '#4daf4a', '#e41a1c',
                       '#4daf4a', '#e41a1c', '#4daf4a', '#4daf4a', '#e41a1c', '#dede00', '#ff7f00'],
                    xticks=range(1, 16), s=6 * Top15['2014'] / 10 ** 10, alpha=.75, figsize=[16, 6]);

    for i, txt in enumerate(Top15.index):
        ax.annotate(txt, [Top15['Rank'][i], Top15['% Renewable'][i]], ha='center')
    plt.show()

    print("This is an example of a visualization that can be created to help understand the data. \
This is a bubble chart showing % Renewable vs. Rank. The size of the bubble corresponds to the countries' \
2014 GDP, and the color corresponds to the continent.")


plot_optional()
