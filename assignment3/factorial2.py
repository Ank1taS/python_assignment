'''
    to find the factorial of a input number
    file name   : factorial1.py
    date        : 18/09/2020
'''

num = int(input("enter a number  =  "))

#checking conditions
if num < 0:
    print("can not find factorial of a negative number.")
else:    
    # factorial calculation
    temp = num
    fac = 1
    while num != 0:
        fac *= num
#        --num          python dont have any increment decrement operator
        num -= 1
        
    print("factorial of {0} is {1} ".format(temp,fac))
