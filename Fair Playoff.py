t=int(input())
for i in range(t):
    l=list(map(int,input().split()))
    x=max(l[0],l[1])
    y=max(l[2],l[3])
    l.sort()
    le=[x,y]
    le.sort()
    if l[-1]==le[-1] and l[-2]==le[-2]:
        print('YES')
    else:
        print('NO')
