# programe to swap 2 numbers without 3rd varriable
# file  : swap1.py
# date  : 29/08/2020

import math

a = 1
b = 4
c = 4

print("equation is = " + str(a) + "X^2 + " + str(b) +"X + " + str(c) )

d = (b * b) - 4 * a * c
if(d == 0) :
    print("\n the above equation have only one root .\n it is = "
    + str((-b /(2 * a))))

elif(d > 0):
    print("\n the above equation have 2 roots.\n they are , X1 = "
    +str((-b + math.sqrt(d)) / (2 * a)) + " and  X2 = " + str((-b - math.sqrt(d)) / (2 * a)))

else:
    print("\n the above equation have imaginary roots")


