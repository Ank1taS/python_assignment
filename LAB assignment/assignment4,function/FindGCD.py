'''
    to find GCD of 2 numbers
    file    :   GCD1.py
    date    :   07/10/2020
'''
def gcd(num1, num2):
    while True:
        rem = num1 % num2
        if rem:
            num1 = num2
            num2 = rem
        else:
            return num2

n1 = int(input("number 1 =  "))
n2 = int(input("number 2 =  "))

print("GCD of {0} and {1} = {2}".format(n1, n2, gcd(n1, n2))) 