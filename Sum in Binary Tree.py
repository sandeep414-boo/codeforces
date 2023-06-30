t=int(input())
for i in range(t):
    n=int(input())
    s=n
    while n>1:
        s+=n//2
        n=n//2
    else:
        s+=1
    print(s-1)
