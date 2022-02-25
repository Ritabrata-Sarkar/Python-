from math import sqrt
A=[-3,7,4,2]
M=0.0
for j in range(3):
    t=A[j]*A[j]
    M=M+t
n=sqrt(M)
print('The Norm of the matrix =',n)
Ahat=[-j/n for j in A]

print('The components of the unit vector is given below')
for r in Ahat:
    print(r)
