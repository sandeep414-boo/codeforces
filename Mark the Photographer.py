t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    l=list(map(int,input().split()))
    l.sort()
    l1=l[:n]
    l2=l[n:]
    f=0
    #print(l1,l2)
    for i in range(n//2):
        if l2[i]-l1[i]<x:
            #print(l2[i]-l1[i])
            f=1
            break
    if f==0:
        print('YES')
    else:
        print('NO')
