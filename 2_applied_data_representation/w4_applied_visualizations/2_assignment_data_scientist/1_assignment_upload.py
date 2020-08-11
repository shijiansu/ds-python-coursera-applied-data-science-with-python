#!/usr/bin/python
# -*- coding:utf-8 -*-

import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

gdp = pd.read_csv('data/gdp/gross-domestic-product-at-current-market-prices-by-detailed-industry-quarterly.csv')
industries = gdp['level_3'].unique()
print ('\nindustries:')
print(industries)

gdp['year'] = gdp['quarter'].apply(lambda x: x[:4])
gdp['qtr'] = gdp['quarter'].apply(lambda x: x[5:7])
gdp = gdp[(gdp['year'] > '2008') & (gdp['year'] < '2017')]
gdp['year'] = gdp['year'].astype(int)
gdp = gdp[['level_3', 'year', 'qtr', 'value']]
gdp = gdp[gdp['level_3'] == 'Information & Communications']
gdp = gdp.groupby(['year']).sum()
gdp = gdp.reset_index().sort_values(['year'])
gdp = gdp.rename(columns={'value': 'GDP of Infocomm'})

print('\ngdp:')
print(gdp.head(10))


def preprocess_salary(salary):
    salary = salary[(salary['university'] != 'Singapore Institute of Technology')
                    & (salary['university'] != 'Singapore University of Technology and Design')]

    salary = salary[(salary['degree'].str.contains('Computing'))
                    | (salary['degree'].str.contains('Information'))
                    | (salary['degree'].str.contains('Computer'))]

    salary = salary[salary['basic_monthly_mean'] != 'na']
    salary['year'] = salary['year'].astype(int)
    salary['basic_monthly_mean'] = salary['basic_monthly_mean'].astype(int)

    salary = salary[['university', 'year', 'basic_monthly_mean']]
    salary = salary.groupby(['university', 'year'])['basic_monthly_mean'].mean()
    salary = salary.to_frame(name=None)
    salary = salary.reset_index()
    return salary


salary_2013_2015 = pd.read_csv('data/salary/graduate-employment-survey-ntu-nus-sit-smu-sutd.csv')
salary_2013_2015 = preprocess_salary(salary_2013_2015)

salary_2009_2012_2016 = salary2 = pd.read_csv('data/salary_website/salary.txt', dtype=str, delimiter='|', header=0)
salary_2009_2012_2016 = preprocess_salary(salary_2009_2012_2016)
salary_2009_2016 = pd.concat([salary_2013_2015, salary_2009_2012_2016]).sort_values(['university', 'year'])
print('\nsalary_2009_2016:')
print(salary_2009_2016.head(10))

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
print('\ndf:')
print(df)

# http://seaborn.pydata.org/generated/seaborn.pairplot.html
g = sns.pairplot(df, diag_kind='kde', size=3, diag_kws=dict(shade=True))
plt.subplots_adjust(top=0.95)
g.fig.suptitle(
    'Correlation between Singapore Infocomm Industry GDP and '
    'Public Universities Infocomm Related Graduate Employment Average Salary (2009 ~ 2016)')
plt.show()
