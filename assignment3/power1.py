'''
    to find the power of x to y
    file    :   power1.py
    date    :   20/09/2020
'''

x = int(input("x = "))
y = int(input("y = "))
result = 1.0

if y >= 0:
    for i in range(y):
        result *= x
 #   print(result)
    if x < 0 and result > 0:
        result *= -1

else:
    for i in range(0, y, -1):
        result *= 1/x

        if x < 0 and result > 0:
            result *= -1

print("{0} ^ {1} = {2}".format(x, y, result))
