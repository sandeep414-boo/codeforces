t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    if n==k:
        print('0')
    else:
        x=l.copy()
        x.sort()
        c=0
        x=x[:k]
        for i in range(k):
            if l[i] not in x:
                c+=1
        print(c)
        
        
