n,k=map(int,input().split())
c=0
f=0
for i in range(n+1):
    c+=i*5
    if c+k>240:
        f=1
        break
if f==1:
    print(i-1)
else:
    print(i)
    
