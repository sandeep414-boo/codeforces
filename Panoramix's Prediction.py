n,m=map(int,input().split())
flag=0
x=0
for i in range(n+1,m+1):
    
    if i%2==0:
        pass
    else:
        f=0
        for j in range(2,i//2):
            if i%j==0:
                f=1
                break
        if f==0 and x==0:
            x=i
            
if x==m:
    print('YES')
else:
    print('NO')
