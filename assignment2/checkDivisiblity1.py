# to check wheather number isdivisible by both 11 & 13 or by both 5 & 7 
# file name : checkDivisibility.py
# date  : 5/9/2020 

num =int(input("enter the number"))

if (not(num % 11)) and (not(num % 13)):
    print("{} is divisible by 11 and 13.".format(num))
else:
    print("{} is not divisible by 11 and 13.".format(num))


if (not(num % 5)) and (not(num % 7)):
        print("{} is divisible by 5 and 7.".format(num))
else:
    print("{} is not divisible by 5 and 7.".format(num))

