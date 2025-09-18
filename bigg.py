a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))

if a>b:
    if a>c:
        print("the biggest number is :",a)
    else:
        print("the biggest number is:",c)
else:
    if b>c:
        print("the biggest number is:",b)
    else:
        print("the biggest number is:",c)
