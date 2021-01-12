'''
    to print digits of a number in word
    file    : wordDigit1.py
    date    : 19/09/2020
'''

num = (input("enter a number  ="))
n = int(num)

#wheather inputed integer is positive or not
if n < 0:
    length = len(num) - 1
    n = n * (-1)
else:
    length = len(num)


print("  {0} in words  ".format(num))

for i in range (1, length + 1):
    # extracting digit
    digit = n // pow(10, length - i)

    # printing digit in word
    if digit == 0:
        print("ZERO  ", end = "")
    elif digit == 1:
        print("ONE  ", end = "")
    elif digit == 2:
        print("TWO  ", end = "")
    elif digit == 3:
        print("THREE  ", end = "")
    elif digit == 4:
        print("FOUR  ", end = "")
    elif digit == 5:
        print("FIVE  ", end = "")
    elif digit == 6:
        print("SIX  ", end = "")
    elif digit == 7:
        print("SEVEN  ", end = "")
    elif digit == 8:
        print("EIGHT  ", end = "")
    elif digit == 9:
        print("NINE  ", end = "")

    #updating number
    n = n % pow(10, length - i)