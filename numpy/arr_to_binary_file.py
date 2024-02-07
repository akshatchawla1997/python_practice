"""
Write a NumPy program to save a given array to a binary file.
"""

import numpy as np
import os
array = np.array([[1,2,3,4],[5,6,7,8]])

np.save('temp_array.npy', array)

if os.path.exists("temp_array.npy"):
    arrya1 = np.load("temp_array.npy")
    print(np.array_equal(array, arrya1))