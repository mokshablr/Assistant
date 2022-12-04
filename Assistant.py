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

def spotify(): #plays spotify when it is the next window
    import pyautogui as pa
    import os
    import time
    os.system('spotify')
    time.sleep(2)
    pa.press('space')
    pa.hotkey('alt','tab')

    while True:
        spot_inp=input('>> ')
        if spot_inp=='next' or inp=='skip':
            pa.hotkey('alt','tab')
            pa.hotkey('ctrl','right')
            pa.hotkey('alt','tab')
        elif spot_inp=='prev':
            pa.hotkey('alt','tab')
            pa.hotkey('ctrl', 'left')
            pa.hotkey('alt','tab')
        elif spot_inp=='shuffle' or spot_inp=='mix':
            pa.hotkey('alt','tab')
            pa.hotkey('ctrl', 's')
            pa.hotkey('alt','tab')
        elif spot_inp=='main' or spot_inp=='exit':
            break
    

def files():
    def num_files():
        ctr=0
        di=input('Enter directory path: ')
        num_inp=input('Which file-type would you like to count?\n>>> ').lower()

        if num_inp=='all':
            for filename in os.listdir(di):
                f= os.path.join(di,filename)
                if os.path.isfile(f):
                    ctr+=1
            print("Number of files:",ctr)
        else:
            for filename in os.listdir(di):
                f= os.path.join(di,filename)
                if os.path.isfile(f):
                    if f.endswith(num_inp):
                        ctr+=1
            print(f"Number of {num_inp} files:",ctr)
    
    while True:
        files_inp= input('>> ').lower()
        if files_inp== 'num' or files_inp=='count':
            num_files()
        elif files_inp=='exit' or files_inp=='main':
            break
        else:
            print('Unrecognised command. Try again...')


greet()

operands=['+', '-', '*', '/', '^', '**']

while True:
    inp=input('> ').lower()

    if inp=='time?' or inp=='time':
        currtime()
    elif inp=='thanks' or inp=='ty':
        print("No problem!")
    elif inp=='battery?' or inp=='battery' or inp=='bat':#battery status
        batt()
    elif any(op in inp for op in operands):#checks for operands in inp
        cal(inp)
    elif inp=='check files' or inp=='files':
        files()
    elif inp=='music':
        spotify()

    elif inp=='exit' or inp=='quit':
        print("Have a good day!")
        exit()
    else:
        print('Unrecognised command. Try again...')