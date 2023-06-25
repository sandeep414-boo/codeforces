t=int(input())
for i in range(t):
    n=int(input())
    if n>1:
        l1=list(map(str,input().split()))
        l2=list(map(str,input().split()))
        l3=list(map(str,input().split()))
    else:
        l1,l2,l3=[],[],[]
        s1=input()
        l1.append(s1)
        s2=input()
        l2.append(s2)
        
        s3=input()
        l3.append(s3)
    
    d={}
    for j in l1:
        if j not in d:
            d[j]=3
            
    for j in l2:
        if j not in d:
            d[j]=3
        else:
            d[j]=1
    for j in l3:
        if j not in d:
            d[j]=3
        else:
            if d[j]==1:
                d[j]=0
            else:
                d[j]=1
    #print(d)
    c1,c2,c3=0,0,0
    for j in l1:
        c1+=d[j]
    for j in l2:
        c2+=d[j]
    for j in l3:
        c3+=d[j]
    print(c1,c2,c3)
    
            
    
    
    
