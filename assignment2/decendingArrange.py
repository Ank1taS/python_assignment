# arrange 3 numbers in descending order.

num1 = int(input ("enter a number "))
num2 = int(input ("enter a number "))
num3 = int(input ("enter a number "))

if (num1 > num2):
    if (num1 > num3):
        max = num1
        if (num2 > num3):
            mid, min = num2, num3
        else:
            mid, min = num3,num2
    else:
        max, mid, min = num3, num1, num2
elif (num2 > num3):
    max = num2
    if(num1 > num3):
        mid, min = num1, num3
    else:
        mid, min = num3, num1
else:
    max, mid, min = num3, num2, num1

print("in decending order :" + str(max) + ", " + str(mid) + ", " + str(min))