t=int(input())
for j in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    for i in range(n):
        if l[i]>k:
            l[i]=l[i]%k
    d={}
    for i in range(n):
        if l[i] in d:
            x=d[l[i]]
            x.append(i+1)
        else:
            x=[i+1]
            d[l[i]]=x
    res=[]
    for i in range(k,0,-1):
        try:
            for v in d[i]:
                res.append(v)
        except:
            pass
    for i in res:
        print(i,end=' ')
    print()
            
        
