"""

6. Write a NumPy program to test elements-wise for positive or negative infinity. 
"""

import numpy as np

array1 = np.array([0,1,-10,-20, np.nan, -np.inf, np.inf])

print(array1)
print(np.isinf(array1))