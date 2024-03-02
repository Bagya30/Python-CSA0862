n=eval(input("enter a number:"))
org=n
sum=0
while(n>0):
    a=n%10
    sum=sum+a*a*a
    n=n//10             
if(sum==org):
    print("armstrong number")
else:
    print("not a armstrong number")

                
