t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    d={}
    f=0
    ch=''
    for i in s:
        if i in d:
            if i!=ch:
                f=1
                break
        else:
            d[i]=i
            ch=i
    if f==1:
        print('NO')
    else:
        print('YES')
            
        
