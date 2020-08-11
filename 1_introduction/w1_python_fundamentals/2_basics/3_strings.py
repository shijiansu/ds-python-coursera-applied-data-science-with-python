# -*- coding: UTF-8 -*-

# print('Chris' + 2) # error

print('Chris' + str(2))
# Chris2

sales_record = {
    'price': 3.24,
    'num_items': 4,
    'person': 'Chris'}

sales_statement = '{} bought {} item(s) at a price of {} each for a total of {}'

print(sales_statement.format(sales_record['person'],
                             sales_record['num_items'],
                             sales_record['price'],
                             sales_record['num_items'] * sales_record['price']))
# Chris bought 4 item(s) at a price of 3.24 each for a total of 12.96
