'''
    programe name   :   to find factorial of a number
    file            :   factorial.py
    date            :   19/10/2020
'''

# recursive function to find factorial
def rec_fact(num):
    if num == 0:
        return 1 
    else:
        return (num * rec_fact(num - 1))

# main()
while True:
    num = input("Enter a decimal integer = ")
    if isinstance(num, int) != 0:
        print("{0} is not a integer number ")
    else:
        num = int(num)
        break


if num < 0:
    print("Can not find factotoal of a negative number.")
else:
    fac = rec_fact(num)
    print("factorial of {0} is  - {1}".format(num, fac))
