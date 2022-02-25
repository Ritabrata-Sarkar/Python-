a=[8,5,9,2,-2,13,-56,78,96,89]
for i in range(len(a)-1,0,-1):
    for j in range(1,i+1):
        if a[j]<a[j-1]:
            a[j-1],a[j]=a[j],a[j-1]
print (a)
