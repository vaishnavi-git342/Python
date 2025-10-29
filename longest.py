list=input("Enter a list of words separated by spaces:").split(" ")
longest_lenght=0
for word in list:
    if len(word)>longest_lenght:
        longest_lenght=len(word)
        long_word=wordprint("The longest word is",long_word)
        print("The length of the longest word is:",longest_lenght)