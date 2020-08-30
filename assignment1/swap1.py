# programe to swap 2 numbers without 3rd varriable
# file  : swap1.py
# date  : 29/08/2020

a = 10
b = 20
print("Before swaping  a = " + str(a) + " b = " + str(b))

a = a + b 
b = a - b
a = a - b
print("\nAfter swaping  a = " + str(a) + " b = " + str(b))
