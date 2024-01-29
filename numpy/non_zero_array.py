"""
 Write a NumPy program to test whether none of the elements of a given array are zero or false
"""

import numpy as np

array1 = np.array([1,0,1])
print(np.all(array1))