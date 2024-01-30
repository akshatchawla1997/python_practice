"""
1. print the numpy version
2. Write a NumPy program to get help with the add function.
3. Write a NumPy program to get the addition, subtraction, division, multiplication
"""
import numpy as np

a1 = np.array([[1,2,3,4],[10,12,13,14]])
a2 = np.array([[4,3,2,1],[1,2,3,4],[10,12,13,14]])
print(np.__version__)

# Get dimensions of a1 as array 1
print(a1.ndim)

# Get Shape
print(a1.shape)
print(a2.shape)

# Get type
print(a1.dtype)

# Get Size
print(a1.size)

# Get total size
print(a1.nbytes)

# Get a specific item [row, column]
print(a1[1,2])

# Get a specific row
print(a1[0,:])

# print(np.info(np.add))
# print(np.add(a1,a2))
# addition = a1 + a2
# multiplication = a1 * a2
# difference = a1 - a2
# division = a1/a2
# print(addition)
# print(difference)
# print(multiplication)
# print(division)
