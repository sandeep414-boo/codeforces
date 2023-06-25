t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    fa=1
    d={}
    f=1
    for i in s:
        if f==1:
            if i not in d:
                d[i]=1
            f=0
        else:
            if i not in d:
                d[i]=0
            f=1
    res=[]
    res.append(d[s[0]])
    #print(d,res)
    for i in range(1,n):
        if res[-1]==d[s[i]]:
            fa=0
            break
        else:
            res.append(d[s[i]])
        
        
        
        
    if fa==1:
        print('YES')
    else:
        print('NO')
            
