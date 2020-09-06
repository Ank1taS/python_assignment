# programe to convert seconds to hour minute and second
# file  : timeconvertion1.py
# date  : 05/09/2020

time = int(input("enter time in seconds = "))

if time == 0:
    print("second should not be 0.")
else:
    sec = time
    hour = sec // 3600
    sec %= 3600
    minute = sec // 60
    sec = sec % 60

    print(str(time) + "secs  =  " + str(hour) + "Hr:" + str(minute) + "Min:" + str(sec) +"Sec. ") 