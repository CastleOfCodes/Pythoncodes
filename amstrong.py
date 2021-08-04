n=int(input())
temp=n
sum=0
while(n>0):
    d=n%10
    sum+=(d**3)
    n=n//10
if(temp==sum):
    print("Amstrong")
else:
    print("Not amstrong")