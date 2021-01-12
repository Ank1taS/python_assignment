'''
    to print multiplication table for a number
    file    :   multiplicationTable1.py
    date    :   20/09/2020
'''

num = int(input("enter a term =  "))
print("       ", end = "")
for i in range (1, 11):
    print("%-4d" %i, end ="")
print()
for i in range (1, 11):
    print("=======", end ="")
for i in range (1, num + 1):
    print("\n   ||\n %-2d||  " %i, end = "")
    for j in range(1, 11):
        print("%-4d" % (i * j), end ="")


