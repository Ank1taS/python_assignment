# programe to find of a triangle using 3 sides
# file  : trianglearea.py
# date  : 29/08/2020

import math

# taking input
a = 240
b = 340
c = 500

s = (a + b + c) // 2

print("Area of the triangle is : " + str(math.sqrt( s * (s - a) * (s - b) * (s - c))))

