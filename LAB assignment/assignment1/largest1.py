'''
    to find the largest among the 3 numbers
    file    :   Largest1.py
    date    :   19/09/2020
'''

num1 = float(input("enter number =  "))
num2 = float(input("enter number =  "))
num3 = float(input("enter number =  "))

print("largest number = ", end = '')
print (num1) if num1 > num2 and num1 > num3 else (print (num2) if num2 > num3 else print(num3))