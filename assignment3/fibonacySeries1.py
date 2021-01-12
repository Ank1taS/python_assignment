''' to print fibonacy series up to nth term
    file    : fibonacySeries1.py
    date    : 19/09/2020
'''

num = int(input("enter a term = "))

print("\t\tFIBONACY SERIES Till {0}".format(num))

x = 1
y = 0

for i in range(1,num + 1):
    print(y)
    y = x - y
    x += y


