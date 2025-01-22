I=input("Enter string ")
I=I.lower()
print(I)
vowels={"a":0,"e":0,"i":0,"o":0,"u":0 }

for i in I:
    print(i)
    if i in vowels:
        vowels[i]+=1



print(vowels)





