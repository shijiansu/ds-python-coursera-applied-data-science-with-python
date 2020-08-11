# -*- coding: UTF-8 -*-

my_function = lambda a, b, c : a + b
print(my_function(1, 2, 3))
# 3

my_list = []
for number in range(0, 1000):
    if number % 2 == 0:
        my_list.append(number)
print(my_list)
# [0, 2, 4, 6, 8, ..., 994, 996, 998]

my_list = [number for number in range(0,1000) if number % 2 == 0]
print(my_list)
# [0, 2, 4, 6, 8, ..., 994, 996, 998]
