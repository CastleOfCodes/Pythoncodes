n1=0
n2=1
i=0
n=int(input())
if(n==0):
    print("Enter valid number")
elif(n==1):
    print(n1)
else:
    print(n1)
    print(n2)
    while(i<n-2):
        k=n1+n2
        n1=n2
        n2=k
        i+=1
        print(k)