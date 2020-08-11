# -*- coding: UTF-8 -*-
x = 1
y = 2
print(x + y)  # 3
print(x)  # 1

print('----------------------------------------')


def add_numbers(x, y):
    return x + y


print(add_numbers(1, 2))  # 3

print('----------------------------------------')


def add_numbers(x, y, z=None):
    if z is None:
        return x + y
    else:
        return x + y + z


print(add_numbers(1, 2))  # 3
print(add_numbers(1, 2, 3))  # 4

print('----------------------------------------')


def add_numbers(x, y, z=None, flag=False):
    if flag:
        print('Flag is true!')  # Flag is true!
    if z is None:
        return x + y
    else:
        return x + y + z


print(add_numbers(1, 2, flag=True))  # 3

print('----------------------------------------')
a = add_numbers
print(a(1, 2))  # 3
