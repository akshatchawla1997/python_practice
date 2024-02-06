"""
 Write a NumPy program to create a vector of length 10 with values evenly distributed between 5 and 50.
"""

import numpy as np

vector1 = np.linspace(5,50,10)

print(vector1)

"""
Vector Dot Product 
In mathematics, the dot product or scalar product is an algebraic operation that takes two equal-length 
sequences of numbers and returns a single number. 
For this we will use dot method.
"""

vector2 = np.linspace(10,100,10)

dotproduct = vector1.dot(vector2)

print(f"dot product of 2 vectors are {dotproduct}")

"""
Vector-Scalar Multiplication 
Multiplying a vector by a scalar is called scalar multiplication. To perform scalar multiplication, 
we need to multiply the scalar by each component of the vector.
"""

scalar_multiplication = vector1 * vector2

print(f"scalar multiplication of 2 vectors are {scalar_multiplication}")