t=int(input())

for i in range(t):
    n,d=map(int,input().split())
    s=input()
    res=''
    f=0
    for i in s:
        if int(i)<d and f==0:
            res+=str(d)+i
            f=1
        else:
            res+=i

    if len(res)==n:
        res+=str(d)
    print(int(res))
