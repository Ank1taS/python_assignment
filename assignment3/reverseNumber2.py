''' 
    to print thr reverse of a input number
    file    : reverseNumber1.py
    date    : 18/09/2020
'''

num = int(input("enter a number = "))
revNum = 0  # to store reverse number

if num > 0:
    temp = num
else:
    temp = num * (-1)


while temp != 0:
    rem = temp % 10
    revNum = (revNum * 10) + rem
    temp //= 10
if num > 0:
    print("reverse of input number {0} is = {1}".format(num, revNum))
else:
    print("reverse of input number {0} is = -{1}".format(num, revNum))
