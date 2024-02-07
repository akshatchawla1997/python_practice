"""
Write a NumPy program to compute the sum of all elements, the sum of each column and the sum of each row in a given
array.
"""

import numpy as np

array = np.array([[1,40],[10,20]])

print(f"original array {array}")


sum = np.sum(array)

axis_sum = np.sum(array, axis=0)
print(axis_sum,"axis sum")
axis_sum = np.sum(array, axis=1)
print(axis_sum,"axis sum")

print(sum)