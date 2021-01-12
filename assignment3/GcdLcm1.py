'''
    to find the lcm and gcd of 2 number
    file    :   GcdLcm1.py
    date    :   20/09/2020
'''

n1 = int(input("enter 1st number "))
n2 = int(input("enter 2nd number "))
mul = n1 * n2   
rem = 0

while True:
    rem = n1 % n2
    if rem:   
        n1 = n2
        n2 = rem
    else:
        break

print("GCD = {}".format(n2))
print("LCM = {}".format(mul // n2))