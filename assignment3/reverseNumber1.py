''' 
    to print thr reverse of a input number
    file    : reverseNumber1.py
    date    : 18/09/2020
'''

num = int(input("enter a number = "))
revNum = 0  # to store reverse number
temp = num

while temp != 0:
    rem = temp % 10
    revNum = (revNum * 10) + rem
    temp //= 10

print("reverse of input number {0} is = {1}".format(num, revNum))
