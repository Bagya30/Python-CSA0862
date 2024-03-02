elements=eval(input("Enter the list elements: "))
M=eval(input("M="))
N=eval(input("N="))
sorted_elements=sorted(elements)
if M>len(elements) or N>len(elements):
    print("M or N value is out of range. Please enter valid values.")
else:
    max=sorted_elements[-M]
    min=sorted_elements[N - 1]
    sum=max+min
    diff=abs(max-min)

    print(M,"Maximum Number =",max)
    print(N," Minimum Number =",min)
    print("Sum =", sum)
    print("Difference =", diff)
