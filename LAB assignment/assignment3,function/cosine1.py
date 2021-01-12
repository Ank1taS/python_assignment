'''
    programe name   :   to compute cosine series
    file name       :   cosine1.py
    date            :   3/10/2020
'''

import math

def cosinSeries(num, n):
    sum = 1
    even = 2
    sign = -1

    for i in range(1, n + 1):
        fact = 1
        temp = even

        while temp != 0:
            fact *= temp
            temp -= 1

        sum += (math.pow(num, even) / fact) * sign
        sign *= -1
        even += 2

    return sum

degree = float(input("enter the value in degree : "))
term = int(input("Enter the term: "))

print("The sum of sine series of {} term of the value {} = {:.3f}".format(term, degree, cosinSeries(degree, term)))
