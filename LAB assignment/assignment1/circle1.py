'''
    to find area and perimeter of circle while input is diameter
    file    :   Circle1.py
    date    :   19/09/2020
'''

diameter = float(input("Enter diameter =  "))
radious = diameter / 2

print("Perimeter of circle of radious %f is = %.3f "%(radious, 2 * 3.1415 * radious))
print("area of circle of radious %f is = %.3f "%(radious, 3.1415 * (radious ** 2)))
