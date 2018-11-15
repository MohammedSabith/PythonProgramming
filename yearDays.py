'''Write a test program that displays the number of days in the years from 2010 
to 2020.'''

def numDays(y):
	if((y%400==0) or (y%4==0 and y%100!=0)):
		return 366
	else:
		return 365


for i in range(2010,2021):
	print(i," -> ",numDays(i)) 