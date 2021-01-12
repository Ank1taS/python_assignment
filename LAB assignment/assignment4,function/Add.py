'''
    to find the sum of max 5 numbers by one function
    file name   :   Add.py
    date        :   07/10/2020
'''

def sum(n1 = 0, n2 = 0, n3 = 0, n4 = 0, n5 = 0):
    return n1 + n2 + n3 + n4 + n5

# sum of 2 numbers
print("{0} + {1} = {2} ".format(5, 10, sum(5, 10)))

# sum of 3 numbers
print("{0} + {1} + {2} = {3} ".format(5, 10, 10, sum(5, 10, 10)))

# sum of 4 numbers
print("{0} + {1} + {2} + {3} = {4} ".format(5, 10, 10, 5, sum(5, 10, 10, 5)))

# sum of 5 numbers
print("{0} + {1} + {2} + {3} + {4} = {5} ".format(5, 10, 10, 5, 10, sum(5, 10, 10, 5, 10)))
