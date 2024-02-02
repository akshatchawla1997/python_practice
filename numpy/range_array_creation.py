"""
Write a NumPy program to create an array of integers from 30 to 70.
"""

import numpy as np
# python code to print numbers in a given range
array1 = np.arange(30,70)
print(array1)

# python code to print even numbers in a given range
array1 = np.arange(30,70,2)
print(array1)

# python code to print odd numbers in a given range
start = 30
end = 40
start = start + 1 if start % 2 == 0 else start
array1 = np.arange(start,end,2)
print(array1)