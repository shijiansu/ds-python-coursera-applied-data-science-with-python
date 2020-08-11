# -*- coding: UTF-8 -*-
def add_numbers(x, y):
    return x + y


print(type('This is a string'))  # <type 'str'>
print(type(None))  # <type 'NoneType'>
print(type(1))  # <type 'int'>
print(type(1.0))  # <type 'float'>
print(type(add_numbers))  # <type 'function'>

print('----------------------------------------')
x = (1, 'a', 2, 'b')
print(type(x))  # <type 'tuple'>

x = [1, 'a', 2, 'b']
print(type(x))  # <type 'list'>

x.append(3.3)
print(x)  # [1, 'a', 2, 'b', 3.3]

print('----------------------------------------')
for item in x:
    print(item)

i = 0
while i != len(x):
    print(x[i])
    i += 1

print([1, 2] + [3, 4])  # [1, 2, 3, 4]
print([1] * 3)  # [1, 1, 1]
print(1 in [1, 2, 3])  # True

print('----------------------------------------')
x = 'This is a string'
print(x[0])  # first character # T
print(x[0:1])  # first character, but we have explicitly set the end character # T
print(x[0:2])  # first two characters # Th
print(x[-1])  # g
print(x[-4:-2])  # ri
print(x[:3])  # Thi
print(x[3:])  # s is a string

print('----------------------------------------')
firstname = 'Christopher'
lastname = 'Brooks'

print(firstname + ' ' + lastname)  # Christopher Brooks
print(firstname * 3)  # ChristopherChristopherChristopher
print('Chris' in firstname)  # True

firstname = 'Christopher Arthur Hansen Brooks'.split(' ')[0]  # [0] selects the first element of the list
lastname = 'Christopher Arthur Hansen Brooks'.split(' ')[-1]  # [-1] selects the last element of the list
print(firstname)  # Christopher
print(lastname)  # Brooks
print('Chris' + str(2))  # Chris2

print('----------------------------------------')
x = {'Christopher Brooks': 'brooksch@umich.edu', 'Bill Gates': 'billg@microsoft.com'}
print(x['Christopher Brooks'])  # Retrieve a value by using the indexing operator # brooksch@umich.edu

x['Kevyn Collins-Thompson'] = None
print(x['Kevyn Collins-Thompson'])  # None

for name in x:
    print(x[name])

for email in x.values():
    print(email)

for name, email in x.items():
    print(name)
    print(email)

print('----------------------------------------')
# x = ('Christopher', 'Brooks', 'brooksch@umich.edu', 'Ann Arbor') # Error is x has 4 elements
x = ('Christopher', 'Brooks', 'brooksch@umich.edu')
fname, lname, email = x
print(fname)  # Christopher
print(lname)  # Brooks
