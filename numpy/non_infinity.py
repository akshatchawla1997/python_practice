"""
Write a NumPy program to test a given array element-wise for finiteness (not infinity 
or not a number).
"""
import numpy as np

array1 = np.array([1,0,np.nan, np.inf])
print(array1)
print(np.isfinite(array1))

