'''
    programe name   :   to find the reverse of integer using recursion
    file name       :   reverse1.py
    date            :   7/10/2020
'''
# recursive reverse() to return reverse of the number
def reverse(num):
    global rev
    global pos
    if num > 0:
        reverse((int)(num // 10))
   #     reverse(num // 10)
        rev += (num % 10) * pos 
        pos *= 10

    return rev

rev = 0
pos = 1

# main()
while True:
    num = input("Enter a decimal integer = ")
    if isinstance(num, int) != 0:
        print("{0} is not a integer number ")
    else:
        num = int(num)
        break
if num > 0:
    print("reverse of {0} is {1}".format(num, reverse(num)))
else:
    num *= -1
    print("reverse of {0} is -{1}".format(num, reverse(num)))
