''' 
    to check a number is palindrome number or not
    file : checkPalindrome1.py
    date : 19/09/2020
'''
import math

num = input("Enter a number : ")

n = int(num)

if n < 0:
    print("Negative numbers are not palindromic. ")
else:
    revNum = 0
    # reversing the inputed integer
    while n != 0:
        rem = n % 10
        revNum = (revNum * 10) + rem
        n //= 10

    if revNum == int(num):
        print("{0} is a palindrome number .".format(num))
    else:
        print("{0} is not a palindrome number .".format(num))
