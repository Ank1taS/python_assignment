'''
    to check a number perfect square or not
    file    :   perfectSquare1.py
    date    :   23/09/2020
'''

import math

num = int(input("Enter a number = "))

if num < 0:
    print("negative numbers do not have real square roots.\nit is impossible for a negative value to be a perfect square!")
else:
    squareRoot = math.sqrt(num)
    # to store integer part of squareRoot
    intSRoot = int(squareRoot)  # math.floor() can also be used

    if squareRoot - intSRoot:
        print("{0} is not a perfect square.".format(num))
    else:
        print("{0} is a perfect square.".format(num))