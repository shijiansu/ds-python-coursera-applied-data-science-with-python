#!/usr/bin/python
# -*- coding:utf-8 -*-

import matplotlib as mpl
import matplotlib.pyplot as plt

print(mpl.get_backend())

plt.plot(3, 2)
plt.show()

plt.plot(3, 2, '.')
plt.show()
