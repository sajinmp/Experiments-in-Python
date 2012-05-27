a=0
b=1
s=0
while (a+b < 4000000):
    c=a+b
    s += c
    a=b
    b=c
print s/2
