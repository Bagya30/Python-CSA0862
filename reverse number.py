n=int(input("enter a number:"))
temp=n
rev=0
num=0
while(n>0):
    num=n%10
    rev=rev*10+num
    n=n//10
if(temp==rev):
    print("palindrome ")
else:
    print("not a palindrome")
print(rev)
    
