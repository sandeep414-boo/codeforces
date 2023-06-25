t=int(input())
for j in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    c=0
    f=0
    li=[]
    if n>3:
        for i in range(n-1):
            if l[i]>l[i+1]:
                li.append(1)
            else:
                li.append(0)
        for i in range(n-3):
            if li[i]==1 and li[i+1]==0 and li[i+2]==1:
                f=1
                break
        if f==0:
            print('YES')
        else:
            print('NO')
    elif n==3:
            print('YES')
        
    elif n==2:
        if l[0]>l[1]:
            print('NO')
        else:
            print('YES')
    else:
        print('YES')
                
                
                
        
        
