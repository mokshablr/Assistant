import os
from datetime import datetime
def greet():
    time= int(datetime.now().strftime("%H"))
    timestr=datetime.now().strftime("%H:%M:%S")
    if time>=6 and time<=12:
        print("Good Morning Arjun! The time is", timestr)
    elif time>12 or time <=6:
        print("Welcome back Arjun! The time is", timestr)

def currtime():
    timestr=datetime.now().strftime("%H:%M:%S")
    print("The time is",timestr)

greet()
while True:
    inp=input().lower()
    if inp=='time?' or inp=='time':
        currtime()
    elif inp=='thanks' or inp=='ty':
        print("No problem!")
    elif inp=='exit' or inp=='quit':
        exit()