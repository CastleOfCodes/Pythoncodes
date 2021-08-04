n=int(input())
l=list(map(int,input().split()))
l=sorted(l)
s=0
c=0
count=0
for i in l:
    s+=i
for i in l[::-1]:
    c+=i
    count+=1
    if(c>s/2):
        break
print(count)