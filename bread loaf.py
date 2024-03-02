n=int(input("Enter no.of fresh loves Purchased: "))
m=int(input("Enter no.of day old loves Purchased: "))

reg=185.00
new=reg*n
old=111*m
print("regular Price: Rs.185.00")
roun=format(new,".2f")
row=format(old,".2f")
print("Amount new loves: ",roun)
print("Amount of old loves", row)
total=new+old
tot=format(total,".2f")
print("Total Amount: ",tot)
