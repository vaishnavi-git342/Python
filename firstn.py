def compare(s1, s2, n):
   
    for i in range(n):
        if s1[i] != s2[i]:
            return "false"
    return "true"


s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")
n = int(input("Enter the number of characters to compare: "))

print("The first", n, "characters of both strings are the same?:", compare(s1, s2, n))
