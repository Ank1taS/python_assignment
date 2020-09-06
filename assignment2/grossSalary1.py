# to calculate thr gross salary

basic = float(input("Enter the besic salary :  "))

DA = basic * 0.6
HRA = basic * 0.15
conveyance = basic * 0.15
medical = basic * 0.1

grossSalary = basic + DA + HRA + conveyance + medical

print("Gross salary is = {}".format(grossSalary))
