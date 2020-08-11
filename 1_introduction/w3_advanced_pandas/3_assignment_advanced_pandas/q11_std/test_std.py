import numpy as np

asia_values = np.array([7.707563e+07, 1.276731e+09, 1.367645e+09, 1.274094e+08, 4.980543e+07])
print(np.std(asia_values))
# 607403627.241

print(np.std(asia_values, ddof=1))
# 679097900.145
