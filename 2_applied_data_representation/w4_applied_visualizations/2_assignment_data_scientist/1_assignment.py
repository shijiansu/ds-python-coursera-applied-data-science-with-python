#!/usr/bin/python
# -*- coding:utf-8 -*-

# This assignment requires that you identify at least two publicly accessible datasets
# from the same region that are consistent across a meaningful dimension.
# You will state a research question that can be answered using these data sets and then create a visual
# using matplotlib that addresses your stated research question.
# You will then be asked to justify how your visual addresses your research question.
#
# As this assignment is for the whole course,
# you must incorporate and defend the principles discussed in the first week and align with Cairo’s
# principles of truth, beauty, function, and insight.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 加载GDP数据
gdp = pd.read_csv('data/gdp/gross-domestic-product-at-current-market-prices-by-detailed-industry-quarterly.csv')
industries = gdp['level_3'].unique()
print ('\nindustries:')
print(industries)  # 所有行业

gdp['year'] = gdp['quarter'].apply(lambda x: x[:4])  # 获得单独的年
gdp['qtr'] = gdp['quarter'].apply(lambda x: x[5:7])  # 获得单独的季度
gdp = gdp[(gdp['year'] > '2008') & (gdp['year'] < '2017')]  # 只要2009~2016
gdp['year'] = gdp['year'].astype(int)  # 转化为数字类型
gdp = gdp[['level_3', 'year', 'qtr', 'value']]  # 只需要子集数据
gdp = gdp[gdp['level_3'] == 'Information & Communications']  # 获取信息行业
gdp = gdp.groupby(['year']).sum()  # 按年份求和
gdp = gdp.reset_index().sort_values(['year'])  # 使index重排
gdp = gdp.rename(columns={'value': 'GDP of Infocomm'})

print('\ngdp:')
print(gdp.head(10))


# 加载Salary数据
def preprocess_salary(salary):
    salary = salary[(salary['university'] != 'Singapore Institute of Technology')
                    & (salary['university'] != 'Singapore University of Technology and Design')]

    salary = salary[(salary['degree'].str.contains('Computing'))
                    | (salary['degree'].str.contains('Information'))
                    | (salary['degree'].str.contains('Computer'))]  # 获取信息行业相关专业

    salary = salary[salary['basic_monthly_mean'] != 'na']  # 移除空值
    salary['year'] = salary['year'].astype(int)  # 转化为数字类型
    salary['basic_monthly_mean'] = salary['basic_monthly_mean'].astype(int)  # 转化为数字类型

    salary = salary[['university', 'year', 'basic_monthly_mean']]  # 只需要子集数据
    salary = salary.groupby(['university', 'year'])['basic_monthly_mean'].mean()  # 求均值
    salary = salary.to_frame(name=None)  # 转化为dataframe
    salary = salary.reset_index()  # 使index重排
    return salary


salary_2013_2015 = pd.read_csv('data/salary/graduate-employment-survey-ntu-nus-sit-smu-sutd.csv')
salary_2013_2015 = preprocess_salary(salary_2013_2015)

salary_2009_2012_2016 = salary2 = pd.read_csv('data/salary_website/salary.txt', dtype=str, delimiter='|', header=0)
salary_2009_2012_2016 = preprocess_salary(salary_2009_2012_2016)
salary_2009_2016 = pd.concat([salary_2013_2015, salary_2009_2012_2016]).sort_values(['university', 'year'])  # 合并并排序
print('\nsalary_2009_2016:')
print(salary_2009_2016.head(10))

# 行列转换
salary_uni = []
university_shortnames = {'singapore_management_university': 'SMU',
                         'national_university_of_singapore': 'NUS',
                         'nanyang_technological_university': 'NTU'}
universities = salary_2009_2016['university'].unique()
for uni in universities:
    s = salary_2009_2016[salary_2009_2016['university'] == uni]
    s = s[['year', 'basic_monthly_mean']]
    s = s.rename(
        columns={'basic_monthly_mean': 'Salary of ' + university_shortnames[uni.lower().replace(' ', '_')] + ' (SGD)'})
    salary_uni.append(s)

salary = None
for su in salary_uni:
    if salary is None:
        salary = su
        continue
    salary = pd.merge(salary, su, left_on='year', right_on='year', how='left')
print('\nsalary:')
print(salary)

df = pd.merge(salary, gdp, left_on='year', right_on='year', how='left')
df = df.rename(columns={'year': 'Year'})
df = df.set_index('Year')
# df = df[['GDP of Infocomm', 'Salary of NUS', 'Salary of NTU', 'Salary of SMU']]
print('\ndf:')
print(df)

# 显示数据
# http://seaborn.pydata.org/generated/seaborn.pairplot.html
g = sns.pairplot(df, diag_kind='kde', size=3, diag_kws=dict(shade=True))
plt.subplots_adjust(top=0.95)
g.fig.suptitle(
    'Correlation between Singapore Infocomm Industry GDP and '
    'Public Universities Infocomm Related Graduate Employment Average Salary (2009 ~ 2016)')
plt.show()
