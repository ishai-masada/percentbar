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
	decimal = random.randrange(9) / 10
	integer = random.randrange(10)
	increment = decimal + integer
	leftover = 100 - percent
	if increment > leftover:
		increment = random.randrange(int(leftover * 10))
		percent += increment / 10
	percent += increment
	print(round(percent, 1), '%')
	time.sleep(1)
	clear()