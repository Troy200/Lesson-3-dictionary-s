I=input("Enter number")
pangram={"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}


for i in I:
    print(i)
    if i in pangram:
        pangram[i]+=1


print(pangram)
result=True
for i in pangram.values():
    if i==0:
        result=False
        break
  
if result:
    print("pangram")
else:
    print("not pangram")


