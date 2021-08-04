n=int(input())
temp=n
sum=0
while(temp>0):
    dig=temp%10
    sum=(sum*10)+dig
    temp=temp//10
if(n==sum):
    print("Palindrome")
else:
    print("Not Palindrome")