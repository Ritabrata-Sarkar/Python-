#22nd December,2021
#Euler's Method
'''
def f(x,y):return 3*x*y
x=0.0
y=1
h=0.003
for i in range(1001):
    y=y+h*f(x,y)
    x=x+h
    print(y)
    
'''
#------------------------------------------------
#Runge-Kutta-2nd order(RK2)
'''
def f(x,y):return 3*x*y
x=0.0
y=1.0
h=0.0002
for i in range(10001):
    k1=h*f(x,y)
    k2=h*f(x+h,y+k1)
    y=y+0.5*(k1+k2)
    x=x+h
    print(y)
'''
#----------------------------------------------

#pogram-2
'''

import matplotlib.pyplot as plt
import numpy as np
import math

d=np.linspace(0,2.01,201)
d3=np.exp(1.5*d**2)
d1=[]
d2=[]
d4=[]


#Euler Method
def f(x,y): return 3*x2*y2
x2=0.0
y2=1.0
h=0.01
for i in range (201):
	y2=y2+h*f(x2,y2)
	x2=x2+h
	d4.append(y2)
print (y2)


#Rk 2 Method 
def f(x,y): return 3*x*y
x=0.0
y=1.0
h=0.01
for i in range (201):
	k1=h*f(x,y)
	k2=h*f(x+h,y+k1)
	y=y+0.5*(k1+k2)
	x=x+h
	d1.append(y)
print (y)


#RK-4 Method
def f(x1,y1): return 3*x1*y1
x1=0.0
y1=1.0
h=0.01
for i in range (201):
	k11=h*f(x1,y1)
	k22=h*f(x1+h/2.0,y1+k11/2.0)
	k3=h*f(x1+h/2.0,y1+k22/2.0)
	k4=h*f(x1+h,y1+k3)
	y1=y1+(1/6.0)*(k11+2*k22+2*k3+k4)
	x1=x1+h
	d2.append(y1)
print (y1)


plt.plot(d,d1,'*',label='RK2')
plt.plot(d,d2,'+',label='RK4')
plt.plot(d,d3,label='EXACT') 
plt.plot(d,d4,'.',label='EULER')
plt. legend(fontsize=10) 
plt.show()
'''
