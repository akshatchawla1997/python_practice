"""
Write a NumPy program to test element-wise for complex numbers, real numbers in a given
array. Also test if a given number is of a scalar type or not.

"""

import numpy as np

array = np.array([1+1j, 1+0j, 4.5, 3, 2, 2j])

print(array)
print(np.iscomplex(array))
print(np.isreal(array))
print(np.isscalar(array))
print(np.isscalar(2.1))