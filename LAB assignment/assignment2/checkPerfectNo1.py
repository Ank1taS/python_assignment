'''
    to check a number perfect number or not
    file    :   CheckPerfectNo1.py
    date    :   23/09/2020
'''

while True:
    num = input("Enter number :  ")
    if num.isnumeric() == 0:
        print("{0} is a nonnumwric value.".format(num))
    else:
        num = int(num)
        break

sum = 0

for i in range (1, num):
    if num % i == 0:
        sum += i   
if sum == num:
    print("{0} is a perfect number".format(sum))
else:
    print("{0} is not a perfect number".format(num))
    