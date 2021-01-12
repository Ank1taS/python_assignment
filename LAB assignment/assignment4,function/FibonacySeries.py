''' to print nth term of fibonacy series using recursion
    file    : FibonacySeries.py
    date    : 07/10/2020
'''
import sys

# recursion function Rec_nth_Fibonacy
def rec_nth_Fibonacy(term):
    if term <= 0:
        print("Invalid term.")
        sys.exit()
    elif term == 1:
        return 0
    elif term == 2:
        return 1
    else:
        return rec_nth_Fibonacy(term - 1) + rec_nth_Fibonacy(term - 2)

term = int(input("enter a term = "))

print("{0}th fibonacy term is = ".format(term), end = '')
x = 1
y = 0
print("{0} ".format(rec_nth_Fibonacy(term)))
