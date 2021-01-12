''' 
    to print different types inputs in positional parameter format
    file name : Ass2.py
    date      : 16/09/2020
'''

a = int(input("Enter a integer for a = "))
b = float(input("Enter a float for b = "))
c = bool(input("enter a boolian value for c = "))
d = input("Enter a string for d = ")

# print  using positional parameter method
print()
print("a = {0} , {1}".format(a, type(a))) 
print("b = {0} , {1}".format(b, type(b))) 
print("c = {0} , {1}".format(c, type(c))) 
print("d = {0} , {1}".format(d, type(d))) 
