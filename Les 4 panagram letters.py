I=input("Enter word: ")
letters={"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}

I=I.lower()

for i in I:
    print(i)
    if i in letters:
        letters[i]+=1

print("This is the occurence of each letter = ")
print(letters)
result=True
for i in letters.values():
    if i==0:
        result=False
        break

if result:
    print("pangram")
else:
    print("not pangram")
