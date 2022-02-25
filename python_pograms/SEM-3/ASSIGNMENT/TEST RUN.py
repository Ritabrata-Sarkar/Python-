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
