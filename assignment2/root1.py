# programe to find the roots of a quadratic equation
# file  : root1.py
# date  : 06/09/2020

import math

a = int(input("Equation is ax^2 + bx + c = 0\nenter a = "))
b = int(input("enter b = "))
c = int(input("enter c = "))

print("equation is = " + str(a) + "X^2 + " + str(b) +"X + " + str(c))
print()

if(a == 0):
    if(a == 0 and b == 0):
        print("Equation has no solution\n")
    else:
        print("Equation has one solution")
else:
    d = (b * b) - 4 * a * c
    if(d == 0):
        print("\n the above equation have only one root .\n it is = "
        + str((-b /(2 * a))))

    elif(d > 0):
        print("\n the above equation have 2 roots.\n they are , X1 = "
        +str((-b + math.sqrt(d)) / (2 * a)) + " and  X2 = " + str((-b - math.sqrt(d)) / (2 * a)))

    else:
        print("\n the above equation have imaginary roots")


