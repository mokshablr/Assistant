import os
from datetime import datetime
def greet():
    timestr=datetime.now().strftime("%H:%M:%S")
    time= int(timestr[:2])
    if time>=6 and time<=12:
        print("Good Morning Arjun! The time is", timestr)
    elif time>12 or time <=6:
        print("Welcome back Arjun! The time is", timestr)

def currtime():
    timestr=datetime.now().strftime("%H:%M:%S")
    print("The time is",timestr)

def batt():
    import psutil
  
    # function returning time in hh:mm:ss
    def convertTime(seconds):
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return "%d:%02d:%02d" % (hours, minutes, seconds)
    
    # returns a tuple
    battery = psutil.sensors_battery()
    
    print("Battery percentage : ", battery.percent,'%')
    if battery.power_plugged==True:
        print("Power plugged in and Charging")
    else:
        print("On battery")
    # converting seconds to hh:mm:ss
    print("Battery left : ", convertTime(battery.secsleft))

def cal(str):
    l=str.split()
    if '+' in l:
        ind=l.index('+')
        r=float(l[ind-1]) + float(l[ind+1])
        print("The result is:",r)
    elif '-' in l:
        ind=l.index('-')
        r=float(l[ind-1]) - float(l[ind+1])
        print("The result is:",r)
    elif '*' in l:
        ind=l.index('*')
        r=float(l[ind-1]) * float(l[ind+1])
        print("The result is:",r)
    elif '/' in l:
        ind=l.index('/')
        r=float(l[ind-1]) / float(l[ind+1])
        print("The result is:",r)
    elif '^' in l or '**' in l:
        try:
            ind=l.index('^')
        except ValueError:
            ind=l.index('**')
        r=float(l[ind-1]) ** float(l[ind+1])
        print("The result is:",r)

greet()

while True:
    inp=input().lower()
    if inp=='time?' or inp=='time':
        currtime()
    elif inp=='thanks' or inp=='ty':
        print("No problem!")
    elif inp=='battery?' or inp=='battery' or inp=='bat':
        batt()
    elif inp=='calc' or inp=='calculate':
        s=input()
        cal(s)


    elif inp=='exit' or inp=='quit':
        print("Have a good day!")
        exit()