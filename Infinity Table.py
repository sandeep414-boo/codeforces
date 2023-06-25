import math
t=int(input())
for i in range(t):
    n=int(input())
    x=int(math.sqrt(n))
    if n==x*x:
        print(x,'1')
    else:
        y=n-x*x
        if y<x+1:
            r=y
            c=x+1
        else:
            r=x+1
            y=y-r
            c=r-y
        print(r,c)
        
        
        
        
