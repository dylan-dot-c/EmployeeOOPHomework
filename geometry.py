# 
import math

def areaOfCircle(radius:float):
    """Function that takes in a radius as a parameted and returns the area of A circle with radius R of type float"""
    return math.pi * radius ** 2

def hypothenuse(side1:float, side2: float):
    """function that takes in 2 arguments, side1 and side2 of a triangle and returns the length of the hypothenuse."""
    squared = side1 ** 2 + side2 ** 2
    return math.sqrt(squared)