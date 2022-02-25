#Topic :Newton FORWARD Interpolation 
#26th September
#program-1
#continued at 1st 0ctober,2021
'''
x=[5.0,10.0,15.0,20.0,25.0,30.0]
y=[45.0,105.0,174.0,259.0,364.0,496.0]
d=[]
t=(18.0-x[0])/5.0
sum=y[0]
coef=t
k=1.0
for i in range (len(y),1,-1):
    for j in range(i-1):
        dif=y[j+1]-y[j]
        d.append(dif)
    sum=sum+coef*d[0]
    coef=((coef*(t-k))/(k+1))
    k=k+1
    y=d
    d=[]


print (sum)
#----------------------------------------------------------------------------
#5th October,2021
#NEWTON'S BACKWARD INTERPOLATION
x=[5.0,10.0,15.0,20.0,25.0,30.0]
y=[45.0,105.0,174.0,259.0,364.0,496.0]
d=[]
n=len(x)-1
t=(18.0-x[n])/5.0
sum=y[n]
coef=t
k=1.0
for i in range (len(y),1,-1):
    for j in range(i-1):
        dif=y[j+1]-y[j]
        d.append(dif)
    sum=sum+coef*d[j]
    coef=coef*(t+k)/(k+1)
    k=k+1
    y=d
    d=[]
print(sum)

'''















