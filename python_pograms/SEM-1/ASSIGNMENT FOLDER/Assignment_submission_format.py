'''
Name: Ritabrata Sarkar
Roll: xxxxxxxxxx
reg: xxxxxxxxxxx
Question:
ABCDEFGHIJKLMNOPQRSTUVWXYZ
'''
x=float(input('enter your input x'))
s=1
t=(1.0/x**3)
s=s+t
for i in range(1,40):
    t=t/x**2
    if t<0.001:
        break
    s=s+t
print ('Sum of the series is',s)
print ('number of total term',i+2)

'''
>>> 
enter your input x2
Sum of the series is 1.166015625
number of total term 6
>>> 
'''
