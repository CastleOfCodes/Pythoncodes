n=int(input())
s=input()
counta=0
countd=0
for i in s:
    if(i=='A'):
        counta+=1
    else:
        countd+=1
if(counta>countd):
    print("Anton")
elif(counta<countd):
    print("Danik")
else:
    print("Friendship")