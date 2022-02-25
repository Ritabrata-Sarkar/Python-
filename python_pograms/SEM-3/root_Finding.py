# there are 2 ways to find the root of a given no. : Bisection method & Newton Raphason Method.
#----------------------------------------------------------------------------------------------------
#12th September,2021
#here we just use the theory to find the root by graph plotting calculation.

#program-1

'''
def f(x): return x**2-4.0  # defining a function.
x=0.0
t=0.0001

while f(x)<0.0001: # it will run untill it crosses the 0.0001
    x=x+t
print (x-t)

'''
'''
#program-2

def f(x): return x**2-96.0  # defining a function.
x=0.0
t=0.0001

while f(x)<0.0001: # it will run untill it crosses the 0.0001
    x=x+t
    print ((x),f(x))
'''
#--------------------------------------------------------------------------------------------------
#19th September
# Bisection Method
#program-1
'''
import sys
def f(x): return x**2-4.0

a=float(input("enter first guess value"))
b=float(input("enter second guess value"))
if f(a)*f(b)>0:
    print ("No root is Available within the range")
    sys.exit()
while abs (a-b)>=0.001:
    xm=(a+b)*0.5
    if f(xm)==0:
        print ("the root is",xm)
        sys.exit()
    if f(a)*f(xm)<0:
        b=xm
    else:
        a=xm
print("The root is=",(a+b)*0.5)
'''

#-----------------------------------------------------------------------------------------------------
#Newton Rhapson Method
#Program-2

'''

import sys
def f(x):return x**2-4.0
def h(x):return 2*x
x=float(input("enter the value of approximate root"))
if f(x)==0:
    print ("root is==",x)
    sys.exit
while f(x)>0.0001:
    x=x-f(x)/h(x)
print ("The root is==",x)

'''
#-----------------------------------------------------------------------------------




