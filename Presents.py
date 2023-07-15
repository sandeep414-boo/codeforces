n=int(input())
d={}
l=list(map(int,input().split()))
for i in range(n):
    d[i+1]=l[i]
for v in d.keys():
    l[d[v]-1]=v
for i in l:
    print(i,end=' ')
    
