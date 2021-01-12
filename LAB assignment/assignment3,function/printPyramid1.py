''' 
    programe    :   to print            0
                                    1       0
                                0       1       0
                            1       0       1       0
                        0       1       0       1       0   
                    and so on 
    file        :   printPyramid1.py
    date        :   3/10/2020
'''
# to print 1 and 0
def printItems(item, count):
    for i in range (0, count):
        print("{0} ".format(item), end = '')
        if item == 0:
            item = 1
        else:
            item = 0

# to take input of line number
while True:
    num = input("Enter line :  ")
    if num.isnumeric() == 0:
        print("{0} is a non numeric value.".format(num))
    else:
        num = int(num)
        break
    
# row operations
for row in range (1, num + 1): 
    #print 3 space
    for sp in range(row, num): 
        print(" ", end = "")

    if row % 2 == 0:
        printItems(1, row)
    else:
        printItems(0, row)

    print()


