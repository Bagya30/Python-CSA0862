def fact(n):
    if(n==1):
        return 1
    else:
        return n*fact(n-1)
    
n=eval(input("enter a number:"))
fact=fact(n)
print("factorial=",fact)
