# -*- coding: UTF-8 -*-
from __future__ import division
import pandas as pd

# For the next set of questions, we will be using census data from the United States Census Bureau.
# Counties are political and geographic subdivisions of states in the United States.
# This dataset contains population data for counties and states in the US from 2010 to 2015.
# See this document for a description of the variable names.
# The census dataset (census.csv) should be loaded as census_df. Answer questions using this as appropriate.

census_df = pd.read_csv('../data/census.csv')
print(census_df.head(1))


#    SUMLEV  REGION  DIVISION  STATE  COUNTY   STNAME  CTYNAME  CENSUS2010POP  \
# 0      40       3         6      1       0  Alabama  Alabama        4779736
#    ESTIMATESBASE2010  POPESTIMATE2010     ...       RDOMESTICMIG2011  \
# 0            4780127          4785161     ...               0.002295
#    RDOMESTICMIG2012  RDOMESTICMIG2013  RDOMESTICMIG2014  RDOMESTICMIG2015  \
# 0         -0.193196          0.381066          0.582002         -0.467369
#    RNETMIG2011  RNETMIG2012  RNETMIG2013  RNETMIG2014  RNETMIG2015
# 0     1.030015     0.826644     1.383282     1.724718     0.712594


# Question 5
# ----------------------------------------
# Quiz Question: Which state has the most counties in it? (hint: consider the sumlevel key carefully!
# You'll need this for future questions too...)
# This function should return a single string value.
def answer_five():
    stnames = census_df.groupby(census_df['STNAME'])
    # print(stnames) # pandas.core.groupby.DataFrameGroupBy object at 0x0000000006BE4A90>
    return stnames['COUNTY'].count().argmax()


def answer_five2():
    # 'STNAME' becomes the index name
    county_grp = census_df['COUNTY'].groupby(census_df['STNAME'])
    # print(county_grp) # <pandas.core.groupby.SeriesGroupBy object at 0x0000000006BE4A90>
    return county_grp.count().argmax()


print('\nQuestion 5')
print(answer_five())  # Texas
print(answer_five2())  # Texas


# Question 6
# ----------------------------------------
# Quiz Question: Only looking at the three most populous counties for each state, what are the three
# most populous states (in order of highest population to lowest population)?
# This function should return a list of string values.
def answer_six():
    # 1. Remove sub level = 40 (state level)
    df = census_df[census_df['SUMLEV'] == 50]

    # 2. First is to get top 3 most populous counties for each state
    group_by_state = df.groupby(census_df['STNAME'])
    top3_country = group_by_state['POPESTIMATE2015'].nlargest(3)
    # print(top3_grp)
    # STNAME
    # Alabama           0        4779736
    #                   37        658466
    #                   49        412992

    # make index as list with column names. "top3" variable here is same as "top3_country".
    top3 = top3_country.reset_index()
    # print(top3)
    #                    STNAME  level_1  CENSUS2010POP
    # 0                 Alabama        0        4779736
    # 1                 Alabama       37         658466
    # 2                 Alabama       49         412992

    # 3. Sum the value by state and get the top 3 most populous states
    group_by_state_in_top3 = top3.groupby(top3['STNAME'])
    county = group_by_state_in_top3['POPESTIMATE2015'].sum()
    # print(county)
    # STNAME
    # Alabama                  5851194
    # Alaska                   1099638
    # Arizona                 11189397
    return county.nlargest(3).index.values.tolist()


print('\nQuestion 6')
print(type(answer_six()))  # <class 'list'>
print(answer_six())  # ['California', 'Texas', 'Illinois']


# Question 7
# ----------------------------------------
# Quiz Question: Which county has had the largest absolute change in population within the period 2010-2015?
# (Hint: population values are stored in columns POPESTIMATE2010 through POPESTIMATE2015,
# you need to consider all six columns.)
# e.g. If County Population in the 5 year period is 100, 120, 80, 105, 100, 130,
# then its largest change in the period would be |130-80| = 50.
# This function should return a single string value.
def answer_seven():
    # remove sub level = 40 (state level)
    df = census_df[census_df['SUMLEV'] == 50]

    # largest change would be the max population during the 5-year period minus the min population
    df2 = pd.DataFrame()
    years = ['POPESTIMATE2010', 'POPESTIMATE2011', 'POPESTIMATE2012', 'POPESTIMATE2013', 'POPESTIMATE2014',
             'POPESTIMATE2015']

    # 重新组合一个data frame
    df2['CTYNAME'] = df['CTYNAME']
    df2['Y_MIN'] = df[years].min(axis=1)
    df2['Y_MAX'] = df[years].max(axis=1)
    df2['Y_CHANGE'] = abs(df2['Y_MAX'] - df2['Y_MIN'])
    # print(df2)
    #                  CTYNAME   Y_MIN   Y_MAX  Y_CHANGE
    # 1         Autauga County   54660   55347       687
    # 2         Baldwin County  183193  203709     20516
    # 3         Barbour County   26489   27341       852

    # print(df2['Y_CHANGE'].nlargest(5))
    # 获取最大Y_CHANGE值的索引值, 后续再通过dataframe.loc去定位到该行.
    # dataframe.iloc按下标选取，或者使用dataframe.loc按索引选取.
    index = df2['Y_CHANGE'].argmax()
    # print(index) # 2667
    return df2.loc[index, 'CTYNAME']


print('\nQuestion 7')
print(answer_seven())  # Harris County


def answer_seven_2():
    df = pd.DataFrame(census_df[census_df['SUMLEV'] == 50])
    grouped_max = df[['POPESTIMATE2015', 'POPESTIMATE2014', 'POPESTIMATE2013', 'POPESTIMATE2012', 'POPESTIMATE2011',
                      'POPESTIMATE2010']].max(axis=1)
    grouped_min = df[['POPESTIMATE2015', 'POPESTIMATE2014', 'POPESTIMATE2013', 'POPESTIMATE2012', 'POPESTIMATE2011',
                      'POPESTIMATE2010']].min(axis=1)
    df['Difference'] = (grouped_max - grouped_min).abs()
    print(df[['CTYNAME', 'Difference']].max()[0])


answer_seven_2()


# Question 8
# ----------------------------------------
# Quiz Question: In this datafile, the United States is broken up into four regions using the "REGION" column.
# Create a query that finds the counties that belong to regions 1 or 2, whose name starts with 'Washington',
# and whose POPESTIMATE2015 was greater than their POPESTIMATE 2014.
# This function should return a 5x2 DataFrame with the columns = ['STNAME', 'CTYNAME'] and the same
# index ID as the census_df (sorted ascending by index).
def answer_eight():
    # remove sub level = 40 (state level)
    df = census_df[census_df['SUMLEV'] == 50]

    condition = ((df['REGION'] == 1) | (df['REGION'] == 2)) \
                & (df['CTYNAME'].str.startswith('Washington')) \
                & (df['POPESTIMATE2015'] > df['POPESTIMATE2014'])
    # default is sorted ascending by index
    return df[condition].iloc[:5, :].loc[:, ['STNAME', 'CTYNAME']]


print('\nQuestion 8')
print(answer_eight())
#             STNAME            CTYNAME
# 896           Iowa  Washington County
# 1419     Minnesota  Washington County
# 2345  Pennsylvania  Washington County
# 2355  Rhode Island  Washington County
# 3163     Wisconsin  Washington County
