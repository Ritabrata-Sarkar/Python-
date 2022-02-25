#For reading the programme you need to know the series of cos
from math import pi,cos
x=float(input())
x=x*pi/180
t=1
s=1
for i in range(1,10,2):
    t=-1.0*t*x**2/(i*(i+1))
    s=s+t
print('The calculated value of cox(x)using python',s)
print('The value of cos(x) from library',cos(x))
