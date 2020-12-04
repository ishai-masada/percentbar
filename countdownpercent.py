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
	#decimal = random.randrange(9)/10
	integer = random.randrange(10)
	#increment = decimal + integer
	leftover = 100 - percent
	if integer > leftover:
		integer = random.randrange(leftover)
	percent += integer 
	print(percent, '%')
	time.sleep(1)
	clear()