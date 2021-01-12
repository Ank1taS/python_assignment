''' 
    to check a number wheather amstong or not enter digit must be 3 digit number
    file name  : checkAmstong1.py
    date       : 18/09/2020
'''

n = input("enter a number = ")
num = int(n) 

if num <= 0:
    print("{0} is not a natural number .".format(num))

elif len(n) > 3:
    print("number must contain less than 4 digits.")

else:
    #to check amstong or not
    temp = num
    sum = 0     # initialising to 0
    while(temp != 0):
        rem = temp % 10
        sum += rem ** 3
        temp //= 10
    print(sum)
    if sum == num:
        print("{0} is an amstrong number.".format(num))
    else:
        print("{0} is not an amstrong number.".format(num))



