'''
    to find the product of max 4 numbers by one function
    file name   :   Multiply.py
    date        :   07/10/2020
'''

def product(n1 = 1, n2 = 1, n3 = 1, n4 = 1):
    return n1 * n2 * n3 * n4

# multipling 2 numbers
print("{0} * {1} = {2} ".format(5, 10, product(5, 10)))

# multipling 3 numbers
print("{0} * {1} * {2} = {3} ".format(5, 10, 2, product(5, 10, 2)))

# multipling 4 numbers
print("{0} * {1} * {2} * {3} = {4} ".format(5, 10, 2, 5, product(5, 10, 2, 5)))