t=int(input())
for i in range(t):
    d={}
    n=int(input())
    l=list(map(int,input().split()))
    d[l[0]]=1
    c=l[0]
    for i in range(1,n):
        if l[i] in d:
            c=l[i]
            break
        else:
            d[l[i]]=1
    for i in range(n):
        if l[i]!=c:
            print(i+1)
            
            
    
    
            
