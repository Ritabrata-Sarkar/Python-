a=[6,10,12,1,-10,-4,5,0]
for i in range(len(a)):
    for j in range(i,len(a)):
        if a[j]<a[i]:
            a[i],a[j]=a[j],a[i]
print('the sorted list is ',a)
