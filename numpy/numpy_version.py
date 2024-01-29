"""
1. print the numpy version
2. Write a NumPy program to get help with the add function.
"""
import numpy as np

a1 = np.array([1,2,3,4])
a2 = np.array([1,2,3,4])
print(np.__version__)

# print(np.info(np.add))
print(np.add(a1,a2))
