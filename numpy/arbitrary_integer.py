"""
Create a vector of length 5 filled with arbitrary integers from 0 to 10
"""

import numpy as np

arbitrary_numbers = np.random.randint(0,11,5)

print(arbitrary_numbers)

"""
Multiply the values ​​of two given vectors
"""

arbitrary_numbers2 = np.random.randint(0,11,5)
print(arbitrary_numbers2)

arbitrary_mul = arbitrary_numbers * arbitrary_numbers2

print(arbitrary_mul)


"""
Create a 3x3x3 array filled with arbitrary values
"""

arbitrary_numbers3d = np.random.random((3,3,3))

print(arbitrary_numbers3d)