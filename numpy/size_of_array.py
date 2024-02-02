"""
Write a NumPy program to create an array with the values 1, 7, 13, 105 and determine the 
size of the memory occupied by the array.

"""

import numpy as np 
array1 = np.array([1, 7, 13, 105])

print(array1.size * array1.itemsize)