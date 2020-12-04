
import os 
import random 
import time


def clear():
    os.system('clear')

percent = 0
clear()	
print(percent, '%')
time.sleep(1)
while percent < 100:
    clear()
    increment = random.randrange(109) / 10
    leftover = 100 - percent
    if increment > leftover:
        increment = random.randrange(int(leftover * 10)) / 10
        percent += increment
    percent += increment
    print(round(min(percent, 100), 1), '%')
    time.sleep(1)
    clear()
