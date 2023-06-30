t=int(input())
for i in range(t):
    n,k,x=map(int,input().split())
    l=[]
    if x!=1:
        
        print('YES')
        l=[1]*n
        print(len(l))
        for i in l:
            print(i,end=' ')
    else:
        if n%2==0:
            if k>1:
                print('YES')
                l=[2]*(n//2)
                print(len(l))
                for i in l:
                    print(i,end=' ')
            else:
                print('NO',end=' ')
        else:
            if k>2:
                ref=n
                while n>1:
                    l.append(2)
                    n-=2
                if n==1:
                    l.pop()
                    l.append(3)
                    #print(l)
                    if sum(l)==ref:
                        print('YES')
                        print(len(l))
                        
                        for i in l:
                            print(i,end=' ')
                    else:
                        print('NO',end=' ')
                else:
                    print('NO',end=' ')
                
            
            else:
                print('NO',end=' ')
    print()
                
                
            
            
            
        
        
        
