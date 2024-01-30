"""
1. print the numpy version
2. Write a NumPy program to get help with the add function.
3. Write a NumPy program to get the addition, subtraction, division, multiplication
"""
import numpy as np

a1 = np.array([1,2,3,4])
a2 = np.array([4,3,2,1])
print(np.__version__)

# print(np.info(np.add))
print(np.add(a1,a2))
addition = a1 + a2
multiplication = a1 * a2
difference = a1 - a2
division = a1/a2
print(addition)
print(difference)
print(multiplication)
print(division)
