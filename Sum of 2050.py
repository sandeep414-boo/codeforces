t=int(input())
for i in range(t):
    n=int(input())
    if n<2050 and n%2050!=0:
        print('-1')
    else:
        n=n//2050
        s=0
        while n>0:
            s=s*10+n%10
            n=n//10
        print(s)
            
            
    
