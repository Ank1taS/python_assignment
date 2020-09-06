# to check whether a given year is leap year or not.
# file name : leapYear1.py
# date      : 5/9/20

year = int(input("enter a year = "))


if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("{ 0 } is a leap year".format(year))
        
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
