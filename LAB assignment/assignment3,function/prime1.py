'''
    programe    :   to print 1st n prime numbers
    file        :   prime1.py
    date        :   3/10/2020
'''
def CheckPrime(num):
    count = 0

    for i in range (2, num):
        if(num % i == 0):
            count = 1
            break
    
    if count == 0:
        return True
    else:
        return False


# to accept input n
while True:
    n = input("enter n  =  ")
    if n.isnumeric() == 0:
        print("{0} is a non-numeric value ".format(n))
    else:
        n = int(n)
        break

# number varriable to store each number to check prime
num = 2
# count varriable to count numbers of prime numbers
count = 0

print("First {0} prime numbers are - ".format(n))
#infinite loop to travel each numbers
while True:
    if CheckPrime(num):
        print("{0},  ".format(num), end = "")
        count += 1
        if count == n:
            break
    num += 1 # to increase num to check next integer
