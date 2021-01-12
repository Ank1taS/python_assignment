''' 
    to find the sum of digits of a number
    file : digitSum1.py
    date : 19/09/2020
'''

num = int(input("Enter a number = "))

print("Sum of digit(s) of {0} is ".format(num), end = " ")

if num < 0:
    num *= -1

sum = 0
while num != 0:
 #   rem = num % 10
    sum += num % 10
    num //= 10

print(sum)