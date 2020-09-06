# to find the grade of a student according to the average mark
# file name : gradeCalculation1.py
# date  : 5/9/2020

sub1 = int(input("enter mark in subject-1 = "))
sub2 = int(input("enter mark in subject-2 = "))
sub3 = int(input("enter mark in subject-3 = "))
sub4 = int(input("enter mark in subject-4 = "))
sub5 = int(input("enter mark in subject-5 = "))

avg = ((sub1 + sub2 + sub3 + sub4 + sub5) / 5 )

if avg >= 90:
    print("grade - O")
elif (avg < 90) & (avg >= 80):
    print("grade - E")
elif (avg < 80) & (avg >= 70):
    print("grade - A")
elif (avg < 70) & (avg >= 60):
    print("Grade - B")
else:
    print("Grade - c")