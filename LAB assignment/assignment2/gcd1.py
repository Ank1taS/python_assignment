'''
    to find GCD of 2 numbers
    file    :   GCD1.py
    date    :   23/09/2020
'''

n1 = int(input("number 1 =  "))
n2 = int(input("number 2 =  "))

num1 = n1
num2 = n2

while True:
    rem = num1 % num2
    if rem:
        num1 = num2
        num2 = rem
    else:
        break

print("GCD of {0} and {1} = {2}".format(n1, n2, num2))