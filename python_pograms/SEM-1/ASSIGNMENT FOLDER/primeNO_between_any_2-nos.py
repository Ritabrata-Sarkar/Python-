'''
Name : Ritabrata Sarkar
Roll NO. 2835
Question: To Find out all the prime no.s between 2 given numbers by using python programme.
'''
low=int(input("enter Lower Range"))
up=int(input("enter upper Range"))
count=0
for num in range(low,up+1):
    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            count=count+1
            print(num,end=" ")

print()
print("Total prime numbers are",count)
