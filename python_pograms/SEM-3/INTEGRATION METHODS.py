#INTEGRATION
#7th October,2021
'''
# INTEGRATION BY RECTANGULAR METHOD-
def f(x): return 3.0
b=float(input('enter upper limit'))
a=float(input('enter lower limit'))
sum=f(a)*(b-a)
print (sum)
#OUTPUT-
enter upper limit6
enter lower limit2
12.0
'''
#---------------------------------------------------
'''
# INTEGRATION BY TRAPIZOIDAL METHOD-
def f(x): return x**2
b=float(input('enter upper limit: '))
a=float(input('enter lower limit: '))
h=b-a
sum= 0.5*(f(a)+f(b))*h
print (sum)
#enter upper limit: 10
#enter lower limit: 2
#output: 416.0
'''
#---------------------------------------------------
#8th october,2021
'''
# INTEGRATION BY COMPOSITE TRAPIZOIDAL RULE-
def f(x): return x**2
b=float(input('enter upper limit: '))
a=float(input('enter lower limit: '))
n=int(input('enter no of division: '))
h=float((b-a))/n
sum=(f(b)+f(a))*0.5
for i in range (1,n):
    x=a+i*h
    sum=sum+f(x)

'''

#--------------------------------------
#13th November,2021
'''
#INTEGRATION BY SIMPSON METHOD-
def f(x): return x**2
b=float(input('enter upper limit: '))
a=float(input('enter lower limit: '))
h=float((b-a))/2
y0=f(a)
y1=f(0.5*(a+b))
y2=f(b)
sum= (h/3.0)*(y0+4*y1+y2)
print (sum)

#enter upper limit: 10
#enter lower limit: 2
#output:330.66666666666663
'''

#----------------------------------------
#24th November,2021
#SIMPSON COMPOSITE RULE
'''
def f(x): return x**2
b=float(input('enter upper limit: '))
a=float(input('enter lower limit: '))
n=int(input('enter number of division: '))
h=float((b-a))/n
sum1=f(a)+f(b)
sum2=0.0
for i in range (1,n,2):
    x=a+i*h
    sum2=sum2+f(x)
sum3=0.0
for j in range (2,n,2):
    x=a+j*h
    sum3=sum3+f(x)
I=(h/3.0)*(sum1+(4*sum2)+(2*sum3))
print(I)
'''
#-----------------------------------------
#8TH December,2021
#INTEGRATION BY USING SCIPY MODULE-1
#Caution: if you want to integrate upto nth value of x put (n+1) besides x= command.
'''
import numpy as np
from scipy import integrate
x=np.arange(0,3)
y=x**2
I=integrate.simps(y,x)
print (I)
'''
#------------------------------------------------------
#DECEMBER-15 &16 ,2021
#simpson by scipy
'''
from scipy.integrate import simps
import math
f=lambda x: math.sqrt(4-x**2)
I=simps(f,0,2,100)
print I
'''
'''
#by using Scipy & Numpy
from scipy import integrate
import numpy as np
x = np.arange(5,31,5)
y = [12, 22, 32, 42, 52, 62]
print(x)
print(y)
I = integrate.simps(y,x)
print(I)
'''
'''
#by summing method

x=[5.0,10.0,15.0,20.0,25.0,30.0]
y=[12.0,22.0,32.0,42.0,52.0,62.0]
s=0.0
for i in range(len(x)-1):
    a=((x[i+1]-x[i])*y[i])+0.5*(x[i+1]-x[i])*(y[i+1]-y[i])
    s=s+a
print (s)
#output:925.0
'''

'''
def f(x): return 3*x**2+2*x
print f(3.5)
'''
#verify by simpson
'''
from scipy.integrate import quad
import numpy as np
f=lambda x: x**2
I=quad(f,1,5)
print I
'''
#-----------------------------------------------------






    
