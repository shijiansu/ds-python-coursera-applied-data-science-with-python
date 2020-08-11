# -*- coding: UTF-8 -*-

store1 = [10.00, 11.00, 12.34, 2.34]
store2 = [9.00, 11.10, 12.34, 2.01]
cheapest = map(min, store1, store2)
print(cheapest)
# [9.0, 11.0, 12.34, 2.01]

for item in cheapest:
    print(item)
# 9.0
# 11.0
# 12.34
# 2.01
