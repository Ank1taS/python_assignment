'''
    programe    :   to print pascal triangle while input is numbers of line
    file        :   PascalTriangle1.py
    date        :   30/09/2020
'''
# to calculate factorial
def factorial(n):
    fact = 1
    while n:
        fact *= n
        n -= 1
    # return factorial of the parameter
    return fact
    
# to take input of line number
while True:
    num = input("Enter line :  ")
    if num.isnumeric() == 0:
        print("{0} is a non numeric value.".format(num))
    else:
        num = int(num)
        break
    
# row operations
for row in range(0, num): 
    #print 3 space
    for sp in range(row, num): 
        print("   ", end = "")

    #print term of the row
    for pos in range (0, row + 1):
        print("%6d"%(factorial(row) / (factorial(pos) * factorial(row - pos))), end ="")
    print("\n")
        
