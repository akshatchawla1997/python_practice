"""
NumPy: Create a vector with values ​​from 0 to 20 and change the sign of the numbers in the range from 9 to 15
"""

import numpy as np

array = np.arange(20)

print(array,"the given array is")

for element in np.nditer(array):
    if element <= 15 and element >= 9:
        print(element * -1)
    else:
        print(element)

# Printing a message indicating changing the sign of numbers in the range from 9 to 15
# Using boolean indexing, multiplying elements between 9 and 15 by -1 to change their sign
array[(array >= 9) & (array <= 15)] *= -1

# after changeing the array with list comprehension is 
print(array, "after updation")