l,r=map(int,input().split())
f=0
while l<=r:
    d={}
    n=l
    while n>0:
        if n%10 in d:
            break
        else:
            d[n%10]=1
        n//=10
    else:
        print(l)
        f=1
        break
    
    l+=1
if f==0:
    print(-1)
    
    
