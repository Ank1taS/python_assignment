'''
    to find the digital roots of a integer number
         (ittirate sum of digits of number until reduced to a single digit)
    file    :   DigitalRoots1.py
    date    :   23/09/2020
'''

while True:   
    num = input("Number =  ")
    if num.isnumeric() == 0:
        print("{0} is non numeric.".format(num))
    else:
        num = int(num)
        break
number = num

while True:
    sum = 0

    while num != 0:     # to finf the sum of digits
        sum += num % 10
        num //= 10


    # to check if digital root
    if sum > 9:
        num = sum
    else:
        break
  
print("Digital roots of {0} is = {1}".format(number,sum))