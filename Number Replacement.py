t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    s=input()
    d={}
    for j in range(n):
        if l[j] not in d:
            d[l[j]]=s[j]
    res=''
    for j in l:
        res+=d[j]
    if res==s:
        print('YES')
    else:
        print('NO')
