
First of all I must say thank you to everyone in the discussion of this course!

I would like to share some issues I faced in the week 4 assignment. I hope this would help you.
My understanding is just for your reference, it may not be 100% accurate.

1. Unlike with other weeks' assignment, this week assignment questions closely relate to the instruction on the top.

2. get_list_of_university_towns()
1) In the assignment, it shows "dictionary to map state names" before this question.
It may suggest us to use states dictionary to answer this question.
Please keep an open mind and check the university_towns.txt,
there may have another way to process the text file values. Getting the State and RegionName without
using states dictionary (map, merge, or some other functions) is possible.

2) To get the RegionName, you need to remove the (...) and [edit]. Please mind if there is space after you remove (...).

3) For your reference,
print(towns.dtypes)
# State object
# RegionName object
# dtype: object

4) This function should return a DataFrame with 2 columns and 517 entries. The column names are [State, RegionName]

3. get_recession_start() & get_recession_end() & get_recession_bottom()
1) GDP data only from the first quarter of 2000 onward
URL: https://www.coursera.org/learn/python-data-analysis/discussions/weeks/4/threads/we0YuaKQEeaprQ4LnRHZcg

2) Definitions of recession,
Thanks for Chris Little, his answer really saved me.
URL: https://www.coursera.org/learn/python-data-analysis/discussions/weeks/4/threads/fePT_6GkEeaURQ7PXsSdbA
Well, let me give you an example here. Let us say we have below years with quarter and GDP,
Year_Quarter GDP
2000q4 100 # quarter before recession
2001q1 100 # start of recession
2001q2 90
2001q3 80 # at this point, we know recession happens
2001q4 70 # bottom of recession
2002q1 80
2002q2 90 # end of recession
A discussion about how to get the value:
URL: https://www.coursera.org/learn/python-data-analysis/discussions/weeks/4/threads/vagcU6N5EeagbRJODex4yg

3) Those functions should return a string, e.g. 2000q4

4. convert_housing_data_to_quarters()
1) If you are renaming the column name, you may get some inspiration from,
URL: https://www.coursera.org/learn/python-data-analysis/discussions/weeks/4/threads/KcdnFaMAEeaWGQ4arwmx_A
Or, it is possible to just do a looping in columns.

2) This function should return a DataFrame with 67 columns and 10730 entries. The index names are [State, RegionName].

5. run_ttest()
1) About 'First creates new data showing the decline or growth of housing prices between the recession start
and the recession bottom.'
I think here is to ask us plot the data, but I think it is not a part of the t-test question.
I did once to get all year/quater between the recession start and the recession bottom,
but I find it is nowhere to use later.

2) About 'Then runs a ttest comparing the university town values to the non-university towns values,'
According to the context, I guess the "values" here referring to the price ratio.

3) Definition of price ratio,
It is from the instruction on the top,
"price_ratio=quarter_before_recession/recession_bottom",
which is the ratio of (price of quarter_before_recession / price of recession_bottom)

4) My understanding for "mean",
- mean price: As we got the mean value of house prices in the same quarters,
it refers to the values from convert_housing_data_to_quarters();
- mean price ratio: It suggests us to get the price ratios mean value for the final answer - "better";

5) About the dataframes of university town and non-university town
I do not do the extra data cleaning at the RegionName other than the assignment required.
For your reference,
# ut -> university town; nut -> non-university town
print(len(df_ut)) # 269
print(len(df_ut.dropna())) # 247
print(len(df_nut)) # 10461
print(len(df_nut.dropna())) # 9108

6) This function should return a tuple. e.g. (different, p, better)
# different: True or False;
# p: p-value in the t test, which is a reasonable value;
# better: "university town" or "non-university town";
