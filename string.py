str=input("enter a string:")
word={}
for char in str:
    if char in str:
        if char in word:
            word[char]+=1
        else:
            word[char]=1
            print("Character frequency:")
            for char,count in word.items():
                print(f"{char}:{count}")