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