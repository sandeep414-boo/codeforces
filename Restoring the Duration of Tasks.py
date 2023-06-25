t=int(input())
for i in range(t):
    
    n=int(input())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))

    res=[]
    for j in range(n):
        if j==0:
            res.append(l2[j]-l1[j])
        else:
            ma=max(l1[j],l2[j-1])
            res.append(l2[j]-ma)
    for j in res:
        print(j,end=' ')
    print()
    
