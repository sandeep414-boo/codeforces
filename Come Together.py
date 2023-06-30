t=int(input())
for i in range(t):
    xa,ya=map(int,input().split())
    xb,yb=map(int,input().split())
    xc,yc=map(int,input().split())
    c=0
    f=True
    if xa > xb and xa> xc:
        c=min(xb,xc)
        f=False
    elif xa == xb and xa == xc and xa == xb and xa == xc:
        c+=1
        f=True
    else:
        c=min(xb,xc)
        f=True
        
        

    if ya > yb and ya> yc and f:
        c+=min(yb,yc)
    elif ya > yb and ya> yc and f==False:
        c=0
        c+=abs(xa-min(xb,xc))+abs(ya-min(yb,yc))
        c+=1
    elif ya < yb and ya< yc and f==False:
        c=0
        c+=abs(xa-min(xb,xc))+abs(ya-min(yb,yc))
        c+=1
    elif ya < yb and ya< yc and f:
        c+=min(yb,yc)
        
        
    elif ya == yb and ya == yc and (ya == yb and ya == yc and xa!=ya):
        c+=1
    print(c)
    
        
