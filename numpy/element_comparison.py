"""
1. Write a NumPy program to create an element-wise comparison (greater, greater_equal, less 
and less_equal) of two given arrays.

2. Write a NumPy program to create an element-wise comparison (equal, equal within a tolerance) of two given arrays.
"""
import numpy as np
array1 = np.array([1,2])
array2 = np.array([3,4,])

# solution 1
# check array1 is greater than array 2
print(np.greater(array1, array2))
# Check array1 is less than array2
print(np.less(array1, array2))
# Check Array1 is equal to array2
print(np.equal(array1, array2))
# Check Array1 is less than equal to array2
print(np.less_equal(array1, array2))
# Check Array1 is greater than equal to array2
print(np.greater_equal(array1, array2))

# solution2
#  equal within a tolerance
print(np.allclose(array1, array2))