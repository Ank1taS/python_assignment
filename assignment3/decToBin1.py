'''
    to convert a decimal number to binary
    file    :   decToBin1.py
    date    :   20/09/2020
'''

decNum = int(input("enter a number =  "))
print("{0} in binary = ".format(decNum), end = " ")
binNum = 0
place = 1

while decNum != 0:
    rem = decNum % 2
    binNum += rem * place
    place *= 10
    decNum //= 2

print(binNum)
