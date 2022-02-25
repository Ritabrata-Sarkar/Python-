a=[]
n=input('Enter total number of elements')
for i in range(int(n)):
    a.append(input())
print (a)
b=[float(j)/2.0 for j in a]
print (b)
print ('sum of b list', float(sum(b)))
print ('average of b list', sum(b)/len(b))
