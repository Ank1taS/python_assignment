'''
    to find the prime factors of a number
    file    :   primeFactor1.py
    date    :   20/09/2020
'''

num = int(input("number =  "))

check = False # to check the factor is prime or not

for count in range (2, num): # to divide num by each number < num 
    if (num % count == 0):   # to check it is a factor of num
        check = True
        for i in range(2, count):   # to check the factor is prime or not
            if (count % i == 0): # if count is not a prime number
                check = False
                break
        if check == True:
            print(count)  