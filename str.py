text=input("enter a string:")
first_char=text[0]
result=first_char+text[1:].replace(first_char,'$')
print("Result:", result)