t=int(input())
for j in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    s=[]
    f=0
    for i in l:
        if len(s)==0:
            s.append(i)
        elif s[-1]==i:
            s.append(i)
            f=1
        else:
            if f==1:
                x=s[-1]
                try:
                    while x==s[-1]:
                        s.pop()
                except:
                    pass
                    
                
            if i in s:
                while s[-1]!=i:
                    s.pop()
                s.pop()
            else:
                s.append(i)
            f=0
        #print(s)
    x=0
    for i in range(len(s)):
        #print(s[i+1:])
        if s[i] in s[i+1:]:
            break
        x+=1
    print(n-x)
                    
