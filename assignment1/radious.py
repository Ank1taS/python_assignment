# programe to find the radious of a circle having same area as a rectangle
# file  : radious.py
# date  : 29/08/2020

import math

a = 5
b = 10
print("Sides of the rectangle are " + str(a) + str(b))
print("radious of thr circle whose area is same as the above rectangle is : " 
+ str(math.sqrt((a * b) / math.pi)))