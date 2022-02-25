A=[[1,9,4],[2,3,-8],[14,-11,13]]
B=[[-1,-2,-3],[4,-5,6],[9,-8,-7]]
C=[[0,0,0],[0,0,0],[0,0,0]]
D=[[0,0,0],[0,0,0],[0,0,0]]
for i in range (3):
    for j in range(3):
        C[i][j]=A[i][j]+B[i][j]
print(C)
for i in range(3):
    for j in range(3):
        D[i][j]=A[i][j]-B[i][j]
print('The A Matrix is')
for j in A:
    print (j)
print('The B Matrix is')
for j in B:
    print (j)
print('The sum of A and B Matrix(C=A+B) is')
for j in C:
    print (j)
print('The Substracted Matrix of A and B(D=A-B) is')
for j in D:
    print (j)
