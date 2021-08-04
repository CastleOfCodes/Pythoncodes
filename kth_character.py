def charat(str,n):
    dec=' '
    i=0
    while(i<len(str)):
        dec+=str[i]*int(str[i+1])
        i+=2
    if(n>len(dec)):
        print(-1)
    else:
        print(dec[n])

str=input()
n=int(input())
charat(str,n)

"""
----------------------------------Example1------------------------------------------
#input1 - a3b2
#input2 - 7
#output - -1
#---------------------------------Example2---------------------------------------------
#input1 - a3b5
#input2 - 7
#output - b
"""