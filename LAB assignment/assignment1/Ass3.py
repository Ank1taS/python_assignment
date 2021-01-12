''' 
    to print different types inputs in format specification method
    file name : Ass3.py
    date      : 16/09/2020
'''

a = int(input("Enter a integer for a = "))
b = float(input("Enter a float for b = "))
c = bool(input("enter a boolian value for c = "))
d = input("Enter a string for d = ")

# print  using posiyional parameter method
print()
print("a = %d , %s"%(a , type(a)))
print("b = %d , %s"%(b , type(b))) 
print("c = %s , %s"%(c , type(c))) 
print("d = %s , %s"%(d , type(d)))
