t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    if(n%2==0 and m%2==0 ) or (n%2!=0 and m%2!=0):
        print('Tonya')
    else:
        print('Burenka')
