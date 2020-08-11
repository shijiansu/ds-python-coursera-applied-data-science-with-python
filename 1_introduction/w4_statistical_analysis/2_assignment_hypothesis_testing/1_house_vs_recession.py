# -*- coding: UTF-8 -*-
from __future__ import division

import pandas as pd


# 思路分析:
# # 问题: 这里先是做了一个假设, 该假设是大学城镇再经济衰退的房价跌幅没有非大学城镇的多.
# # 1. 通过university_towns.txt, 找出大学城镇;
# # 2. 通过gdplev.xls里面GDP的值, 找出衰退期;
# # 3. 通过City_Zhvi_AllHomes.csv, 找出房价的值;
# ## 具体一些坑, 请参阅1_house_price_vs_recession_readme.sh
# # 数据源:
# ## 通过university_towns.txt: 貌似是从Wiki下载而来的, 可以通过文本处理而获得州及大学城镇. 州后面单纯以[edit]结尾;
# ## gdplev.xls: 历年各季度的GDP;
# ## City_Zhvi_AllHomes.csv: 每月的房价值, 需要通过地区Code转为城镇名称, 并且将每3个月合成季度数据;
# # 关键点:
# # 由于3个数据源之间的主键(Region Name)不一样, 所以需要对其做基本的数据清洗. 联合主键为State + Region Name.
# 由于GDP的数据是季度的, 所以要把房价的数据转为季度.
# # 对recession的定义要掌握, 具体如下,
# # Year_Quarter GDP
# # 2000q4 100 # quarter before recession
# # 2001q1 100 # start of recession
# # 2001q2 90
# # 2001q3 80 # at this point, we know recession happens
# # 2001q4 70 # bottom of recession
# # 2002q1 80
# # 2002q2 90 # end of recession

# This assignment requires more individual learning than previous assignments - you are encouraged to check out
# the pandas documentation to find functions or methods you might not have used yet, or ask questions on
# Stack Overflow and tag them as pandas and python related. And of course,
# the discussion forums are open for interaction with your peers and the course staff.
# Definitions:
# - A quarter is a specific three month period, Q1 is January through March,
#   Q2 is April through June, Q3 is July through September, Q4 is October through December.
# - A recession is defined as starting with two consecutive quarters of GDP decline,
#   and ending with two consecutive quarters of GDP growth.
# - A recession bottom is the quarter within a recession which had the lowest GDP.
# - A university town is a city which has a high percentage of university students compared
#   to the total population of the city.
#
# Hypothesis: University towns have their mean housing prices (指季度的中每月房价的mean) less effected by recessions.
# Run a t-test to compare the ratio of the mean price of houses in university towns the quarter
# before the recession starts compared to the recession bottom. (price_ratio=quarter_before_recession/recession_bottom)
# The following data files are available for this assignment:
# - From the Zillow research data site there is housing data for the United States.
# In particular the datafile for all homes at a city level, City_Zhvi_AllHomes.csv,
# has median home sale prices at a fine grained level.
# - From the Wikipedia page on college towns is a list of university towns in the United States which has been copy
# and pasted into the file university_towns.txt.
# - From Bureau of Economic Analysis, US Department of Commerce, the GDP over time of the United States
# in current dollars (use the chained value in 2009 dollars), in quarterly intervals, in the file gdplev.xls.
# For this assignment, only look at GDP data from the first quarter of 2000 onward.
#
# Each function in this assignment below is worth 10%, with the exception of run_ttest(), which is worth 50%.

# Question 1
# ----------------------------------------
# Quiz Question: Returns a DataFrame of towns and the states they are in from the university_towns.txt list.
# The format of the DataFrame should be: DataFrame( [ ["Michigan","Ann Arbor"], ["Michigan", "Yipsilanti"] ],
# columns=["State","RegionName"])
# This function should return a DataFrame with 2 columns and 517 entries. The column names are [State, RegionName]
def get_list_of_university_towns():
    df = pd.read_csv('data/university_towns.txt', dtype=str, delimiter='|', header=None)

    import re
    # 正则表达式对大学所在城市去除 (....)[...]. 保留州的[edit]作为标识
    df = df.apply(lambda x: re.sub(' \(.*', '', x[0]), axis=1)  # x is Series data type

    index = 0
    state_region = []
    current_state = ''
    for i in range(len(df)):
        name = df.iloc[i]
        # get the state name, and skip to next line
        if "[edit]" in name:  # 有[edit]的就是所在州了
            current_state = name.replace('[edit]', '')  # 在该州下面的列都是所属的RegionName
            continue
        # construct one line of data frame
        state_region.append(pd.Series({'State': current_state, 'RegionName': name}))
        index += 1
    # convert
    df_final = pd.DataFrame(state_region, index=range(len(state_region)), columns=['State', 'RegionName'])
    return df_final


print('\nQuestion 1')
towns = get_list_of_university_towns()
print(towns.dtypes)
# State         object
# RegionName    object
# dtype: object
print(towns.shape)  # (517, 2)
print(towns.head(1))


#      State    RegionName
# 0  Alabama        Auburn


# Question 2
# ----------------------------------------
# Quiz Question: Return recession start time.
# Those functions should return a string, e.g. 2000q4
def get_gdp():
    # Load data
    df = pd.read_excel("data/gdplev.xls", skiprows=5)
    df = df.iloc[2:, 4:-1]
    df.index -= 2  # 使index从0开始
    df.columns = ['Year_Quarter', 'Current', '2009']
    return df


def get_recession_start():
    df = get_gdp()
    # only look at GDP data from the first quarter of 2000 onward
    _2000q1 = df[df['Year_Quarter'] == '2000q1'].index[0]  # 获取对应index

    gdp = df['Current']
    for i in range(_2000q1, len(df)):
        if (gdp[i] < gdp[i - 1]) and (gdp[i - 1] < gdp[i - 2]):
            # print df.loc[i, 'Year_Quarter']
            # get back to 2 Q ago...
            start = df.loc[i - 2, 'Year_Quarter']
            break
    return start


print('\nQuestion 2')
print(get_recession_start())  # 2008q3


# Question 3
# ----------------------------------------
# Quiz Question: Return recession end time.
# Those functions should return a string, e.g. 2000q4
def get_recession_end():
    df = get_gdp()
    # only look at GDP data from the first quarter of 2000 onward
    start = get_recession_start()
    start = df[df['Year_Quarter'] == start].index[0] + 2  # 获取对应index, +2是真正确认为衰退

    gdp = df['Current']
    for i in range(start, len(df)):
        if (gdp[i] > gdp[i - 1]) and (gdp[i - 1] > gdp[i - 2]):
            end = df.loc[i, 'Year_Quarter']
            break
    return end


print('\nQuestion 3')
print(get_recession_end())  # 2009q4


# Question 4
# ----------------------------------------
# Quiz Question: Return recession bottom time.
# Those functions should return a string, e.g. 2000q4
def get_recession_bottom():
    df = get_gdp()
    df = df.set_index('Year_Quarter')

    start = get_recession_start()
    end = get_recession_end()
    bottom = df.loc[start: end]['Current'].argmin()
    return bottom


print('\nQuestion 4')
print(get_recession_bottom())  # 2009q2

# Question 5
# ----------------------------------------
# Quiz Question: Converts the housing data to quarters and returns it as mean values in a dataframe.
# This dataframe should be a dataframe with columns for 2000q1 through 2016q3, and should have a multi-index
# in the shape of ["State","RegionName"].
# Note: Quarters are defined in the assignment description, they are not arbitrary three month periods.
# This function should return a DataFrame with 67 columns and 10730 entries. The index names are [State, RegionName].
# Use this dictionary to map state names to two letter acronyms
states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 'NA': 'National',
          'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana',
          'IL': 'Illinois', 'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho',
          'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan',
          'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico',
          'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', 'MP': 'Northern Mariana Islands', 'IA': 'Iowa',
          'MO': 'Missouri', 'CT': 'Connecticut', 'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana',
          'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California',
          'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island',
          'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia',
          'ND': 'North Dakota', 'VA': 'Virginia'}


# 将每三个月的房屋价格数据转为季度数据
def convert_housing_data_to_quarters():
    # Load data
    df = pd.read_csv('data/City_Zhvi_AllHomes.csv')

    # replace to state name by mapping
    df['State'] = df['State'].apply(lambda x: states.get(x))
    # print(df.columns)

    df_final1 = group_month_to_quarter1(df)
    df_final2 = group_month_to_quarter2(df)
    print('2 Grouping Approach Compare: {}'.format(df_final1.equals(df_final2)))

    # print(df_final1.values == df_final2.values)/

    df_final = df_final2
    df_final['State'] = df['State']
    df_final['RegionName'] = df['RegionName']
    df_final.set_index(['State', 'RegionName'], inplace=True)

    # # print df_final.head(1)
    return df_final


# 这个方法是利用循环的. 思路为每3个为一步, 然后组建新的列并赋值
def group_month_to_quarter1(df):
    # 由于缺少了2016-09而不能被3整除, 所以预先加上一列, 值为2016-07和2016-08的mean值. 这样可不影响后续求mean逻辑
    df['2016-09'] = (df['2016-07'] + df['2016-08']).mean()
    # only get needed columns
    years = df.columns[6:]  # ignore region name, state, etc.
    _2000 = years[[int(x.replace('-', '')) > 200000 for x in years]]  # filter only > 200001

    df_final = pd.DataFrame()
    for i in range(0, len(_2000), 3):
        y = _2000[i].split('-')  # 2000-01 -> 2000, 01
        new_column = y[0] + 'q' + str((int(y[1]) // 3) + 1)  # (int('03'))//3) + 1 = 1//3 + 1 = 1
        df_final[new_column] = df[[_2000[i], _2000[i + 1], _2000[i + 2]]].mean(axis=1)
    return df_final


# 这个方法是直接改去列名, 然后通过转置+groupby去求mean, 然后再转置为原来的格式
def group_month_to_quarter2(df):
    # only get needed columns
    years = df.columns[6:]  # ignore region name, state, etc.
    _2000 = years[[int(x.replace('-', '')) > 200000 for x in years]]  # filter only > 200001

    # 这里split后[1]需要减1是因为避免3,6,9,12的计算错误
    df_final = df[_2000].rename(
        columns={x: x.split('-')[0] + 'q' + str(((int(x.split('-')[1]) - 1) // 3) + 1) for x in _2000})

    # import numpy as np
    # df_final = df_final.T.groupby(level=0).agg(np.mean).T
    df_final = df_final.groupby(df_final.columns, axis=1).mean()  # 这个更直观!
    return df_final


print('\nQuestion 5')
data = convert_housing_data_to_quarters()
print(data.shape)  # (10730, 67)
print(data.columns)


# Index([u'2000q1', u'2000q2', u'2000q3', u'2000q4', u'2001q1', u'2001q2',
#        u'2001q3', u'2001q4', u'2002q1', u'2002q2', u'2002q3', u'2002q4',
#        u'2003q1', u'2003q2', u'2003q3', u'2003q4', u'2004q1', u'2004q2',
#        u'2004q3', u'2004q4', u'2005q1', u'2005q2', u'2005q3', u'2005q4',
#        u'2006q1', u'2006q2', u'2006q3', u'2006q4', u'2007q1', u'2007q2',
#        u'2007q3', u'2007q4', u'2008q1', u'2008q2', u'2008q3', u'2008q4',
#        u'2009q1', u'2009q2', u'2009q3', u'2009q4', u'2010q1', u'2010q2',
#        u'2010q3', u'2010q4', u'2011q1', u'2011q2', u'2011q3', u'2011q4',
#        u'2012q1', u'2012q2', u'2012q3', u'2012q4', u'2013q1', u'2013q2',
#        u'2013q3', u'2013q4', u'2014q1', u'2014q2', u'2014q3', u'2014q4',
#        u'2015q1', u'2015q2', u'2015q3', u'2015q4', u'2016q1', u'2016q2',
#        u'2016q3'],
#       dtype='object')

# Question 6
# ----------------------------------------
# Quiz Question: First creates new data showing the decline or growth of housing prices
# between the recession start and the recession bottom (和题目要求所做无关).
# Then runs a ttest comparing the university town values (指price_ratio) to the non-university towns values,
# return whether the alternative hypothesis (that the two groups are the same)
# is true or not as well as the p-value of the confidence.
#
# Return the tuple (different, p, better) where different=True if the t-test is
# True at a p<0.01 (we reject the null hypothesis), or different=False if
# otherwise (we cannot reject the null hypothesis). The variable p should
# be equal to the exact p value returned from scipy.stats.ttest_ind(). The
# value for better should be either "university town" or "non-university town"
# depending on which has a lower mean price ratio (求出price ratio的mean进行比较)
# (which is equivilent to a reduced market loss).
# This function should return a tuple. e.g. (different, p, better)
def run_ttest(if_debug=False):
    # Load data
    uni_towns = get_list_of_university_towns()
    prices = convert_housing_data_to_quarters()

    # get related years
    start = get_recession_start()
    years = prices.columns
    before = years[years.tolist().index(start) - 1]
    bottom = get_recession_bottom()
    print('year quarter start recession: {}, before recession: {}, recession bottom: {}'.format(start, before, bottom))
    # year quarter start recession: 2008q3, before recession: 2008q2, recession bottom: 2009q2

    # according to the Hypothesis description
    prices['PriceRatio'] = prices[before] / prices[bottom]

    # tell which group
    uni_towns['UniversityInd'] = 1
    uni_towns.set_index(['State', 'RegionName'], inplace=True)
    prices = pd.merge(prices, uni_towns, how='left', left_index=True, right_index=True)
    prices['UniversityInd'] = prices['UniversityInd'].fillna(0)

    # get 2 t-test data set
    df_ut = prices[prices['UniversityInd'] == 1]
    if if_debug:
        print('\nlen(df_ut): {}'.format(len(df_ut)))  # 269
        print('len(df_ut): {}'.format(len(df_ut.dropna())))  # 247
        print('df_ut PriceRatio Mean: {}'.format(df_ut.dropna()['PriceRatio'].mean()))  # 1.05789995005
        # print df_ut['PriceRatio']
    df_ut = df_ut.dropna()

    df_nut = prices[prices['UniversityInd'] == 0]
    if if_debug:
        print('\nlen(df_nut): {}'.format(len(df_nut)))  # 10461
        print('len(df_nut.dropna): {}'.format(len(df_nut.dropna())))  # 9108
        print('df_nut PriceRatio Mean: {}'.format(df_nut.dropna()['PriceRatio'].mean()))  # 1.07739511541
        # print df_nut['PriceRatio']
    df_nut = df_nut.dropna()

    from scipy.stats import ttest_ind
    ttest_result = ttest_ind(df_ut['PriceRatio'], df_nut['PriceRatio'])
    p = ttest_result[1]
    different = p < 0.01
    if df_ut['PriceRatio'].mean() <= df_nut['PriceRatio'].mean():
        better = 'university town'
    else:
        better = 'non-university town'
    return different, p, better


print('\nQuestion 6')
print(run_ttest(True))  # (True, 0.0051648663279190233, 'university town')
