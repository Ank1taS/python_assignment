'''
    to check a number wheather prime or not
    file name   : checkPrime1.py
    date        : 19/09/2020
'''
import sys
num = int(input("enter a number  =  "))

count = 0

if num > 1:
    for i in range (2, num):
        if (num % i) == 0:
            count += 1
else:
    print("{0} is not a natural number.".format(num))
    sys.exit()

if count == 0:
    print("{0} is a prime number.".format(num))
else:
    print("{0} is not a prime number.".format(num))
