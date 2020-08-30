# programe to convert seconds to hour minute and second
# file  : timeconvertion.py
# date  : 29/08/2020

time = 9015
sec = time
hour = sec // 3600
sec %= 3600
minute = sec // 60
sec = sec % 60

print(str(time) + "secs  =  " + str(hour) + "h " + str(minute) + "min " + str(sec) +"sec ")