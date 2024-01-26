"""
Write circle_calc() function that takes radius of a circle as an input from user and 
then it calculates and returns area, circumference and diameter. You should get these 
values in your main program by calling circle_calc function and then print them
"""
import math
def circle_calc(radius):
    circle = {}
    circle["circumference"] = 2*radius*math.pi
    circle['diameter']= 2*radius
    circle['area']= math.pi*radius**2
    return circle

print(circle_calc(2.0))
    