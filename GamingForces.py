t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    x=l.count(1)
    y=l.count(2)
    res=0
    f=1
    if x!=0:
        if x%2==0:
            res=x//2
        else:
            res=x//2
            if y>0:
                res+=1
                f=0
            else:
                res+=1
    for i in l:
        if i!=1:
            if i==2 and f==0:
                res+=1
                f=1
            elif i==2:
                res+=1
            else:
                res+=1
    print(res)
        
