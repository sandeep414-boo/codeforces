n=int(input())
mi=0
for i in range(n):
    a,b=map(int,input().split())
    if i==0:
        x=b
    else:
        x=x-a
        x+=b
    if mi<x:
        mi=x
print(mi)
    
