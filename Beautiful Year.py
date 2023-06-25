n=int(input())
n=n+1
while True:
    d={}
    f=0
    ref=n
    while n>0:
        r=n%10
        if r not in d:
            d[r]=1
        else:
            f=1
            break
        n//=10
    if f==0:
        print(ref)
        break
    ref+=1
    n=ref
        
