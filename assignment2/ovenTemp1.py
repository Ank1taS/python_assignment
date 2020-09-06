# to set temperature of the oven based on the
#reading from a pressure meter. The rules are:
#a. If reading = 2 or 3 : temperature should be set to 500 degrees.
#b. If reading = 4: temperature should be set to 600 degrees.
#c. If reading = 5 or 6 or 7: temperature should be set to 700 degrees
#d. For any other reading, the default temperature setting is 300 degrees.
# file name : ovenTemp1.py


reading = float(input("Enter the reading =  "))

if (reading == 2) or (reading == 3):
    temp = 500
elif (reading == 4):
    temp = 600
elif (reading == 5) or (reading == 6) or (reading == 7):
    temp = 700
else:
    temp = 300

print("Temperature of oven is set to {}".format(temp))