t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    c=0
    l=0
    j=1
    while j<n:
        if (arr[i]+arr[j])%2==0:
            i=j
            j+=1
        else:
            if (arr[j-1]+arr[j])%2==0:
                i=j
                j+=1
                
            else:
                j+=1
            c+=1
            
    print(c)
            
