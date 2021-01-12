'''
    to print the greater nmber using terinary operator
    file    :   TerinaryOp1.py
    date    :   18/09/2020  
'''
num1 = float(input("enter num1 ="))
num2 = float(input("enter num2 ="))

print("greater number is = ", end = '')
print(num1) if num1 > num2 else  print(num2)