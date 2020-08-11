# -*- coding: UTF-8 -*-
import datetime as dt
import time as tm

# time returns the current time in seconds since the Epoch. (January 1st, 1970)
print(tm.time())

# Convert the timestamp to datetime.
dtnow = dt.datetime.fromtimestamp(tm.time())
print(dtnow)  # 2016-11-03 16:10:34.633000

# Handy datetime attributes:
print('year:{}, month:{}, day:{}'.format(dtnow.year, dtnow.month, dtnow.day))
print('hour:{}, minute:{}, second:{}'.format(dtnow.hour, dtnow.minute, dtnow.second))
# year:2016, month:11, day:3
# hour:16, minute:10, second:34

# timedelta is a duration expressing the difference between two dates.
delta = dt.timedelta(days=100)  # create a timedelta of 100 days
today = dt.date.today()
print(today - delta)  # the date 100 days ago # 2016-07-26
print(today > today - delta)  # compare dates # True
