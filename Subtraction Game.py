t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    
    if a>=3:
        print('2')
    else:
        if a*2<b:
            
            print(a*2)
        else:
            print(a+b)
