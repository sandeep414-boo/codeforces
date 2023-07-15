t=int(input())
for i in range(t):
    n=int(input())
    x=n%7
    if x==0:
        print(n)
    else:
        y1=n-x
        y2=n+7-x
        if y2//10==n//10:
            print(y2)
        elif y1//10==n//10:
            print(y1)
        else:
            print(y2)
        
        
        
