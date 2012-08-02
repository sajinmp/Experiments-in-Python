""" THis is a program to find the sum of numbers divisible by 3 or 5 upto the limit 1000.
You are free to edit modify or redistribute this program. 

Author : Sajin M Prasad
Email  : sajin_prasadkm@yahoo.co.in
"""

sum=0
for i in range(1,1000):
	if (i%3==0 or i%5==0):
		sum=sum+i
print sum
