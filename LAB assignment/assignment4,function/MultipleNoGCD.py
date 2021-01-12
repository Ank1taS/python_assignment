'''
    programe name   :   to find gcd of arbitary numbers of arguments [while loop for input] 
    file name       :   MultipleNoGCD.py
    created by      :   ankita sahoo
    date            :
'''

# computing recursive gncd function 
def ngcd(num1, num2):
    if num1 == num2:
        return num1
    elif num1 > num2:
            return ngcd(num1 - num2, num2)
    else:
            return ngcd(num1, num2 - num1)

# main()
num = int(input("Enter number = "))
gcdValue = num
choice = "Y"

while True:
    num = int(input("Enter number = "))
    gcdValue = ngcd(gcdValue, num)
    choice = input("Do you want to continue? [Y/N] :  ")
    if choice == "N" or choice == "n":
        break
    elif choice == "Y" or choice == "y":
        continue
    else:
        print("Undefined choice.\nprograme ends...")
        break

print("GCD = ", gcdValue)
