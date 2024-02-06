"""
Write a NumPy program to create a 3X4 array and iterate over it.
"""

import numpy as np

array3x4 = np.arange(10,22).reshape(3,4)

print(array3x4)

for element in np.nditer(array3x4):
    print(element, end=" ")


"""
Write a NumPy program to find the number of rows and columns in a given matrix.
"""

print(array3x4.shape, "shape of array array3x4")