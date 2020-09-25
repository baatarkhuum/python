import os
import time 

second,minute,hours=0,0,0

while(True):
    print(hours,':',minute,':',second)
    time.sleep(1)
    second+=1
    if second ==60:
        second=0
        minute+=1
    if minute ==60:
        hours+=1
        minute=0
    if minute==1:
        print("time is over")
        break
    os.system('cls')