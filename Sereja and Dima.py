n=int(input())
l=list(map(int,input().split()))
m1=0
m2=0
for i in range(n//2):
    if i%2==0:
        if l[i]>l[n-i-1]:
            m1+=l[i]
            m2+=l[n-i-1]
        else:
            m1+=l[n-i-1]
            m2+=l[i]
    else:
        if l[i]>l[n-i-1]:
            m2+=l[i]
            m1+=l[n-i-1]
        else:
            m2+=l[n-i-1]
            m1+=l[i]
    #print(l[i],l[n-i-1])
if n%2!=0:
    m1+=l[n//2]//2
    m2+=l[n//2]//2
print(m1,m2)
        
    
    
