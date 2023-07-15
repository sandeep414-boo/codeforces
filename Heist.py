n=int(input())
l=list(map(int,input().split()))
l.sort()
ma=0
l.sort()
for i in range(n-1):
    if l[i+1]-l[i]> 1:
        ma+=l[i+1]-l[i]-1
print(ma)
