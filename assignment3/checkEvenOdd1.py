'''
    to check  input numbers are even or odd
    file    :   checkEvenOdd1.py
    date    :   20/09/2020
'''

countEven = 0
countOdd = 0

for i in range (0,10):
    x = int(input("enter a integer number  = "))

    if x % 2:
        countOdd += 1
    else:
        countEven += 1

print("out of 10 inputs {0} are even numbers and {1} are odd numbers .".format(countEven, countOdd))
