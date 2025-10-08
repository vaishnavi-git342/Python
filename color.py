list1=input("enter colors in list1(separated with space):").split()
list2=input("enter colors in list2(separated with space):").split()
result=[]
for color in list1:
    if color not in list2:
        result.append(color)
    print(result)