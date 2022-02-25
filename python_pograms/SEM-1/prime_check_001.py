print('Enter Your Number')
x=int(input())
for i in range (2,x):
    if x%i==0:
        print('Number is Not Prime')
        print (i),'times',x/i
        break
else:
        print('Number is Prime')
