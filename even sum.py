n=input("enter the number:")
x=len(n)
n=int(n)
sum=0
n1=n
for i in range(0,x,1):
    if((n%10)%2!=0):
        sum+=n%10
    n=n//10
print(sum)
