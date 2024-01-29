"""
 3. Write a NumPy program to test whether none of the elements of a given array are zero or false
 4. Write a NumPy program to test if any of the elements of a given array are non-zero. 
"""

import numpy as np

array1 = np.array([0,1,0])
print(np.all(array1)) # all method will return true if all the values of an array are true or 1
print(np.any(array1)) # any method will return true if any the values of an array are true or 1 else it will return false