n,k=map(int,input().split())
l=list(map(int,input().split()))
nu=l[k-1]
c=0
for i in l:
    if i>=nu and i>0:
        c+=1
print(c)
