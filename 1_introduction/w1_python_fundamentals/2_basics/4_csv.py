# -*- coding: UTF-8 -*-
import csv
import numpy as np

# mpg是每加仑英里, 为车辆油耗指标
with open('data/mpg.csv') as csvfile:
    mpg = list(csv.DictReader(csvfile))

# mpg[:3]  # The first three dictionaries in our list.
print(len(mpg))  # 234
print(mpg[0].keys())
# ['', 'trans', 'displ', 'hwy', 'cty', 'drv', 'year', 'model', 'manufacturer', 'fl', 'class', 'cyl']

print('----------------------------------------')
# get average
print(sum(float(d['cty']) for d in mpg) / len(mpg))  # 16.858974359
print(sum(float(d['hwy']) for d in mpg) / len(mpg))  # 23.4401709402

print('----------------------------------------')
# 求各类气缸数量的车辆的平均油耗量
# unique values
cylinders = set(d['cyl'] for d in mpg)  # 气缸
print(cylinders)
# set(['8', '5', '4', '6'])

# grouping the cars by number of cylinder
CtyMpgByCyl = []

# 这个嵌套循环的效率不太好, 因为是通过遍历去判断d['cyl'] == c, 先做个切片再循环就好了
for c in cylinders:  # iterate over all the cylinder levels
    summpg = 0
    cyltypecount = 0
    for d in mpg:  # iterate over all dictionaries
        if d['cyl'] == c:  # if the cylinder level type matches,
            summpg += float(d['cty'])  # add the cty mpg # 根据上下文, 为油耗量吧
            cyltypecount += 1  # increment the count
    # 求对应的气缸数中, 平均每辆车辆的油耗量
    CtyMpgByCyl.append((c, summpg / cyltypecount))  # append the tuple ('cylinder', 'avg mpg')

CtyMpgByCyl.sort(key=lambda x: x[0])
print(np.matrix(CtyMpgByCyl))
# [['4' '21.012345679']
#  ['5' '20.5']
#  ['6' '16.2151898734']
#  ['8' '12.5714285714']]

print('----------------------------------------')
# 求各类车辆类型的车辆的平均油耗量
vehicleclass = set(d['class'] for d in mpg)  # what are the class types
print(vehicleclass)
# set(['compact', 'subcompact', '2seater', 'suv', 'pickup', 'midsize', 'minivan'])

HwyMpgByClass = []

for t in vehicleclass:  # iterate over all the vehicle classes
    summpg = 0
    vclasscount = 0
    for d in mpg:  # iterate over all dictionaries
        if d['class'] == t:  # if the cylinder amount type matches,
            summpg += float(d['hwy'])  # add the hwy mpg
            vclasscount += 1  # increment the count
    HwyMpgByClass.append((t, summpg / vclasscount))  # append the tuple ('class', 'avg mpg')

HwyMpgByClass.sort(key=lambda x: x[1])
print(np.matrix(HwyMpgByClass))
# [['pickup' '16.8787878788']
#  ['suv' '18.1290322581']
#  ['minivan' '22.3636363636']
#  ['2seater' '24.8']
#  ['midsize' '27.2926829268']
#  ['subcompact' '28.1428571429']
#  ['compact' '28.2978723404']]
