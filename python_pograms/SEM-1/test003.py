from math import sqrt
a=[]
n=input('Enter total number of elements')
for i in range(int(n)):
    a.append(input())
print ('list before interchange', a)
a[0],a[-2]=a[-2],a[0]
print ('list after interchange', a)
b=[sqrt(float(j)) for j in a]
print ('list b=', b)
