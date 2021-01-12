'''
    programe name   :   to compute sine series
    file name       :   sineSeries1.py
    date            :   3/10/2020
'''

import math

def sinSeries(num, n):
    sum = 0
    odd = 1
    sign = 1

    for i in range(1, n + 1):
        fact = 1
        temp = odd

        while temp != 0:
            fact *= temp
            temp -= 1

        sum = sum + (math.pow(num, odd) / fact) * sign
        sign *= -1
        odd += 2

    return sum

degree = float(input("enter the angle in degree: "))
term = int(input("Enter the term: "))

print("The sum of sine series of {} term of the value {} = {:.3f}".format(term, degree, sinSeries(degree, term)))
