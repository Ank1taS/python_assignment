'''
    to print perfect numbers present in a range
    file    :   CheckPerfectNo1.py
    date    :   23/09/2020
'''

# to check the number as perfect 
def perfect(num):
    sum = 0

    for j in range(1, num):
        if num % j == 0:
            sum += j  
    #if a perfect number
    if sum == num:
        return True
    else:   # if not a perfect number
        return False

# to take 1st input
while True:
    n = input("Enter n :  ")
    if n.isnumeric() == 0:
        print("{0} is a nonnumwric value.".format(n))
    else:
        n = int(n)
        break
# to take second input
while True:
    m = input("Enter m :  ")
    if m.isnumeric() == 0:
        print("{0} is a nonnumwric value.".format(m))
    else:
        m = int(m)
        break

# to go through range
for num in range (n, m + 1):

    # to check the number as perfect 
    if perfect(num):
        print("{0} is a perfect number".format(num))

    