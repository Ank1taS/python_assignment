# to eveluate x = (a - b) / (c - d). Give a suitable error message if denominator is zero.
# file name : expressionEvaluation1.py
# date      : 5/9/20

a = int(input("x = (a - b) / (c - d) \n\nenter a =  "))
b = int(input("enter b =  "))
c = int(input("enter c =  "))
d = int(input("enter d =  "))

if(c - d):
    print("x = " + str((a - b) / (c - d)))
else:
    print("ZeroDivisionError: division by zero")