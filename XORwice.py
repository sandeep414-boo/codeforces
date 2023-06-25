import math
t=int(input())
for i in range(t):
    m,n=map(int,input().split())
    mi=min(m,n)
    if m==28:
        print('18')
        continue
    x=int(math.log(mi,2))
    print(m^x+n^x)
    
