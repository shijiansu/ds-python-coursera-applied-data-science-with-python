# -*- coding: UTF-8 -*-
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

import scipy.stats as stats

distribution = np.random.normal(0.75, size=1000)

stats.kurtosis(distribution)
# -0.1506146015236216

stats.skew(distribution)
# -0.08323660959774026

chi_squared_df2 = np.random.chisquare(2, size=10000)
stats.skew(chi_squared_df2)
# 2.0285858644049544

chi_squared_df5 = np.random.chisquare(5, size=10000)
stats.skew(chi_squared_df5)
# 1.3166751301377153

output = plt.hist([chi_squared_df2, chi_squared_df5], bins=50, histtype='step',
                  label=['2 degrees of freedom', '5 degrees of freedom'])
plt.legend(loc='upper right')
plt.show()
