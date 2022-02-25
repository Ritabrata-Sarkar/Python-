from math import pi,sin
x=float(input())
x=x*pi/180
s=x
t=x
for i in range(2,21,2):
	t=-1.0*t*x**2/(i*(i+1))
	s=s+t
print('calculated value of sin() using python',s)
print('value of sin()using library',sin(x))
