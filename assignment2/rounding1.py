# to rounding a floating point number to integer by considering the floor & ceiling operation without using built in function.

x = float(input("Enter a float number : "))
value2 = int(x)

res = float(x - value2)

if res >= 0.5:
#    print(str(x) + " = " + str(x+1))
    print("Rounded Value: {}".format(value2 + 1))
else:
    print("Rounded Value: {}".format(value2))
