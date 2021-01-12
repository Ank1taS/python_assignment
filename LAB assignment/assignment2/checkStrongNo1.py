'''
    to check a number is stong number or not
    file  : CheckStongNo1.py
    date  : 23/09/2020
'''

num = int(input("number =  "))
sum = 0
n = num

while n :
    factorial = 1
    rem = n % 10
    for i in range (1, rem + 1):
        factorial *= i

    sum += factorial
    n //= 10
if num == sum:
    print("{} is a strong number...".format(num))
else:
    print("{} is not a strong number...".format(num))
