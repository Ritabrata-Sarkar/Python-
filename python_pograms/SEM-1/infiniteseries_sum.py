'''
s=1
x=float(input())
for i in range(1,40):
    t=1.0/x**(2*i+1)
    if t<0.001:
        break
    s=s+t
print (s)
print (i)

'''
'''
x=float(input())
s=1
t=1/x**3
s=s+t
for i in range(40):
    t=t/x**2
    if t<0.001:
        break
    s=s+t
print(s)
print(i)
'''
x=float(input())
s=1
t=1/x**3
s=s+t
for i in range(1,40):
    t=t/x**2
    if t<0.001:
        break
    s=s+t
print(s)
print(i)









    
