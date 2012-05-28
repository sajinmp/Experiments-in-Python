""" This is a program to find the sum of even numbers of fibanocci series upto a limit of 4 million. 

You are free to edit modify or redistribute this program.

Author  :  Sajin M Prasad
Email   :  sajin_prasadkm@yahoo.co.in"""




a=0
b=1
s=0
while (a+b < 4000000):
    c=a+b
    if (c%2==0):
        s += c
    a=b
    b=c
print s
